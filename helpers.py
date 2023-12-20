from button import *
import os


def draw_text(text, font, text_col, tx, ty, screen):
    img = font.render(text, True, text_col)
    screen.blit(img, (tx, ty))


def get_text_font():
    pygame.font.init()
    font = pygame.font.Font(os.path.join("assets", "fonts", "baveuse.ttf"), 30)
    return font


def button_animation(b_list):
    for b in b_list:
        b.draw_button()


def scale_image(image, scale):
    scaled_img = pygame.transform.scale(image, (image.get_width() * scale, image.get_height() * scale))
    return scaled_img
