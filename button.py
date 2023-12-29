import pygame


class Button:
    def __init__(self, image, scale):
        self.image = image
        width = image[0].get_width()
        height = image[0].get_height()
        for n, img in enumerate(image):
            self.image[n] = pygame.transform.scale(image[n], (width * scale, height * scale))
        self.rect = self.image[0].get_rect()

    def update(self, delta_time, actions):
        pass

    def click_event(self):
        pass