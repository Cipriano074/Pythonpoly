# triggering the project

import pygame

from game import Game


def run():
    print("Run")
    game = Game()
    game.run()


if __name__ == '__main__':
    run()
    pygame.quit()
