import pygame

import constants
from game.gameState import GameState


class Board:
    def __init__(self):
        self.window = pygame.display.set_mode(constants.SCREEN_SIZE)
        pygame.display.set_caption(constants.GAME_NAME)
        self.screen = pygame.display.get_surface()
        self.background_image = pygame.image.load("./img/background.png").convert()

        self.gameState = GameState()

    def draw(self):
        self.screen.blit(self.background_image, (0, 0))
        self.update()
        pygame.display.flip()

    def update(self):
        if self.gameState.dice:
            dice1, dice2 = self.gameState.dice.render_dice()
            self.window.blit(*dice1)
            self.window.blit(*dice2)

    def show_dice(self):
        self.gameState.set_dice()

    def hide_dice(self):
        self.gameState.del_dice()
