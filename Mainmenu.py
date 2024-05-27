##Created by Adrien Mourot##
#########24/05/2024#########

import pygame
import pygame_menu
from pygame_menu import themes
from typing import Tuple, Any

pygame.init() #here, we define the bases characteristics of the window to launch
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('IPSA GAME PLATFORM')

def signup_button(): #here is some functions, this one define the actions when we click on the button to sign up
    c1 = courriel1.get_value()
    m1 = mdp1.get_value()
    file = open('File_username.csv', 'r')
    lines = file.readlines()
    flag=0
    for line in lines:
        line = line.strip()
        l = line.split(',') #the following lines search in the database if the email already exist 
        if l[0] == c1: #if yes, it returns to the user that it already exist
            colour1 = (200, 0, 0)
            fontObj = pygame.font.Font('freesansbold.ttf', 15)  
            text = fontObj.render("Already signed up email!", True, colour1)
            screen.blit(text, (550,320))
            pygame.display.update()
            pygame.time.delay(1000)
            flag=1
    if flag==0: #if not, it returns that the user is now registered
        if len(m1)>6:
            file=open("File_username.csv", "a")
            file.write(f"\n{c1},{m1}")
            colour1 = (200, 0, 0)
            fontObj = pygame.font.Font('freesansbold.ttf', 15)  
            text = fontObj.render("New user is registered!", True, colour1)
            screen.blit(text, (560,320))
            pygame.display.update()
            pygame.time.delay(1000)
            file.close()
        elif len(m1)<6: #these few lines check if the password is much long as necessary
            colour1 = (200, 0, 0)
            fontObj = pygame.font.Font('freesansbold.ttf', 15)  
            text = fontObj.render("The password is too short (min 6 characters)", True, colour1)
            screen.blit(text, (475,320))
            pygame.display.update()
            pygame.time.delay(1000)
            

def login_button(): #this function check in the data base if the email associated to the password are in the database
    c2 = courriel2.get_value()
    m2 = mdp2.get_value()
    file = open('File_username.csv', 'r')
    lines = file.readlines()
    flag=0
    for line in lines:
        line = line.strip()
        l = line.split(',')
        flag=0
        if l[0] == c2 and l[1] == m2: #if yes, it imports another python file which is another window to open (work in progress...)
            pygame_menu.events.EXIT #type: ignore
            import Afterloginsettings
            file.close()         
            flag=1
            return flag   
           
    if flag==0 and (l[0] != c2 or l[1] != m2): #if not, it returns to the user that there is an incorrect parameter
        colour1 = (200, 0, 0)
        fontObj = pygame.font.Font('freesansbold.ttf', 15)  
        text = fontObj.render("Username or password is not correct!", True, colour1)
        screen.blit(text, (500,320))
        pygame.display.update()
        pygame.time.delay(1000)
        flag=1  



difficulty = 1
def set_difficulty(set_difficulty: Tuple, value: Any) -> None:
    global difficulty
    difficulty = str(value)
    print(difficulty)

 
def start_the_game():
    print(difficulty)
         
level = pygame_menu.Menu('Select a Difficulty', 400, 400, theme=themes.THEME_SOLARIZED)
level.add.selector('levels :', [('level1', 1), ('level2', 2)], onchange=set_difficulty)

mainmenu = pygame_menu.Menu('Welcome to main menu!', 1280, 720, theme=themes.THEME_SOLARIZED) #theses few lines set up the different things to show on the main menu
courriel1 = mainmenu.add.text_input('Email: ', default='Email', maxchar=20)
mdp1 = mainmenu.add.text_input('Password: ', default='Password', maxchar=20)
mainmenu.add.button('Sign up', signup_button)
mainmenu.add.text_input('',maxchar=0)
courriel2 = mainmenu.add.text_input('Email: ', default='Email', maxchar=20)
mdp2 = mainmenu.add.text_input('Password: ',default='Password', maxchar=20)
mainmenu.add.button('Log in', login_button)
mainmenu.add.text_input('',maxchar=0)
mainmenu.add.button('Quit', pygame_menu.events.EXIT) # type: ignore

mainmenu.mainloop(screen)
