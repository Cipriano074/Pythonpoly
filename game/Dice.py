import pygame
from pygame import Vector2


class Dice:
    def __init__(self):
        self.cellSize = Vector2(40, 40)
        self.dice1Texture, self.dice2Texture = self.pick_dice()

        self.dice1Pos = Vector2(973, 569)
        self.dice2Pos = Vector2(1039, 569)

    @staticmethod
    def pick_dice():
        dice1_number = "1"
        dice2_number = "3"
        seq1 = ("./img/dice_", dice1_number, ".png")
        seq2 = ("./img/dice_", dice2_number, ".png")

        return pygame.image.load("".join(seq1)).convert(), pygame.image.load("".join(seq2)).convert()
