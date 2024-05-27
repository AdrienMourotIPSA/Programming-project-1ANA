##Created by Adrien Mourot##
#########25/05/2024#########

import pygame
import pygame_menu
from pygame_menu import themes
from typing import Tuple, Any

pygame.init() #here, we define the bases characteristics of the window to launch
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('IPSA GAME PLATFORM')

def profile_button():
    import ProfileMenu

def htp_button():
    import htpmenu

def game_button():
    print("test game ok")

def sb_button():
    print("test sb ok")

def mg_button():
    print("test mg ok")

def settings_button():
    print("test settings ok")



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