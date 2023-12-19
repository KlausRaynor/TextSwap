import pygame
from .base_state import BaseState


class SplashScreen(BaseState):
    def __init__(self):
        super(SplashScreen, self).__init__()
        self.title = self.title_font.render("TextSwap", True, pygame.Color("BLUE"))
        self.attribution = self.attr_font.render("A Game by Klaus Holder", True, pygame.Color("BLUE"))
        self.title_rect = self.title.get_rect(center=self.screen_rect.center)
        self.attribution_rect = self.attribution.get_rect(center=self.screen_rect.center)
        self.next_state = "MENU"
        self.time_active = 0

    def update(self, dt):
        self.time_active += dt
        if self.time_active >= 5000:
            self.done = True

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.done = True

    def draw(self, surface):
        surface.fill(pygame.Color("WHITE"))
        surface.blit(self.title, self.title_rect)
        surface.blit(self.attribution, (self.attribution_rect.x, self.attribution_rect.y + 150))

