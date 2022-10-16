import pandas as pd

from cards import Card


def get_cards_from_csv():
    # data_list = pd.read_csv("./data/cards.csv", encoding="UTF-8")
    data_list = pd.read_csv("./data/cards2.csv", encoding="UTF-8")
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
                build_price=attributes["build_price"],
                position_h=attributes["card_h"],
                position_w=attributes["card_w"]
            )
        )
    return cards_list


def del_ownership_from_cards(cards_list, player_id):
    new_cards_list = []
    print(f'The player {player_id} is dead. Del all of his cards')
    for card in cards_list:
        if card.owner == player_id:
            card.del_owner()
        new_cards_list.append(card)

    return new_cards_list
