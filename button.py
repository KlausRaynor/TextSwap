import pygame


class Button:
    def __init__(self, x, y, image, scale):
        # self.game = game
        # self.load_sprites()
        # self.position_x, self.position_y = 200, 200
        # self.current_frame, self.last_frame_update = 0,0
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (width * scale, height * scale))
        self.rect = self.image.get_rect()
        self.position_x = 0
        self.position_y = 0
        self.rect.topleft = (x, y)

    def update(self, delta_time, actions):
        pass

    def draw(self, screen):
        # draw button on screen
        return screen.blit(self.image, (self.rect.x, self.rect.y))

