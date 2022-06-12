from game.Dice import Dice


class GameState:
    def __init__(self, game_mode):
        self.dice = None
        self.ai_players_count = game_mode
        print(f'Run game with mode {self.ai_players_count}')

    def set_dice(self):
        self.dice = Dice()

    def del_dice(self):
        self.dice = None
