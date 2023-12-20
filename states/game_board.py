import pygame
import os
from .base_state import BaseState
import session_setup
import helpers
from button import Button


class GameBoard(BaseState):
    def __init__(self):
        super(GameBoard, self).__init__()
        self.rect = pygame.Rect((0,0), (80,80))
        self.rect.center = self.screen_rect.center
        self.next_state = "GAME_OVER"
        self.columns = session_setup.get_col_boxes()
        self.active_col = None
        self.letters = None
        self.letter = []
        self.letter_coords = []
        self.font = None
        self.text_color = None
        self.boxes = None
        self.word_line = None
        self.colored_boxes = []
        self.submit_button = None
        self.submit_button_ready = None
        self.submit_button_pressed = None
        self.submit_button_states = []
        self.scaled_img = None

    # CONTINUE STARTUP TO LOAD BOARD + WORDS
    def startup(self, persistent):
        session_setup.setup_session(self.rect.center)
        self.letters = session_setup.get_letters()
        self.font = self.letters[0][1]
        self.text_color = self.letters[0][2]
        for item in self.letters:
            for i in range(0, len(item), 5):
                self.letter.append(item[i][0])
                self.letter_coords.append((item[i + 3], item[i + 4]))
        self.boxes = session_setup.get_boxes()
        self.word_line = pygame.Rect(150, 195, 750, 5)
        self.submit_button_ready = pygame.image.load(os.path.join("assets", "images", "buttons",
                                                                  "resume_button_ready.png"))
        self.submit_button_pressed = pygame.image.load(os.path.join("assets", "images", "buttons",
                                                                    "resume_button_pressed.png"))
        self.submit_button_states.extend([self.submit_button_ready, self.submit_button_pressed])
        self.submit_button = Button(self.submit_button_states, 2)
        self.submit_button.rect.center = (self.screen_rect.center[0], 240)
        self.scaled_image = helpers.scale_image(self.submit_button_ready, 2)
        self.scaled_rect = self.scaled_image.get_rect()
        self.scaled_rect.topleft = (150, 195)
        print("boxes: ", self.boxes)
        print("self.letters: ", self.letters)
        print("LETTERCOORDS: ", self.letter_coords)


    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for n, col in enumerate(self.columns):
                    if col.collidepoint(event.pos):
                        self.active_col = n
                if self.scaled_rect.collidepoint(event.pos):
                    print("Button Clicked!")
        if event.type == pygame.MOUSEBUTTONUP:
            self.active_col = None
        if event.type == pygame.MOUSEMOTION:
            if self.active_col is not None:
                _, y = event.rel
                self.columns[self.active_col].move_ip(0, y)
                for box in self.boxes:
                    if box.colliderect(self.columns[self.active_col]):
                        box.move_ip(0, y)

    def update(self, dt):

        for i, box in enumerate(self.boxes):
            if box.colliderect(self.word_line):
                self.colored_boxes.append(box)

    def draw(self, surface):
        surface.fill(pygame.Color(158, 232, 212))
        surface.blit(self.scaled_image, (700, 240))
        for col in self.columns:
            pygame.draw.rect(surface, "BLUE", col)
        pygame.draw.rect(surface, "GRAY", self.word_line)
        for box in self.boxes:
            pygame.draw.rect(surface, "PINK", box)
        for box in self.colored_boxes:
            if box.colliderect(self.word_line):
                pygame.draw.rect(surface, "LIGHTBLUE", box)
        for i, letter in enumerate(self.letters):
            helpers.draw_text(letter[0], self.font, "PURPLE", self.boxes[i][0], self.boxes[i][1],
                              surface)

