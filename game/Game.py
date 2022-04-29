import pygame

from game import Board


class Game:
    def __init__(self):
        pygame.init()

        # Backgroud
        self.board = Board()

        # Loop properties
        self.clock = pygame.time.Clock()
        self.running = True

    def process_input(self):
        # self.moveTankCommand = Vector2(0, 0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    break
                elif event.key == pygame.K_SPACE:
                    self.board.rollDice()
                    break

    def run(self):
        while self.running:
            self.process_input()
            self.board.draw()
            self.clock.tick(60)

    def button_click(self, event):
        pass
