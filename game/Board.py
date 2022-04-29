import pygame
from pygame import Rect

import constants
from game.gameState import GameState


class Board:
    def __init__(self):
        self.window = pygame.display.set_mode(constants.SCREEN_SIZE)
        pygame.display.set_caption(constants.GAME_NAME)
        self.screen = pygame.display.get_surface()
        self.background_image = pygame.image.load("./img/background.png").convert()

        self.gameState = GameState()

        self.rollDiceCommand = None

    def draw(self):
        self.screen.blit(self.background_image, (0, 0))
        # self.update()
        if self.rollDiceCommand:
            self.render_dice()
        pygame.display.flip()

    def rollDice(self):
        self.gameState.set_dice()
        self.rollDiceCommand = 1

    def render_dice(self):
        # Dice
        dice1_texture_rect = Rect(int(self.gameState.dice.dice1Pos.x), int(self.gameState.dice.dice1Pos.y),
                                  int(self.gameState.dice.cellSize.x),
                                  int(self.gameState.dice.cellSize.y))
        dice2_texture_rect = Rect(int(self.gameState.dice.dice2Pos.x), int(self.gameState.dice.dice2Pos.y),
                                  int(self.gameState.dice.cellSize.x),
                                  int(self.gameState.dice.cellSize.y))
        self.window.blit(self.gameState.dice.dice1Texture, dice1_texture_rect)
        self.window.blit(self.gameState.dice.dice2Texture, dice2_texture_rect)
