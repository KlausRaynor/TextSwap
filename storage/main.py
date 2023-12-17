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

from helpers import *
from session_setup import *


# noinspection SpellCheckingInspection
def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("TextSwap - A Game by Klaus Holder")
    clock = pygame.time.Clock()

    # Game Variables
    game_paused = False
    play_clicked = False
    # for button animation
    button_clicked = False
    show_game_screen = False
    show_start_screen = True
    show_pause_screen = False

    text_font = helpers.get_text_font()
    # for click and drag option
    active_box = None

    pause_text = "Press ESC to pause"
    resume_text = "Press ESC to resume"

    all_buttons = create_buttons()


    # END TESTING ****
# MAIN GAME LOOP
    running = True
    while running:
        screen.fill((202, 228, 241))

        if show_start_screen:
        # BUTTON ANIMATION
            play_button = []
            if button_clicked:
                for b in all_buttons:
                    if "play_button_pressed" in b[0]:
                        play_button.append(b)
                        b[1].draw_button(screen)
                play_clicked = True
            elif not button_clicked:
                for b in all_buttons:
                    if "play_button_ready" in b[0]:
                        play_button.append(b)
                        b[1].draw_button(screen)
    # PAUSE MENU
        if game_paused:
            pass
            draw_text(resume_text, text_font, "RED",
                      SCREEN_WIDTH / 2 - (SCREEN_WIDTH / 3), SCREEN_HEIGHT / 2, screen)
        else:
            draw_text(pause_text, text_font, "BLACK",
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
                if event.key == pygame.K_ESCAPE:
                    if game_paused:
                        game_paused = False
                        show_start_screen = False
                    else:
                        game_paused = True
                        show_start_screen = True
            # click and drag event. Check for MOUSEBUTTONDOWN and MOUSEBUTTONUP event.button == 1
            if event.type == pygame.MOUSEBUTTONDOWN:

                # LEFT CLICK
                if event.button == 1:
                    if all_buttons[1][1].rect.collidepoint(event.pos):
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
