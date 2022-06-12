# triggering the project

import pygame

from game import Game
from menu.Menu import Menu


def run():
    print("Run project")
    pygame.init()
    menu = Menu()
    game_mode = menu.run()
    if game_mode:
        game = Game(game_mode)
        game.run()
    print("Close project")


if __name__ == '__main__':
    run()
    pygame.quit()
