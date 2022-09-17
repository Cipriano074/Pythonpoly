import os

from pygame import Vector2

SCREEN_SIZE = (1280, 768)
GAME_NAME = "Monopoly"
DICE_SIZE = Vector2(40, 40)
DICE1_POSITION = Vector2(973, 569)
DICE2_POSITION = Vector2(1039, 569)
BLACK = (0, 0, 0)
PAWN_SIZE = Vector2(18, 18)
BUTTON_ROLL_DICE_POSITION = Vector2(969, 630)
BUTTON_ROLL_DICE_ACTION = "set_dice"
BUTTON_END_ROUND_POSITION = Vector2(969, 687)
BUTTON_END_ROUND_ACTION = "end_round"

TEXT_START = f"Witaj w grze!\nRozpoczynamy na starcie.\nKażdy z graczy ma po 200 zł w banku."


def get_path(relative_path=""):
    return os.path.join(os.getcwd(), relative_path)
