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

import generate_words
from button import *
from helpers import *
from session_setup import *


# noinspection SpellCheckingInspection
def main():
    pygame.init()
    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 480
    SCALE = 3

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("TextSwap - A Game by Klaus Holder")
    clock = pygame.time.Clock()

    # Game Variables
    game_paused = False
    play_clicked = False

    button_list = []
    # load in button images
    play_ready_img = pygame.image.load('images/play_button_ready.png').convert_alpha()
    play_pressed_img = pygame.image.load('images/play_button_pressed.png').convert_alpha()

    text_font = helpers.get_font()
    # for click and drag option
    active_box = None

    pause_text = "Press SPACE to pause"
    resume_text = "Press SPACE to resume"

# create buttons
    play_button = Button((SCREEN_WIDTH / 2) - ((play_ready_img.get_width() * SCALE) / 2), (SCREEN_HEIGHT / 4), play_ready_img,
                         SCALE)
    play_button_pressed = Button((SCREEN_WIDTH / 2) - ((play_pressed_img.get_width() * SCALE) / 2), (SCREEN_HEIGHT / 4),
                                 play_pressed_img, SCALE)

    button_clicked = False

    button_list.append(play_button)
    button_list.append(play_button_pressed)

    # END TESTING ****
# MAIN GAME LOOP
    running = True
    while running:
        screen.fill((202, 228, 241))

        if button_clicked:
            play_button_pressed.draw_button(screen)
        elif not button_clicked:
            play_button.draw_button(screen)
    # PAUSE MENU
        if game_paused:
            pass
            draw_text(resume_text, text_font, "RED",
                      SCREEN_WIDTH / 2 - (SCREEN_WIDTH / 3), SCREEN_HEIGHT / 2, screen)
        else:
            draw_text(pause_text, text_font, "GREEN",
                      SCREEN_WIDTH / 2 - (SCREEN_WIDTH / 3), SCREEN_HEIGHT / 2, screen)
    # GAME MENU
        if play_clicked:
            start_main_game(screen)
        else:
            pass
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
                running = False
        # refresh screen
        pygame.display.flip()

        clock.tick(60)  # FPS


if __name__ == "__main__":
    main()
