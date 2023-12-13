"""
Author: Klaus Holder
Date: 12/11/23
Clone of the text game TypeShift by Zach Gage
Written in PyGame for CS50 final project
Dictionary lists courtesy of MIT and UMichigan
Dictionary API used: https://dictionaryapi.dev/
PyGame: https://www.pygame.org/docs/
TypeShift: http://www.playtypeshift.com/
"""

import pygame
import generate_words
from button import *


# noinspection SpellCheckingInspection
def main():
    pygame.init()
    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 480
    BOX_WIDTH = 50
    BOX_HEIGHT = 50
    SCALE = 3

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("TextSwap - A Game by Klaus Holder")
    clock = pygame.time.Clock()

    # Game Variables
    game_paused = False

    button_list = []
    # load in button images
    play_ready_img = pygame.image.load('images/play_button_ready.png').convert_alpha()
    play_pressed_img = pygame.image.load('images/play_button_pressed.png').convert_alpha()

    # scale images
    scaled_play_rdy_img = pygame.transform.scale(
        play_ready_img, (play_ready_img.get_width() * 2, play_ready_img.get_height() * SCALE))
    scaled_play_pressed_img = pygame.transform.scale(
        play_pressed_img, (play_pressed_img.get_width() * 2, play_ready_img.get_height() * SCALE))


    # define font
    text_font = pygame.font.Font("Fonts/baveuse.ttf", 30)

    def draw_text(text, font, text_col, tx, ty):
        img = font.render(text, True, text_col)
        screen.blit(img, (tx, ty))

    def draw_button(b):
        screen.blit(b.image, (b.rect.x, b.rect.y))
    # get words for game from generate_words.py
    word_list = generate_words.get_keywords()
    print("Word list: ", word_list)

    # group letters into dictionary of sets
    letters_set = generate_words.create_sets(word_list)

    boxes = []
    box_x = 100
    box_y = 100

    col_boxes = []

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

    print("Length boxes: ", len(boxes))
    print("length letters_set: ", len(letters_set))
    print("Letters set: ", letters_set)
    # for click and drag option
    active_box = None

    # move Letters_set to a list
    letter_list = []
    for i in letters_set:
        for letter in letters_set[i]:
            letter_list.append(letter)

    pause_text = "Press SPACE to pause"
    resume_text = "Press SPACE to resume"

    play_button = Button((SCREEN_WIDTH / 2) - (scaled_play_rdy_img.get_width() / 2), (
            SCREEN_HEIGHT / 4), scaled_play_rdy_img)
    play_button_pressed = Button((SCREEN_WIDTH / 2) - (scaled_play_rdy_img.get_width() / 2),
            (SCREEN_HEIGHT / 4), scaled_play_pressed_img)
    button_clicked = False

    button_list.append(play_button)
    button_list.append(play_button_pressed)

    # END TESTING ****
# MAIN GAME LOOP
    run = True
    while run:
        screen.fill((202, 228, 241))
        if button_clicked:
            draw_button(button_list[1])
        elif not button_clicked:
            draw_button(button_list[0])

        if game_paused == True:
            pass
            draw_text(resume_text, text_font, "RED", (SCREEN_WIDTH)/2 - (SCREEN_WIDTH / 3), SCREEN_HEIGHT / 2)
        else:
            draw_text(pause_text, text_font, "GREEN", (SCREEN_WIDTH)/2 - (SCREEN_WIDTH / 3), SCREEN_HEIGHT / 2)
        # draw columns
        # for col in col_boxes:
        #     pygame.draw.rect(screen, "RED", col)
        # # draw boxes and letters to screen
        # for num, box in enumerate(boxes):
        #     pygame.draw.rect(screen, "BLUE", boxes[num])
        #     draw_text(letter_list[num], text_font, "YELLOW", boxes[num].x, boxes[num].y)
    # UNCOMMENT ABOVE ONCE PAUSE TESTING COMPLETE

    # EVENTS (CLICK N DRAG)--v
        for event in pygame.event.get():

            # KEY DOWN
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if game_paused:
                        game_paused = False
                    else:
                        game_paused = True
            # click and drag event. Check for MOUSEBUTTONDOWN and MOUSEBUTTONUP event.button == 1
            if event.type == pygame.MOUSEBUTTONDOWN:

                # LEFT CLICK
                if event.button == 1:
                    if play_button.rect.collidepoint(event.pos):
                        button_clicked = True
                    # for num, box in enumerate(boxes):
                    #     if box.collidepoint(event.pos):
                    #         active_box = num
                    for num, col_box in enumerate(col_boxes):
                        if col_box.collidepoint(event.pos):
                            active_box = num
        # MOUSE MOVEMENT
            if event.type == pygame.MOUSEMOTION:
                if active_box is not None:
                    _, y = event.rel
                    # boxes[active_box].move_ip(0, y)
                    col_boxes[active_box].move_ip(0, y)
        # RELEASE MOUSE BUTTON
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    active_box = None
                    button_clicked = False
        # QUIT GAME
            if event.type == pygame.QUIT:
                run = False
        # refresh screen
        pygame.display.flip()

        clock.tick(60)  # FPS


if __name__ == "__main__":
    main()
