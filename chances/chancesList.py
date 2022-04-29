from dataclasses import dataclass

import pandas as pd

from chances import Chance


@dataclass
class ChancesList:
    def __init__(self):
        self.chance_list = []
        self.get_chances_from_csv()

    def get_chances_from_csv(self):
        data_list = pd.read_csv("./data/chances.csv", encoding="UTF-8")

        for _, attributes in data_list.iterrows():
            self.chance_list.append(
                Chance(
                    chance_id=attributes["chance_id"],
                    chance_text=attributes["chance_text"],
                    chance_prize=attributes["chance_prize"],
                )
            )

    def __str__(self):
        chance_list = '\n'.join(map(str, self.chance_list))
        return chance_list
