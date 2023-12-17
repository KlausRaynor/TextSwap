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


import sys
import pygame
from states.game_board import GameBoard
from states.title_menu import Menu
from states.splash_screen import SplashScreen
from states.game_over import GameOver
from game import Game

pygame.init()
screen = pygame.display.set_mode((960, 540))
states = {
    "MENU": Menu(),
    "SPLASH": SplashScreen(),
    "GAME_BOARD": GameBoard(),
    "GAME_OVER": GameOver()
}

game = Game(screen, states, "SPLASH")
game.run()

pygame.quit()
sys.exit()