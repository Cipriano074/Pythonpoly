from game.Dice import Dice


class GameState:
    def __init__(self):
        self.dice = None

    def set_dice(self):
        self.dice = Dice()

    def del_dice(self):
        self.dice = None
