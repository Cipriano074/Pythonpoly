from cards import cardsList
from game import Dice
from game.Player import Player


class GameState:
    def __init__(self, game_mode):
        self.dice = None
        self.ai_players_count = game_mode
        self.players_list = self.set_players()
        self.cards = cardsList.get_cards_from_csv()
        self.test()
        print(f'Run game with mode {self.ai_players_count}')

    def set_dice(self):
        self.dice = Dice()

    def del_dice(self):
        self.dice = None

    # Creates list of players
    def set_players(self):
        # Creates list of players
        list_of_players = [Player(0, "human")]

        for x in range(1, self.ai_players_count + 1):
            list_of_players.append(Player(x, "AI"))

        return list_of_players

    def test(self):
        card = self.cards[0]
        print(card.name)
