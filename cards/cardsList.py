from dataclasses import dataclass

import pandas as pd

from cards import Card


@dataclass
class CardsList:
    def __init__(self):
        self.cards_list = []
        self.get_cards_from_csv()

    def get_cards_from_csv(self):
        data_list = pd.read_csv("./data/cards.csv", encoding="UTF-8")

        for _, attributes in data_list.iterrows():
            self.cards_list.append(
                Card(
                    card_id=attributes["card_id"],
                    class_type=attributes["class_type"],
                    card_type=attributes["card_type"],
                    name=attributes["name"],
                    basic_buy_price=attributes["basic_buy_price"],
                    rent_price=attributes["rent_price"],
                    build_price=attributes["build_price"]
                )
            )

    def __str__(self):
        cards_list_str = '\n'.join(map(str, self.cards_list))
        return cards_list_str
