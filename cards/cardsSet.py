import pandas as pd

from cards import Street, Utility, Company


def get_cards(self):
    cards_list = set()
    cards_list = pd.read_csv("./data/cards.csv", encoding="UTF-8")

    attributes_list = """
    
    attributes['ID'],
    attributes['CLASS'],
    attributes['TYPE'],
    attributes['NAME'],
    attributes['BASE_BUY_PRICE'],
    attributes['RENT_PRICE']
    attributes['BUILD_PRICE']
    """

    for _, attributes in cards_list.iterrows():

        if attributes['CLASS'] == 'Street':
            self.cards_list.add(Street(attributes['ID']))

        elif attributes['CLASS'] == 'Utility':
            self.cards_list.add(Utility())

        elif attributes['CLASS'] == 'Company':
            self.cards_list.add(Company())
