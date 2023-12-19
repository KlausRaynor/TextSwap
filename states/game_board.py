import pygame
from .base_state import BaseState
import session_setup


class GameBoard(BaseState):
    def __init__(self):
        super(GameBoard, self).__init__()
        self.rect = pygame.Rect((0,0), (80,80))
        self.rect.center = self.screen_rect.center
        self.next_state = "GAME_OVER"
        self.columns = session_setup.get_col_boxes()

    # CONTINUE STARTUP TO LOAD BOARD + WORDS

    def startup(self, persistent):
        session_setup.setup_session(self.rect.center)

    def get_event(self, event):
        active_col = None
        if event.type == pygame.QUIT:
            self.quit = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for n, col in enumerate(self.columns):
                    if col.collidepoint(event.pos):
                        print("Column ", n, " clicked.")
                        active_col = n
                        print("active_col: ", active_col)
        if event.type == pygame.MOUSEMOTION:
            if active_col is not None:
                _, y = event.rel
                self.columns[active_col].move_ip(0, y)

    def update(self, dt):
        pass

    def draw(self, surface):
        surface.fill(pygame.Color("WHITE"))
        pygame.draw.rect(surface, pygame.Color("BLUE"), self.rect)
        for col in self.columns:
            pygame.draw.rect(surface, "GREEN", col)

        # session_setup.start_main_game(surface)


