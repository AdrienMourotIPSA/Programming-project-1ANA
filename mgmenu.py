## Created by Sarah Houyoux & André Pavlov & Adrien Mourot ##
##########################30/05/2024#########################

import pygame
import pygame_menu
from typing import Tuple, Any
import pygame_menu.themes
import subprocess
import sys

pygame.init() #here, we define the bases characteristics of the window to launch
screen = pygame.display.set_mode((1280 , 720))
pygame.display.set_caption('More Games Menu')

def Return_button():
    subprocess.Popen([sys.executable, 'Afterloginsettings.py'])
    pygame.quit()
    sys.exit()

def start_snake_game():
    show_message('Starting Snake game...', Return_button)
 
def start_table_tennis_game():
    show_message('Starting Table Tennis game...', Return_button)
 
def start_starfield_game():
    show_message('Starting Starfield game...', Return_button)

def show_message(message, callback=None):
    msg_menu = pygame_menu.Menu('', 600, 400, theme=pygame_menu.themes.THEME_DARK)
    msg_menu.add.label(message)
    msg_menu.add.button('Back', callback or pygame_menu.events.BACK) #type:ignore
    msg_menu.mainloop(screen)

more_games_menu = pygame_menu.Menu('More Games', 1280, 720, theme=pygame_menu.themes.THEME_SOLARIZED)
more_games_menu.add.button('Snake', start_snake_game)
more_games_menu.add.button('Table Tennis', start_table_tennis_game)
more_games_menu.add.button('Starfield', start_starfield_game)
more_games_menu.add.button('Return', )
more_games_menu.mainloop(screen)
 
# Placeholder functions for additional games
