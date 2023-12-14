import pygame


def draw_text(text, font, text_col, tx, ty, screen):
    img = font.render(text, True, text_col)
    screen.blit(img, (tx, ty))


def get_text_font():
    return pygame.font.Font("Fonts/baveuse.ttf", 30)
