import pygame
import os
from .base_state import BaseState
import session_setup
import helpers
from button import Button

pygame.mixer.init()



class GameBoard(BaseState):
    def __init__(self):
        super(GameBoard, self).__init__()
        self.rect = pygame.Rect((0, 0), (80, 80))
        self.rect.center = self.screen_rect.center
        self.columns = None
        self.active_col = None
        self.active_box = None
        self.deactivate_boxes = []
        self.letters = None
        self.letterboxes = []
        self.word_builder = []
        self.letter = []
        self.letter_coords = []
        self.font = None
        self.text_color = None
        self.boxes = None
        # self.word_line = None
        self.colored_boxes = set()
        self.submit_button = None
        self.submit_button_ready = None
        self.submit_button_pressed = None
        self.submit_button_states = []
        self.scaled_img = None
        self.scaled_rect = None
        self.background_color = (158, 232, 212)
        self.play_button_pos = (700, 240)
        self.current_submit_button = None
        self.wrong_answer_sound = None
        self.hashable_box = ()
        self.next_state = "GAME_OVER"  # keep as last property

    # CONTINUE STARTUP TO LOAD BOARD + WORDS + CONFIRM BUTTON
    def startup(self, persistent):
        session_setup.setup_session(self.rect.center)
        self.letters = session_setup.get_letters()
        # print("self.letters after session_setup: ", self.letters)
        self.font = self.letters[0][1]
        self.text_color = self.letters[0][2]
        for item in self.letters:
            for i in range(0, len(item), 5):
                self.letter.append(item[i][0])
                self.letter_coords.append((item[i + 3], item[i + 4]))
        self.boxes = session_setup.get_boxes()
        self.columns = session_setup.get_col_boxes()
        # self.word_line = pygame.Rect(150, 195, 750, 5)
        self.submit_button_ready = pygame.image.load(os.path.join("assets", "images", "buttons",
                                                                  "resume_button_ready.png"))
        self.submit_button_pressed = pygame.image.load(os.path.join("assets", "images", "buttons",
                                                                    "resume_button_pressed.png"))
        self.submit_button_states.extend([self.submit_button_ready, self.submit_button_pressed])
        self.submit_button = Button(self.submit_button_states, 1)
        self.current_submit_button = self.submit_button_states[0]
        self.scaled_img = helpers.scale_image(self.submit_button_ready, 3)
        self.scaled_rect = self.scaled_img.get_rect()
        self.scaled_rect.topleft = self.play_button_pos
        # load sound
        self.wrong_answer_sound = pygame.mixer.Sound(os.path.join("assets", "sounds", "wrong.wav"))
        # print("scaled_rect.topleft: ", self.scaled_rect.topleft)
        # print("boxes: ", self.boxes)
        print("letter: ", self.letter)
        # print("LETTERCOORDS: ", self.letter_coords)

    def check_word(self):
        pass

    def get_event(self, event):
        letter_list = []
        if event.type == pygame.QUIT:
            self.quit = True
        if event.type == pygame.KEYUP:
            # end game
            if event.key == pygame.K_SPACE:
                self.done = True
            if self.active_col is None:
                self.active_col = 0

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:
                self.hashable_box = ()
                # get active column
                for n, col in enumerate(self.columns):
                    if col.collidepoint(event.pos):
                        self.active_col = n
                # get active box
                for box in self.boxes:
                    if box.collidepoint(event.pos):
                        self.active_box = box
                # check if word-check button clicked
                if self.scaled_rect.collidepoint(pygame.mouse.get_pos()):
                    print("Button Clicked!")

                    self.wrong_answer_sound.play()
                # add first box to colored_box list
                if self.active_box is not None:
                    print("Active box: ", self.active_box)
                    for corner in self.active_box:
                        self.hashable_box = self.hashable_box + (corner,)
                    if self.active_col is not None:
                        self.hashable_box = self.hashable_box + (self.active_col,)
                        self.colored_boxes.add(self.hashable_box)

        if event.type == pygame.MOUSEBUTTONUP:
            print("Active col: ", self.active_col, " and active box: ", self.active_box)
            print("Colored boxes ", self.colored_boxes)
            if self.active_box is not None:
                self.letterboxes.append(self.active_box)
                self.deactivate_boxes.append(self.active_box)
                if self.active_col is not None:
                    if len(self.colored_boxes) > 1:
                        for n, item in enumerate(self.colored_boxes.copy()):
                            if self.hashable_box[4] == item[4]:
                                self.colored_boxes.discard(item)
                            else:
                                self.colored_boxes.add(item)
            for letter in self.letters:
                if (letter[3], letter[4]) == (self.active_box[0], self.active_box[1]):
                    pass
            # reset active column and box
            # self.active_col = None
            # self.active_box = None

    def update(self, dt):
        pass
        # for box in self.boxes:
        #     if self.active_box is not None:
        #         self.colored_boxes.append((self.active_box, self.active_col))
        #         print("in update: ", self.colored_boxes)

        # for i, box in enumerate(self.boxes):
        #     if self.active_col is not None:
        #         if box.colliderect(self.columns[self.active_col]):
        #             self.colored_boxes.append(box)

                # if self.letter[i][3] == box.x and self.letters[i][4] == box.y:
                #     print(self.letter[i][0])
                # for letter in self.letters:
                #     if letter(self.word_line):
                #         print(letter)

    def draw(self, surface):
        surface.fill(pygame.Color(self.background_color))
        pygame.draw.rect(surface, self.background_color, self.scaled_rect)
        surface.blit(self.scaled_img, self.play_button_pos)
        for col in self.columns:
            pygame.draw.rect(surface, "BLUE", col)
        # pygame.draw.rect(surface, "GRAY", self.word_line)
        for box in self.boxes:
            pygame.draw.rect(surface, "PINK", box)
        if len(self.colored_boxes) >= 1:
            for n, box in enumerate(self.colored_boxes):
                pygame.draw.rect(surface, "LIGHTBLUE", (box[0], box[1], box[2], box[3]))
        for i, letter in enumerate(self.letters):
            helpers.draw_text(letter[0], self.font, "PURPLE", self.boxes[i][0], self.boxes[i][1],
                              surface)
        for box in self.deactivate_boxes:
            pygame.draw.rect(surface, "PURPLE", box)
            # if box.colliderect(self.word_line):
            #     print(letter)


