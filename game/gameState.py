from cards import cardsList
from game import Dice
from game.Player import Player


class GameState:
    def __init__(self, game_mode):
        self.dice = None
        self.ai_players_count = game_mode
        self.players = self.set_players()
        self.cards = cardsList.get_cards_from_csv()
        self.text = ""
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

    def turn_off_player(self, player_id):
        self.players[player_id].set_status()

    def set_card_owner(self, card_id, player_id):
        self.cards[card_id].owner = player_id

    def del_card_owner(self, card_id):
        self.cards[card_id].owner = None

    def test_setting_cards(self):
        self.set_card_owner(0, 0)
        self.del_card_owner(card_id=0)
        print(self.cards[0])

    def update_text(self, add_text="Remove"):
        if add_text == "Remove":
            self.text = ""
        else:
            self.text = "{} {}".format(self.text, add_text)
