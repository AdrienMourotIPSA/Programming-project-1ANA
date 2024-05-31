## Created by Sarah Houyoux & André Pavlov & Adrien Mourot ##
######################## 31/05/2024 #########################

import pygame
import pygame_menu
from pygame_menu import themes
from typing import Tuple, Any
import sys
import subprocess
import csv

run = True
difficulty = 1

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Settings')

def return_button():
    subprocess.Popen([sys.executable, 'Afterloginsettings.py'])
    pygame.quit()
    sys.exit()

def set_difficulty(selected_value: Tuple, difficulty_value: Any) -> None:
    global difficulty
    difficulty = difficulty_value
    save_difficulty_to_csv(difficulty)

def save_difficulty_to_csv(difficulty_value: int) -> None:
    with open('profile.csv', mode='r') as file:
        lines = list(csv.reader(file))

    while len(lines) < 2:
        lines.append([])
    while len(lines[1]) < 3:
        lines[1].append('')

    lines[1][2] = str(difficulty_value)

    with open('profile.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(lines)

while run:
    settings_menu = pygame_menu.Menu('Settings', 1280, 720, theme=themes.THEME_SOLARIZED)
    settings_menu.add.selector('Difficulty: ', [('Easy', 1), ('Hard', 2)], onchange=set_difficulty)
    settings_menu.add.selector('Sound: ', [('On', 1), ('Off', 2)])
    settings_menu.add.button('Back to Main Menu', return_button)
    settings_menu.mainloop(screen)
