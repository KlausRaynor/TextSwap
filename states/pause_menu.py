# import pygame, os
# from .base_state import BaseState
#
#
# class PauseMenu(BaseState):
#     def __init__(self, game):
#         self.game = game
#         State.__init__(self, game)
#         self.pause_img = pygame.image.load(os.path.join(self.game.buttons_dir, "play_button_ready.png"))
#         self.pause_rect = self.pause_img.get_rect()
#         self.pause_rect.center = (self.game.GAME_W * .85, self.game.GAME_H * .4)
#
#     def update(self, delta_time, actions):
#         if actions["resume"]:
#             self.exit_state()
#         self.game.reset_keys()
#
#     def render(self, display):
#         self.prev_state.render(display)
#         display.blit(self.pause_img, self.pause_rect)