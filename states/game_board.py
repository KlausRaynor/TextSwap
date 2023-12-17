import pygame
from .base_state import BaseState
import session_setup


class GameBoard(BaseState):
    def __init__(self):
        super(GameBoard, self).__init__()
        self.rect = pygame.Rect((0,0), (80,80))
        self.rect.center = self.screen_rect.center
        self.next_state = "GAME_OVER"

    # CONTINUE STARTUP TO LOAD BOARD + WORDS
    def startup(self, persistent):
        session_setup.setup_session()

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.rect.move_ip(0, -10)
            if event.key == pygame.K_DOWN:
                self.rect.move_ip(0, 10)
            if event.key == pygame.K_LEFT:
                self.rect.move_ip(-10, 0)
            if event.key == pygame.K_RIGHT:
                self.rect.move_ip(10, 0)
            if event.key == pygame.K_SPACE:
                self.done = True

    def draw(self, surface):
        surface.fill(pygame.Color("WHITE"))
        pygame.draw.rect(surface, pygame.Color("BLUE"), self.rect)
        session_setup.start_main_game(surface)


    #     self.play_button = pygame.image.load(os.path.join(self.game.buttons_dir, "quit_button.png"))
    #
    #
    # def update(self, delta_time, actions):
    #     if actions["play"]:
    #         new_state = PauseMenu(self.game)
    #         new_state.enter_state()
    #
    # def render(self, display):
    #     display.blit(self.play_button, (0, 0))
    #
    # def animate(self, delta_time):
    #     pass
