import random

import pygame
from pygame.rect import Rect

import constants as c


class Dice:
    def __init__(self):
        self.dice1Texture, self.dice2Texture = self.load_dice()

    @staticmethod
    def load_dice():
        dice1_number, dice2_number = random.randint(1, 6), random.randint(1, 6)
        seq1 = ("./img/dice_", str(dice1_number), ".png")
        seq2 = ("./img/dice_", str(dice2_number), ".png")

        return pygame.image.load("".join(seq1)).convert(), pygame.image.load("".join(seq2)).convert()

    def render_dice(self):
        dice1_texture_rect = Rect(c.DICE1_POSITION.x, c.DICE1_POSITION.y, c.DICE_SIZE.x, c.DICE_SIZE.y)
        dice2_texture_rect = Rect(c.DICE2_POSITION.x, c.DICE2_POSITION.y, c.DICE_SIZE.x, c.DICE_SIZE.y)

        return (self.dice1Texture, dice1_texture_rect), (self.dice2Texture, dice2_texture_rect)
