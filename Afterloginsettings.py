##Created by Sarah Houyoux & André Pavlov & Adrien Mourot##
########################25/05/2024#########################

import pygame
import pygame_menu
from pygame_menu import themes
from typing import Tuple, Any
import subprocess
import sys

pygame.init() #here, we define the bases characteristics of the window to launch
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('IPSA GAME PLATFORM')

def profile_button():
    subprocess.Popen([sys.executable, 'ProfileMenu.py'])
    pygame.quit()
    sys.exit()

def htp_button():
    subprocess.Popen([sys.executable, 'htpmenu.py'])
    pygame.quit()
    sys.exit()

def game_button():
    print("test game ok")

def sb_button():
    subprocess.Popen([sys.executable, 'sbmenu.py'])
    pygame.quit()
    sys.exit()

def mg_button():
    subprocess.Popen([sys.executable, 'mgmenu.py'])
    pygame.quit()
    sys.exit()

def settings_button():
    subprocess.Popen([sys.executable, 'settingsmenu.py'])
    pygame.quit()
    sys.exit()



mainmenu = pygame_menu.Menu('Menu: ', 1280, 720, theme=themes.THEME_SOLARIZED) #theses few lines set up the different things to show on the main menu
mainmenu.add.button('Profile', profile_button)
mainmenu.add.button('How to play', htp_button)
mainmenu.add.button('Game', game_button)
mainmenu.add.button('Score Board', sb_button)
mainmenu.add.button('More Games', mg_button)
mainmenu.add.button('Settings', settings_button)
mainmenu.add.text_input('',maxchar=0)
mainmenu.add.button('Quit', pygame_menu.events.EXIT) #type: ignore

mainmenu.mainloop(screen)