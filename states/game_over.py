import pygame
import os
from .base_state import BaseState
from button import Button


class GameOver(BaseState):
    def __init__(self):
        super(GameOver, self).__init__()
        self.title = self.title_font.render("Game Over", True, pygame.Color("BLACK"))
        self.title_rect = self.title.get_rect(center=(self.screen_rect.centerx, (self.screen_rect.centery / 2)
                                                      - 50))
        self.instructions = self.attr_font.render("Press space to start again, or enter to go to the menu", True,
                                                  pygame.Color("BLUE"))
        instructions_center = (self.screen_rect.center[0], self.screen_rect.center[1] + 200)
        self.instructions_rect = self.instructions.get_rect(center=instructions_center)
        self.button_scale = 2
        # Restart button
        self.restart_button_states = []
        self.restart_button_ready = pygame.image.load(os.path.join("assets", "images", "buttons", 
                                                                   "restart_button_ready.png"))
        self.restart_button_pressed = pygame.image.load(os.path.join("assets", "images", "buttons",
                                                                     "restart_button_pressed.png"))
        self.restart_button_states.append(self.restart_button_ready)
        self.restart_button_states.append(self.restart_button_pressed)
        self.restart_button = Button(self.restart_button_states, self.button_scale * 1.5)
        self.restart_button.rect.center = self.screen_rect.center

        self.current_restart_button = self.restart_button_states[0]

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN:
                self.next_state = "MENU"
                self.done = True
            elif event.key == pygame.K_SPACE:
                self.next_state = "GAME_BOARD"
                self.done = True
            elif event.key == pygame.K_ESCAPE:
                self.quit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.restart_button.rect.collidepoint(pygame.mouse.get_pos()):
                    self.current_restart_button = self.restart_button_states[1]

    def draw(self, surface):
        surface.fill(pygame.Color(205, 134, 87))
        surface.blit(self.title, self.title_rect)
        surface.blit(self.instructions, self.instructions_rect)

        surface.blit(self.current_restart_button, self.restart_button)