import pygame

from game import Board
from game.gameState import GameState


class Game:
    def __init__(self):
        pygame.init()

        # Game state
        self.game_state = GameState()

        # Graphics
        self.board = Board(self.game_state)

        # Loop properties
        self.clock = pygame.time.Clock()
        self.running = True

    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    break
                elif event.key == pygame.K_UP:
                    # Set dice
                    self.game_state.set_dice()
                    break
                elif event.key == pygame.K_DOWN:
                    # Delete dice
                    self.game_state.del_dice()
                    break

    def run(self):
        while self.running:
            self.process_input()
            self.board.draw()
            self.clock.tick(60)

    def button_click(self, event):
        pass
