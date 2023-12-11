import pygame
from pygame.locals import *
from generate_words import *
import random


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
    word_list = get_keywords()
    # break apart words into letters
    letters = get_letters(word_list)
    group_letters(word_list)
    active_box = None
    boxes = []
    # Generate Boxes
    for i in range(len(letters)):
        x = random.randint(50, SCREEN_WIDTH - 50)
        y = random.randint(50, SCREEN_HEIGHT - 50)
        box = pygame.Rect(x, y, 50, 50)
        boxes.append(box)
# MAIN GAME LOOP
    run = True
    while run:

        screen.fill("BLACK")

        # draw boxes to screen
        for num, letter in enumerate(letters):
            pygame.draw.rect(screen, "BLUE", boxes[num])
            draw_text(letter, text_font, "YELLOW", boxes[num].x, boxes[num].y)
    # EVENTS
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
