import pygame

import constants


class Menu:
    def __init__(self):
        # Graphics
        self.board = StartingBoard()

        # Loop properties
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = None

    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    break
                elif event.key == pygame.K_DOWN:
                    self.state = 1
                    self.running = False
                    break

    def run(self):
        print("Run menu")
        while self.running:
            self.process_input()
            self.board.draw()
            self.clock.tick(60)
        print("Close menu")
        return self.state

    def button_click(self, event):
        pass


class StartingBoard:
    def __init__(self):
        self.window = pygame.display.set_mode(constants.SCREEN_SIZE)
        pygame.display.set_caption(constants.GAME_NAME)
        self.screen = pygame.display.get_surface()
        self.background_image = pygame.image.load("./img/background_menu.png").convert()

    def draw(self):
        self.screen.blit(self.background_image, (0, 0))
        self.update()
        pygame.display.flip()

    def update(self):
        # change the image
        pass
