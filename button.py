from pygame import display
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    # def draw(self):
    #     # draw button on screen
    #     screen.blit(self.image, (self.rect.x, self.rect.y))