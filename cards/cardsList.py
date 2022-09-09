import pandas as pd

from cards import Card


def get_cards_from_csv():
    data_list = pd.read_csv("./data/cards.csv", encoding="UTF-8")
    cards_list = []
    for _, attributes in data_list.iterrows():
        cards_list.append(
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
    return cards_list
