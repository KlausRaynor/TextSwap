import pygame
from .base_state import BaseState
from button import Button

class Menu(BaseState):
    def __init__(self):
        super(Menu, self).__init__()
        self.active_index = 0
        self.options = ["Start Game", "Quit Game"]
        self.next_state = "GAME_BOARD"

    def create_button(self, button):
        pass

    def draw_text(self, index):
        color = pygame.Color("PURPLE") if index == self.active_index else pygame.Color("BLUE")
        return self.font.render(self.options[index], True, color)

    def get_text_pos(self, text, index):
        center = (self.screen_rect.center[0], self.screen_rect.center[1] + (index * 50))
        return text.get_rect(center=center)

    def action_handler(self):
        if self.active_index == 0:
            self.done = True
        elif self.active_index == 1:
            self.quit = True

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.active_index = 1 if self.active_index <= 0 else 0
            elif event.key == pygame.K_DOWN:
                self.active_index = 0 if self.active_index >= 1 else 1
            elif event.key == pygame.K_RETURN:
                self.action_handler()


    def draw(self, surface):
        surface.fill(pygame.Color("WHITE"))
        for n, option in enumerate(self.options):
            text_render = self.draw_text(n)
            surface.blit(text_render, self.get_text_pos(text_render, n))


#
# class Title(State):
#     def __init__(self, game):
#         State.__init__(self, game)
#         self.start_img = pygame.image.load(os.path.join(self.game.buttons_dir, "play_button_ready.png"))
#         self.start_img_pressed = pygame.image.load(os.path.join(self.game.buttons_dir, "play_button_pressed.png"))
#         self.start_rect = self.start_img.get_rect()
#         self.start_rect.centerx = self.game.GAME_W * .5
#         self.start_rect.centery = self.game.GAME_H * .5
#         # self.start_rect.center = ((self.game.GAME_W * .5) - (self.start_rect.x / 2), self.game.GAME_H * .4)
#
#     def update(self, delta_time, actions):
#         if actions["play"]:
#             new_state = GameBoard(self.game)
#             new_state.enter_state()
#         self.game.reset_keys()
#
#     def render(self, display):
#         display.fill((255, 255, 255))
#         self.game.draw_text(display, "TextSwap", (0, 0, 0), self.game.GAME_W/2, self.game.GAME_H / 4)
#
#         display.blit(self.start_img, self.start_rect)
#
