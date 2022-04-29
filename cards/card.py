from dataclasses import dataclass


@dataclass
class Card:
    card_id: int = None
    class_type: str = None
    card_type: str = None
    name: str = "No name"
    basic_buy_price: int = 0
    rent_price: int = 0
    build_price: int = 0
    __position: tuple = None
    __owner: int = None

    @property
    def owner(self, new_owner: int):
        self.__owner = new_owner

    @property
    def position(self, new_position: tuple):
        self.__position = new_position

    @owner.getter
    def owner(self):
        return self.__owner

    @position.getter
    def position(self):
        return self.__position

    def __str__(self):
        return f"""Card {self.card_id}: {self.card_type}, {self.name}. The base price is {self.basic_buy_price}.
        The owner is {self.__owner}. \n"""

    def __eq__(self, other):
        return self.name == other.name
