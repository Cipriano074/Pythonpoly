from game.Player import Player


class AI(Player):
    def __init__(self, player_id):
        super().__init__(player_id, name="AI")

    def buy_card(self, card):
        buy = False
        text = f"AI nie kupiło karty {card.name} \n"
        if self.money >= card.basic_buy_price:
            self.money -= card.basic_buy_price
            buy = True
            text = f"AI kupiło kartę {card.name} \n"
        return buy, text