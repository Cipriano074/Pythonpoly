import pygame


class Board:
    def __init__(self, text):
        self.screen = pygame.display.get_surface()
        self.background_image = pygame.image.load("./img/background.png")
        self.end_game = False

    def event_loop(self):
        for event in pygame.event.get():
            self.button_click(event)
            self.draw()
            pygame.display.flip()

            if event.type == pygame.QUIT:
                self.end_game = True
                exit()

    def run(self):
        self.draw()
        while not self.end_game:
            self.event_loop()

    def button_click(self, event):
        pass

    def draw(self):
        self.screen.blit(self.background_image, (0, 0))
