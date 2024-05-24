##Created by Adrien Mourot##
#########23/05/2024#########

import pygame
import pygame_menu
from pygame_menu import themes
from typing import Tuple, Any

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('IPSA GAME PLATFORM')

def signup_button():
    c = courriel.get_value()
    m = mdp.get_value()
    file = open('File_username.csv', 'r')
    lines = file.readlines()
    flag=0
    for line in lines:
        line = line.strip()
        l = line.split(',')
        if l[0] == c and l[1] == m:
            colour1 = (200, 0, 0)
            fontObj = pygame.font.Font('freesansbold.ttf', 15)  
            text = fontObj.render("Already signed up email!", True, colour1)
            screen.blit(text, (550,380))
            pygame.display.update()
            pygame.time.delay(2000)
            flag=1
    if flag==0:
        if len(m)>6:
            file=open("File_username.csv", "a")
            file.write(f"\n{c},{m}")
            colour1 = (200, 0, 0)
            fontObj = pygame.font.Font('freesansbold.ttf', 15)  
            text = fontObj.render("New user is registered!", True, colour1)
            screen.blit(text, (560,380))
            pygame.display.update()
            pygame.time.delay(2000)
        elif len(m)<6:
            colour1 = (200, 0, 0)
            fontObj = pygame.font.Font('freesansbold.ttf', 15)  
            text = fontObj.render("The password is too short (min 6 characters)", True, colour1)
            screen.blit(text, (475,380))
            pygame.display.update()
            pygame.time.delay(2000)


difficulty = 1
def set_difficulty(set_difficulty: Tuple, value: Any) -> None:
    global difficulty
    difficulty = str(value)
    print(difficulty)
    
 
def start_the_game():
    print(difficulty)


def login_function():
    print(courriel.get_value())
         
level = pygame_menu.Menu('Select a Difficulty', 400, 400, theme=themes.THEME_SOLARIZED)
level.add.selector('levels :', [('level1', 1), ('level2', 2)], onchange=set_difficulty)

mainmenu = pygame_menu.Menu('Welcome to main menu!', 1280, 720, theme=themes.THEME_SOLARIZED)
courriel = mainmenu.add.text_input('Email: ', default='Email', maxchar=20)
mdp = mainmenu.add.text_input('Password: ', default='Password', maxchar=20)
mainmenu.add.button('Sign up', signup_button)
mainmenu.add.text_input('',maxchar=0)
mainmenu.add.text_input('Email: ', default='Email', maxchar=20)
mainmenu.add.text_input('Password: ',default='Password', maxchar=20)
mainmenu.add.button('Log in', login_function)
 
mainmenu.mainloop(screen)
