import pygame
import os
from .base_state import BaseState
from button import Button


class Menu(BaseState):
    def __init__(self):
        super(Menu, self).__init__()
        # self.active_index = 0
        self.scale = 3
        self.options = ["Start Game", "Quit Game"]
        self.next_state = "GAME_BOARD"
        self.title = self.title_font.render("TextSwap", True, pygame.Color("WHITE"))
        self.title_rect = self.title.get_rect(center=(self.screen_rect.centerx, self.screen_rect.centery -
                                                      self.screen_rect.centery / 2))
        # play button
        self.play_button_states = []
        self.play_button_ready = pygame.image.load(os.path.join("assets", "images", "buttons", "play_button_ready.png"))
        self.play_button_pressed = pygame.image.load(os.path.join("assets", "images", "buttons",
                                                                  "play_button_pressed.png"))
        self.play_button_states.append(self.play_button_ready)
        self.play_button_states.append(self.play_button_pressed)
        self.play_button = Button(self.play_button_states, self.scale * 1.5)
        self.play_button.rect.center = self.screen_rect.center

        # quit button
        self.quit_button_states = []
        self.quit_button_ready = pygame.image.load(os.path.join("assets", "images", "buttons", "quit_button_ready.png"))
        self.quit_button_pressed = pygame.image.load(os.path.join("assets", "images", "buttons",
                                                                  "quit_button_pressed.png"))
        self.quit_button_states.append(self.quit_button_ready)
        self.quit_button_states.append(self.quit_button_pressed)
        self.quit_button = Button(self.quit_button_states, self.scale)
        self.quit_button.rect.center = (self.screen_rect.centerx, self.screen_rect.centery +
                                        self.screen_rect.centery / 2)

        # button that is currently displayed
        self.current_play_button = self.play_button_states[0]
        self.current_quit_button = self.quit_button_states[0]

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.play_button.rect.collidepoint(pygame.mouse.get_pos()):
                    self.current_play_button = self.play_button_states[1]
                if self.quit_button.rect.collidepoint(pygame.mouse.get_pos()):
                    self.current_quit_button = self.quit_button_states[1]
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and self.play_button.rect.collidepoint(pygame.mouse.get_pos()):
                self.current_play_button = self.play_button_states[0]
                self.done = True
            elif event.button == 1 and not self.play_button.rect.collidepoint(pygame.mouse.get_pos()):
                self.current_play_button = self.play_button_states[0]
            if event.button == 1 and self.quit_button.rect.collidepoint(pygame.mouse.get_pos()):
                self.current_quit_button = self.quit_button_states[0]
                self.quit = True
            elif event.button == 1 and not self.quit_button.rect.collidepoint(pygame.mouse.get_pos()):
                self.current_quit_button = self.quit_button_states[0]
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.current_play_button = self.play_button_states[1]
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN:
                self.current_play_button = self.play_button_states[0]
                self.done = True

    def draw(self, surface):
        surface.fill(pygame.Color(50, 121, 168))
        surface.blit(self.current_play_button,  self.play_button)
        surface.blit(self.current_quit_button, self.quit_button)
        surface.blit(self.title, self.title_rect)
