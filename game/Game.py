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
                        self.roll_dice(player_id=self.game_state.current_player_id)
                    if action == constants.BUTTON_END_ROUND_ACTION:
                        # Ending round and deleting dice on button click
                        self.game_state.end_round()
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
            # self.process_round()
            self.clock.tick(60)
        print("Close game")

    def roll_dice(self, player_id):
        self.game_state.set_dice()
        dice = self.game_state.dice
        dices_number = dice.dice2_number + dice.dice1_number
        new_card_number = self.game_state.players[player_id].current_card
        self.game_state.update_text(add_text=f"Byłeś na karcie {self.game_state.cards[new_card_number].name}")
        if dices_number == 12:
            self.game_state.update_text(add_text="Wyrzuciłeś 12, następny rzut nastąpi automatycznie")
            self.game_state.del_dice()
            self.game_state.set_dice()
            dice = self.game_state.dice
            dices_number += dice.dice1_number + dice.dice2_number
            if dices_number == 24:
                self.game_state.update_text(add_text="Znowu wyrzuciłeś 12, trafiasz do więzienia")
                # TODO go to jail
                new_card_number = 10
            else:
                new_card_number += dices_number
        else:
            new_card_number += dices_number

        if new_card_number > 28:
            new_card_number -= 28

        self.game_state.update_text(
            add_text=f"Wyrzuciłeś {dices_number}, przenosimy cię na kartę {self.game_state.cards[new_card_number].name}")

        self.game_state.move_player_to_card(player_id=player_id, card_id=new_card_number)
