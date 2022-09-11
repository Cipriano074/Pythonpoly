import pygame

from game import Board
from game.gameState import GameState


class Game:
    def __init__(self, game_mode):

        # Game state
        self.game_state = GameState(game_mode)

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
                elif event.key == pygame.K_1:
                    # Update text
                    self.game_state.update_text(add_text="trpspapa")
                    break

    def run(self):
        while self.running:
            self.process_input()
            self.board.draw()
            self.clock.tick(60)
        print("Close game")

    def button_click(self, event):
        pass
