import pygame
from pygame import Vector2
from pygame.rect import Rect

import constants


class Player:

    def __init__(self, player_id, name):
        self.player_id = player_id
        self.typeOfPlayer = name
        self.money = 200
        self.status = 1
        self.inJail = False
        self.base_position = self.set_base_position()
        self.current_position = self.base_position
        self.current_card = 0
        self.pawn_texture = self.load_pawn_texture()
        print(f'Created a player {self.player_id},  {self.typeOfPlayer}')

    def __str__(self):
        return f"""Player {self.player_id}: {self.typeOfPlayer}, {self.money} $.
               \n"""

    def update_money(self, amount):
        self.money += amount

    def set_status(self):
        self.status = 0

    def set_base_position(self):
        position = Vector2(0, 0)
        if self.player_id == 1:
            position += (30, 0)
        elif self.player_id == 2:
            position += (0, 30)
        elif self.player_id == 3:
            position += (30, 30)
        return position

    def load_pawn_texture(self):

        file = ("./img/pawn_", str(self.player_id), ".png")
        return pygame.image.load("".join(file)).convert_alpha()

    def load_pawn_rect(self):

        pawn_rect = Rect(self.current_position.x, self.current_position.y, constants.PAWN_SIZE.x, constants.PAWN_SIZE.y)

        return self.pawn_texture, pawn_rect

    def move_pawn(self, card_position, card_id):
        self.current_position = self.base_position + card_position
        self.current_card = card_id


