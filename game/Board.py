import pygame

import constants


class Board:
    def __init__(self, game_state=None):
        self.window = pygame.display.set_mode(constants.SCREEN_SIZE)
        pygame.display.set_caption(constants.GAME_NAME)
        self.screen = pygame.display.get_surface()
        self.background_image = pygame.image.load("./img/background.png").convert()

        self.game_state = game_state

    def draw(self):
        self.screen.blit(self.background_image, (0, 0))
        self.update()
        pygame.display.flip()

    def update(self):
        # Show dice if generated
        if self.game_state.dice:
            dice1, dice2 = self.game_state.dice.render_dice()
            self.window.blit(*dice1)
            self.window.blit(*dice2)
