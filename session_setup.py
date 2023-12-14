import generate_words
import helpers
from button import *
import os
pygame.font.init()

col_boxes = []
boxes = []
letter_list = []
font = helpers.get_text_font()
button_list = []
BOX_WIDTH = 50
BOX_HEIGHT = 50
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

SCALE = 3


def setup_session():

    box_x = 100
    box_y = 100
    # get words for game from generate_words.py
    word_list = generate_words.get_keywords()
    print("Word list: ", word_list)

    # group letters into dictionary of sets
    letters_set = generate_words.create_sets(word_list)

    # create box list based on # of items in letter_set
    for i in letters_set:
        col_size = 0
        for _ in letters_set[i]:
            box = pygame.Rect(box_x, box_y, BOX_WIDTH, BOX_HEIGHT)
            boxes.append(box)
            box_y += 51
            col_size += 1
        box_x += 51
        box_y = 100
        print("Column Size: ", col_size)
        # adjust/shift X one column to left by subtracting BOX_WIDTH
        col_box = pygame.Rect(box_x - BOX_WIDTH, box_y, BOX_WIDTH, BOX_HEIGHT * col_size)
        col_boxes.append(col_box)

    # move Letters_set to a list
    for i in letters_set:
        for letter in letters_set[i]:
            letter_list.append(letter)


def start_main_game(screen):
    # this needs to be repeated in MAIN
    for col in col_boxes:
        pygame.draw.rect(screen, "RED", col)
    # draw boxes and letters to screen
    for num, box in enumerate(boxes):
        pygame.draw.rect(screen, "BLUE", boxes[num])
        helpers.draw_text(letter_list[num], font, "YELLOW", boxes[num].x, boxes[num].y, screen)


def create_buttons():
    # get all images from folder
    image_list = []
    # button directory
    img_dir = 'assets/images/buttons/'
    images = os.listdir(img_dir)
    # load in button images
    button_dir = []
    for button in images:
        button_dir = [button, img_dir + button]
        image_list.append(pygame.image.load(button_dir[1]).convert_alpha())
    # create buttons and set position
    # currently all buttons in same pos.
    for n, img in enumerate(image_list):
        button_list.append([images[n],Button((SCREEN_WIDTH / 2) - ((img.get_width() * SCALE) / 2), (SCREEN_HEIGHT / 4),
                                  img, SCALE)])
    return button_list
