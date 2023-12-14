import pygame


class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (width * scale, height * scale))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw_button(self, screen):
        # draw button on screen
        return screen.blit(self.image, (self.rect.x, self.rect.y))

