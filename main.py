"""
Author: Klaus Holder
Date: 12/11/23
Clone of the text game TypeShift by Zach Gage
Written in PyGame for CS50 final project

PyGame: https://www.pygame.org/docs/
TypeShift: http://www.playtypeshift.com/
"""

import pygame
import generate_words
import random


# noinspection SpellCheckingInspection
def main():
    pygame.init()
    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 480
    BOX_WIDTH = 50
    BOX_HEIGHT = 50

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("TextSwap - A Game by Klaus Holder")
    clock = pygame.time.Clock()

    text_font = pygame.font.Font("Fonts/baveuse.ttf", 50)

    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    # get words for game from generate_words.py
    word_list = generate_words.get_keywords()
    print("Word list: ", word_list)
    # break apart words into letters
    letters = generate_words.get_letters(word_list)
    # group letters into dictionary of sets
    letters_set = generate_words.group_letters(word_list)

    boxes = []
    box_x = 100
    box_y = 100
    i = 0
    for i in letters_set:
        for _ in letters_set[i]:
            box = pygame.Rect(box_x, box_y, BOX_WIDTH, BOX_HEIGHT)
            boxes.append(box)
            box_y += 51
        box_x += 51
        box_y = 100

    print("Boxes: ", boxes)
    print("Length boxes: ", len(boxes))
    print("length letters_set: ", len(letters_set))
    print("Letters set: ", letters_set)
    # for click and drag option
    active_box = None

    # TESTING ***
    # move Letters_set to a list
    letter_list = []
    for i in letters_set:
        for letter in letters_set[i]:
            letter_list.append(letter)
    # END TESTING ****

# MAIN GAME LOOP
    run = True
    while run:
        screen.fill("BLACK")
        for num, box in enumerate(boxes):
            pygame.draw.rect(screen, "BLUE", boxes[num])

        for num, letter in enumerate(letter_list):
            draw_text(letter, text_font, "YELLOW", boxes[num].x, boxes[num].y)

    # EVENTS (CLICK N DRAG)--v
        for event in pygame.event.get():
            # click and drag event. Check for MOUSEBUTTONDOWN and MOUSEBUTTONUP event.button == 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                # LEFT CLICK
                if event.button == 1:
                    for num, box in enumerate(boxes):
                        if box.collidepoint(event.pos):
                            active_box = num
        # MOUSE MOVEMENT
            if event.type == pygame.MOUSEMOTION:
                if active_box is not None:
                    _, y = event.rel
                    boxes[active_box].move_ip(0, y)
        # RELEASE MOUSE BUTTON
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    active_box = None
        # QUIT GAME
            if event.type == pygame.QUIT:
                run = False
        # refresh screen
        pygame.display.flip()

        clock.tick(60)  # FPS


if __name__ == "__main__":
    main()
