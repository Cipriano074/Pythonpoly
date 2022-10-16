import pygame

import constants
from game.button import ButtonRollDice, ButtonEndRound


class Board:
    def __init__(self, game_state=None):
        self.window = pygame.display.set_mode(constants.SCREEN_SIZE)
        pygame.display.set_caption(constants.GAME_NAME)
        self.screen = pygame.display.get_surface()
        self.background_image = pygame.image.load("./img/background.png").convert()

        self.buttonRollDice = ButtonRollDice()
        self.buttonEndRound = ButtonEndRound()

        self.game_state = game_state

    def draw(self):
        self.screen.blit(self.background_image, (0, 0))
        self.draw_dice()
        # Draw text in main window
        self.draw_text(pos=(800, 235), text=self.game_state.text,
                       font=pygame.font.SysFont('monotxtiv25', 12, bold=True))
        # Draw text for players
        self.draw_players_info()
        # Draw pawns
        self.draw_pawns(self.game_state.players)
        # Draw all the buttons
        self.draw_buttons()

        pygame.display.flip()

    def draw_players_info(self):
        h, w = 805, 110
        for player in self.game_state.players:
            player_info = ""
            if player.status:
                player_info = f"""Żyje
                \nMa {player.money} zł
               \n"""
            else:
                player_info = f"""Nieżyje"""

            self.draw_text(pos=(h, w), text=player_info, font=pygame.font.SysFont('monotxtiv25', 10, bold=True))
            h += 120

    def draw_dice(self):
        # Show dice if generated
        if self.game_state.dice:
            dice1, dice2 = self.game_state.dice.render_dice()
            self.window.blit(*dice1)
            self.window.blit(*dice2)

    def draw_text(self, pos, text, font):
        words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
        space = font.size(' ')[0]  # The width of a space.
        max_width, max_height = self.window.get_size()
        x, y = pos
        for line in words:
            for word in line:
                word_surface = font.render(word, True, constants.BLACK)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]  # Reset the x.
                    y += word_height  # Start on new row.
                self.window.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.

    def draw_pawns(self, players):
        for player in players:
            if player.status:
                pawn = player.load_pawn_rect()
                self.window.blit(*pawn)

    def draw_buttons(self):
        if self.game_state.button_roll_dice_state:
            self.buttonRollDice.draw(self.screen)
        if self.game_state.button_end_round_state:
            self.buttonEndRound.draw(self.screen)

    def check_click(self, pos):
        x, y = pos
        if self.buttonRollDice.clicked(x, y):
            self.buttonRollDice.redraw_clicked()
            return constants.BUTTON_ROLL_DICE_ACTION
        if self.buttonEndRound.clicked(x, y):
            self.buttonEndRound.redraw_clicked()
            return constants.BUTTON_END_ROUND_ACTION

    def redraw_buttons_not_clicked(self):
        self.buttonRollDice.redraw_not_clicked()
        self.buttonEndRound.redraw_not_clicked()
