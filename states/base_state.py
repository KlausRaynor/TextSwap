"""
Abstract State class to scaffold other states
"""

import pygame
import os


class BaseState(object):
    def __init__(self):
        self.done = False
        self.quit = False
        self.next_state = None
        self.screen_rect = pygame.display.get_surface().get_rect()
        self.persist = {}
        self.title_font = pygame.font.Font(os.path.join("assets", "fonts", "FFFFORWA.TTF"), 50)
        self.attr_font = pygame.font.Font(os.path.join("assets", "fonts", "FFFFORWA.TTF"), 25)

    def startup(self, persistent):
        self.persist = persistent

    def get_event(self, event):
        pass

    def update(self, dt):
        pass

    def draw(self, surface):
        pass
