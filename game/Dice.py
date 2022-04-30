import random

import pygame
from pygame import Vector2
from pygame.rect import Rect


class Dice:
    def __init__(self):
        self.cellSize = Vector2(40, 40)
        self.dice1Texture, self.dice2Texture = self.load_dice()

        self.dice1Pos = Vector2(973, 569)
        self.dice2Pos = Vector2(1039, 569)

    @staticmethod
    def load_dice():
        dice1_number, dice2_number = random.randint(1, 6), random.randint(1, 6)
        seq1 = ("./img/dice_", str(dice1_number), ".png")
        seq2 = ("./img/dice_", str(dice2_number), ".png")

        return pygame.image.load("".join(seq1)).convert(), pygame.image.load("".join(seq2)).convert()

    def render_dice(self):
        dice1_texture_rect = Rect(int(self.dice1Pos.x), int(self.dice1Pos.y),
                                  int(self.cellSize.x),
                                  int(self.cellSize.y))
        dice2_texture_rect = Rect(int(self.dice2Pos.x), int(self.dice2Pos.y),
                                  int(self.cellSize.x),
                                  int(self.cellSize.y))

        return (self.dice1Texture, dice1_texture_rect), (self.dice2Texture, dice2_texture_rect)