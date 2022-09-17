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
    position_h: int = 0
    position_w: int = 0
    __owner: int = None
    buildings: int = None

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, new_owner: int):
        if self.__owner is None:
            self.__owner = new_owner
            self.buildings = 0
            print(f'The new owner of card {self.name}, is Player {self.__owner}')
        else:
            self.__owner = new_owner
            print(f"There is no owner of card {self.name}")

    def __str__(self):
        return f"""Card {self.card_id}: {self.card_type}, {self.name}. The base price is {self.basic_buy_price}.
        The owner is {self.__owner}. \n"""

    def __eq__(self, other):
        return self.name == other.name
