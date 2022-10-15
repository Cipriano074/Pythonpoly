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

    def run(self):
        while self.running:
            self.process_events()
            self.board.draw()
            self.clock.tick(60)
        print("Close game")
