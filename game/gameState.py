import time
from random import random

from pygame import Vector2

import constants
from cards import cardsList
from chances.chances import get_random_card, get_chances_from_csv
from game import Dice
from game.AI import AI
from game.Player import Player





class GameState:
    def __init__(self, game_mode):
        self.dice = None
        self.ai_players_count = game_mode
        self.players = self.set_players()
        self.cards = cardsList.get_cards_from_csv()
        self.chancesList = get_chances_from_csv()
        self.text = constants.TEXT_START
        self.round_id = 0
        self.current_player_id = -1
        self.button_roll_dice_state = False
        self.button_end_round_state = True
        print(f'Run game with mode {self.ai_players_count}')

    def set_dice(self):
        self.dice = Dice()

    def del_dice(self):
        self.dice = None

    # Creates list of players
    def set_players(self):
        list_of_players = [Player(0, "human")]

        for x in range(1, self.ai_players_count + 1):
            list_of_players.append(AI(x))

        return list_of_players

    def turn_off_player(self, player_id):
        self.players[player_id].set_status()

    def set_card_owner(self, card_id, player_id):
        self.cards[card_id].owner = player_id

    def del_card_owner(self, card_id):
        self.cards[card_id].owner = None
        self.cards[card_id].buildings = None

    def update_text(self, add_text="Remove"):
        if add_text == "Remove":
            self.text = ""
        else:
            self.text = "{} {}".format(self.text, add_text)

    def move_player_to_card(self, player_id, card_id):
        card_position = Vector2(self.cards[card_id].position_h, self.cards[card_id].position_w)
        self.players[player_id].move_pawn(card_position, card_id)

    def move_players_to_start(self):
        for player in self.players:
            self.move_player_to_card(player.player_id, 0)

    def start_next_round(self):
        self.current_player_id = self.set_next_player()
        self.round_id += 1
        self.update_text(add_text=f" Tura {self.round_id}, Gracz nr {self.current_player_id + 1} \n")
        # Check if player is in jail
        if self.players[self.current_player_id].inJail:
            self.update_text(add_text=f" Gracz był w więzieniu, więc nie może wykonać żadnej akcji \n")
            self.players[self.current_player_id].inJail = False
            self.start_next_round()
        else:
            # Check if player is AI
            if self.players[self.current_player_id].typeOfPlayer == "AI":
                self.ai_round()
            else:
                self.human_round()

    def ai_round(self):
        self.button_roll_dice_state = False
        self.button_end_round_state = False
        self.roll_dice()
        self.process_card_event()
        self.del_dice()
        self.start_next_round()

    def human_round(self):
        self.button_end_round_state = False
        self.button_roll_dice_state = True
        self.update_text(add_text="Rzuć kostką aby kontynuować...")

    def set_next_player(self):
        new_id = self.current_player_id
        while True:
            new_id += 1
            if new_id > self.ai_players_count:
                new_id = -1
            elif self.players[new_id].status == 1:
                break

        return new_id
    def go_jail(self, player_id):
        self.move_player_to_card(player_id, 10)
        self.players[self.current_player_id].inJail = True

    def process_card_event(self):
        player_id = self.current_player_id
        card_id = self.players[player_id].current_card
        card_type = self.cards[card_id].class_type
        card_name = self.cards[card_id].name
        text = ""
        if card_type == "ActionCard":
            card_type = self.cards[card_id].card_type
            if card_type == "Chance":
                self.process_chance_event()
            elif card_type == "Start":
                text = "Jesteś na starcie. Nic się nie dzieje. \n"
            elif card_type == "Jail":
                text = "Jesteś w więzieniu. \n"
                self.players[self.current_player_id].inJail = True
            elif card_type == "FreePass":
                text = "Jesteś na parkingu. Nic się nie dzieje \n"
            elif card_type == "WaitInJail":
                text = "Trafiłeś na kartę cofającą do więzienia \n"
                self.go_jail(player_id)
        elif card_type == "Street":
            text = f"Jesteś na karcie {card_name}.\n"
            # TODO: event for street
        elif card_type == "Company":
            text = f"Jesteś na karcie firmy {card_name}.\n"
            # TODO: event for Company
        self.update_text(add_text=text)
        if self.players[self.current_player_id].typeOfPlayer == "human":
            self.button_end_round_state = True
            self.button_roll_dice_state = False

    def check_ownership(self, card_id):

        if self.cards[card_id].owner is None:
            self.update_text(add_text=f"Karta jest dostępna do zakupu.\n")
            # buy_card() - there are two types of cards : street and company
        elif self.cards[card_id].owner != self.current_player_id:
            self.update_text(add_text=f"Musisz zapłacić graczowi.\n")
            # pay_to(owner)  - there are two types of cards : street and company
        else:
            self.update_text(add_text=f"Karta należy do ciebie.\n")

    def roll_dice(self):
        player_id = self.current_player_id
        self.set_dice()
        dice = self.dice
        dices_number = dice.dice2_number + dice.dice1_number
        new_card_number = self.players[player_id].current_card
        if dices_number == 12:
            self.update_text(add_text="Wyrzuciłeś 12, następny rzut nastąpi automatycznie. ")
            self.del_dice()
            self.set_dice()
            dice = self.dice
            dices_number += dice.dice1_number + dice.dice2_number
            if dices_number == 24:
                new_card_number = 10
            else:
                new_card_number += dices_number
        else:
            new_card_number += dices_number

        if new_card_number > 28:
            new_card_number -= 28
            self.players[player_id].update_money(200)

        self.update_text(
            add_text=f"Wyrzuciłeś {dices_number}.")

        self.move_player_to_card(player_id=player_id, card_id=new_card_number)

    def process_chance_event(self):
        card = get_random_card(self.chancesList)
        self.update_text(
            add_text=f"Losowanie karty szansy...  {card.chance_text}. \n")
        # pay money, go to jail, get money, go to start
        if card.chance_prize == "jail":
            self.go_jail(self.current_player_id)
        elif card.chance_prize == "start":
            self.move_player_to_card(self.current_player_id, 0)
        elif "pay" in card.chance_prize:
            prize = card.chance_prize
            prize = prize.replace("pay_", "")
            self.players[self.current_player_id].update_money(-int(prize))
            #TODO: what if the player needs to pay more than in bank
        elif "get" in card.chance_prize:
            prize = card.chance_prize
            prize = prize.replace("get_", "")
            self.players[self.current_player_id].update_money(int(prize))
