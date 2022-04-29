# triggering the project

import pygame

import constants as c
from board import Board


def run():
    print("Running")

    pygame.display.set_mode(c.SCREEN_SIZE)
    pygame.display.set_caption(c.GAME_NAME)

    board = Board(c.GAME_NAME)

    while not board.end_game:
        board.run()


if __name__ == '__main__':
    run()
    pygame.quit()