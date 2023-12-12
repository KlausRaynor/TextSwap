import pygame
from pygame.locals import *
import generate_words
import random

# noinspection SpellCheckingInspection
def main():
    pygame.init()
    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 480

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
    letters_set = generate_words.group_letters(word_list)
    active_box = None
    boxes = []
    box_x = 100
    box_y = 100
    # **TODO** change this to be ordered based on letter group sets
    # TODO change to match # of letters from group_letters
    i = 0
    for i in range(len(letters_set[i]) - 1):
        for j in range(len(letters_set) - 1):
            box = pygame.Rect(box_x, box_y, 50, 50)
            boxes.append(box)
            box_y += 51
        box_x += 51
        box_y = 100
        i += 1
    print("Boxes: ", boxes)
    print("Length boxes: ", len(boxes))
# MAIN GAME LOOP
    run = True
    while run:

        screen.fill("BLACK")

        for i in range(len(letters_set)):
            for num, letter in enumerate(letters_set[i]):
                pygame.draw.rect(screen, "BLUE", boxes[i])
                draw_text(letter, text_font, "YELLOW", boxes[num].x, boxes[num].y)

    # EVENTS (CLICK N DRAG)--v
        for event in pygame.event.get():
            # click and drag event. Check for MOUSEBUTTONDOWN and MOUSEBUTTONUP event.button == 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for num, box in enumerate(boxes):
                        if box.collidepoint(event.pos):
                            active_box = num
            if event.type == pygame.MOUSEMOTION:
                if active_box != None:
                    boxes[active_box].move_ip(event.rel)

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    active_box = None
            # QUIT GAME
            if event.type == pygame.QUIT:
                run = False

        pygame.display.flip()


if __name__ == "__main__":
    main()
