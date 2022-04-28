# triggering the project
from cards.card import Card


def run():
    print("Running")
    get_cards()


def get_cards():
    card_test = Card(name="Siurek")
    print(card_test)


if __name__ == '__main__':
    run()
