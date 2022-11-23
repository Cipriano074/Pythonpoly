import pygame

import constants


class Button(pygame.sprite.Sprite):
    def __init__(self, image_path, clicked_image_path, initial_pos=None):
        super().__init__()
        self._img_path = image_path
        self._clicked_img_path = clicked_image_path
        self.image = self.load_image(self._img_path)
        self.rect = self.image.get_rect()
        if initial_pos is not None:
            self.initial_pos = initial_pos
            self.set_pos(initial_pos[0], initial_pos[1])
        else:
            self.initial_pos = (0, 0)

    @staticmethod
    def load_image(path=""):
        return pygame.image.load(constants.get_path(path))

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def clicked(self, event_x, event_y):
        return self.rect.collidepoint(event_x, event_y)

    def redraw_clicked(self):
        self.image = self.load_image(self._clicked_img_path)
        self.rect = self.image.get_rect()
        x, y = self.initial_pos
        self.set_pos(x - 5, y - 5)

    def redraw_not_clicked(self):
        self.image = self.load_image(self._img_path)
        self.rect = self.image.get_rect()
        x, y = self.initial_pos
        self.set_pos(x, y)


class ButtonRollDice(Button):

    def __init__(self):
        super().__init__("img/button_roll_dice.png", "img/button_roll_dice_light.png",
                        constants.BUTTON_ROLL_DICE_POSITION)


class ButtonEndRound(Button):
    def __init__(self):
        super().__init__("img/button_end_round.png", "img/button_end_round.png",
                        constants.BUTTON_END_ROUND_POSITION)
