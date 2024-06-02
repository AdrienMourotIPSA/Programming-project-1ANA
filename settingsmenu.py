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

languages = {
    'en': {
        'main_menu': 'Main Menu',
        'profile': 'Profile',
        'how_to_play': 'How to Play',
        'game': 'Game',
        'score_board': 'Score Board',
        'more_games': 'More Games',
        'settings': 'Settings',
        'choose_language': 'Choose Language',
        'back': 'Back to Main Menu',
        'quit': 'Quit',
        'welcome': 'Welcome to Game Platform!',
    },
    'fr': {
        'main_menu': 'Menu Principal',
        'profile': 'Profil',
        'how_to_play': 'Comment Jouer',
        'game': 'Jeu',
        'score_board': 'Tableau des Scores',
        'more_games': 'Plus de Jeux',
        'settings': 'Paramètres',
        'choose_language': 'Choisir la langue',
        'back': 'Retour au menu principal',
        'quit': 'Quitter',
        'welcome': 'Bienvenue sur la plateforme de jeux!',
    }
}

current_language = 'en'

def t(key):
    return languages[current_language][key]

def set_language(value, lang):
    global current_language
    current_language = lang

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
    settings_menu.add.selector(t('choose_language'), [('English', 'en'), ('Français', 'fr')], onchange=set_language)
    settings_menu.add.button('Back to Main Menu', return_button)
    settings_menu.mainloop(screen)
