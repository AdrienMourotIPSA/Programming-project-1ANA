##Created by Sarah Houyoux & André Pavlov & Adrien Mourot##
########################30/05/2024#########################

import pygame
import pygame_menu
from pygame_menu import themes
from typing import Tuple, Any
import sys
import subprocess
from operator import itemgetter
import numpy as np

pygame.init() #here, we define the bases characteristics of the window to launch
screen = pygame.display.set_mode((1280 , 720))
pygame.display.set_caption('Score Board Menu')

def profile():
    with open('profile.csv', 'r') as file:
        lines = file.readlines()  # Read all lines
        if lines:
            last_line = lines[-1]  # Get the last line
            l = last_line.split(',')
            return l[0]

class Button:
    def __init__(self, text, pos, font, bg="black", feedback=""):
        self.x, self.y = pos
        self.font = pygame.font.Font(None, font)
        self.change_text(text, bg)

    def change_text(self, text, bg="black"):
        self.text = self.font.render(text, True, pygame.Color("white"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def show(self):
        screen.blit(self.surface, (self.x, self.y))

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    return True
        return False

return_button = Button("Return", (screen.get_width() - 120, screen.get_height() - 60), font=36)

run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if return_button.click(event): 
                subprocess.Popen([sys.executable, 'Afterloginsettings.py'])
                pygame.quit()
                sys.exit()

    screen.fill((239, 231, 211))


    file = open('File_username.csv', 'r')
    lines = file.readlines()
    listname=[]
    listscore=[]
    for line in lines[1:]:
        line = line.strip()
        l = line.split(',')
        if len(l) < 4:
            l.append('0')
        listname.append(l[2])
        listscore.append(l[3])
    scores = list(map(int, listscore))

    # Création d'un dictionnaire associant les noms aux scores
    scoreboard = dict(zip(listname, scores))

    # Tri du dictionnaire par valeurs (scores) en ordre décroissant
    scoreboard_trie = dict(sorted(scoreboard.items(), key=lambda item: item[1], reverse=True))

    profile_name=profile()

    font = pygame.font.Font(None, 36)
    hello=font.render(f"Hello {profile_name} ,here is the Leaderboard!", True, (100, 100, 200))
    screen.blit(hello, (140,100 ))
    first=font.render("#1", True, (100, 0, 0))
    second=font.render("#2", True, (100, 0, 0))
    third=font.render("#3", True, (100, 0, 0))
    screen.blit(first, (450,325 ))
    screen.blit(second, (450,400 ))
    screen.blit(third, (450,475 ))
    rank=font.render("Ranks", True, (100, 0, 0))
    screen.blit(rank, (450,250 ))
    names=font.render("Names", True, (0, 0, 100))
    score=font.render("Scores", True, (0, 0, 100))
    screen.blit(names, (140,250 ))
    screen.blit(score, (300,250 ))

    top_three = list(scoreboard_trie.items())[:3]
    for i, (name, score) in enumerate(top_three):
        name_text = font.render(name, True, (0, 0, 0))
        score_text = font.render(str(score), True, (0, 0, 0))
        screen.blit(name_text, (140, 325 + i * 75))
        screen.blit(score_text, (300, 325 + i * 75))
    
    return_button.show()

    pygame.display.flip()


