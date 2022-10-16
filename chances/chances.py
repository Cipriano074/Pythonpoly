import random

import pandas as pd

from chances import Chance


def get_chances_from_csv():
    data_list = pd.read_csv("./data/chances.csv", encoding="UTF-8")
    chance_list = []
    for _, attributes in data_list.iterrows():
        chance_list.append(
            Chance(
                chance_id=attributes["chance_id"],
                chance_text=attributes["chance_text"],
                chance_prize=attributes["chance_prize"],
            )
        )
    return chance_list


def get_random_card(chancesList):
    chance_id = random.randint(0, 14)
    return chancesList[chance_id]
