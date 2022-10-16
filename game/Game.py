import pygame

import constants
from game import Board
from game.gameState import GameState


class Game:
    def __init__(self, game_mode):

        # Game state
        self.game_state = GameState(game_mode)
        self.game_state.move_players_to_start()

        # Graphics
        self.board = Board(self.game_state)

        # Loop properties
        self.clock = pygame.time.Clock()
        self.running = True

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    action = self.board.check_click(event.pos)
                    if action == constants.BUTTON_ROLL_DICE_ACTION:
                        # Rolling dice on button click
                        self.game_state.roll_dice()
                        # Processing events after the player moved to the new card
                        self.game_state.process_card_event()
                        # If human is dead
                        if self.game_state.players[0].status == 0:
                            self.game_state.update_text(add_text="UMARŁES!!!!")
                            self.game_state.start_next_round()
                            self.game_state.del_dice()
                    if action == constants.BUTTON_END_ROUND_ACTION:
                        # Ending round and deleting dice on button click
                        self.game_state.update_text(add_text="Remove")
                        self.game_state.start_next_round()
                        self.game_state.del_dice()
            elif event.type == pygame.MOUSEBUTTONUP:
                self.board.redraw_buttons_not_clicked()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    break

    def check_game_status(self):
        game_over = False
        if self.game_state.round_id > 50:
            print("Game Over. Too many rounds")
            game_over = True
        elif self.game_state.players[0].status == 0:
            print("Close game. Human dead.")
            game_over = True
        else:
            players_alive = []
            for player in self.game_state.players:
                if player.status == 1:
                    players_alive.append(player)
            alive = len(players_alive)
            if alive == 1:
                print(f"The winner is player {players_alive[0].player_id}, {players_alive[0].typeOfPlayer}")
                game_over = True
        if game_over:
            self.running = False

    def run(self):
        while self.running:
            self.process_events()
            self.board.draw()
            self.clock.tick(60)
            self.check_game_status()
        print("Close game")
