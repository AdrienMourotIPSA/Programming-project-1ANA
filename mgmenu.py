## Created by Sarah Houyoux & André Pavlov & Adrien Mourot ##
##########################30/05/2024#########################

import pygame
import pygame_menu
from typing import Tuple, Any
import pygame_menu.themes
import subprocess
import sys

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('More Games Menu')

class Button:
    def __init__(self, text, pos, font, bg=(4, 47, 58), feedback=""):
        self.x, self.y = pos
        self.font = pygame.font.Font(None, font)
        self.change_text(text, bg)

    def change_text(self, text, bg=(4, 47, 58)):
        self.text = self.font.render(text, True, pygame.Color("white"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill((4, 47, 58))
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

def Return_button():
    subprocess.Popen([sys.executable, 'Afterloginsettings.py'])
    pygame.quit()
    sys.exit()

def start_snake_game():
    subprocess.Popen([sys.executable, r'D:\Aero 1\2nd semester\AnGp121 - Programming project\Student_File-2024\Snake\snake.py'])

def start_table_tennis_game():
    subprocess.Popen([sys.executable, r'D:\Aero 1\2nd semester\AnGp121 - Programming project\Student_File-2024\TableTennis\Pong7_Score.py'])

def start_starfield_game():
    subprocess.Popen([sys.executable, r"D:\Aero 1\2nd semester\AnGp121 - Programming project\Student_File-2024\Starfield\Starfield.py"])

def show_message(message, callback=None):
    msg_menu = pygame_menu.Menu('', 600, 400, theme=pygame_menu.themes.THEME_DARK)
    msg_menu.add.label(message)
    msg_menu.add.button('Back', callback or pygame_menu.events.BACK)  # type: ignore
    msg_menu.mainloop(screen)

snake_image = pygame.image.load(r"D:\Aero 1\2nd semester\AnGp121 - Programming project\Student_File-2024\Snake\Graphics\apple.png")
table_tennis_image = pygame.image.load(r"D:\Aero 1\2nd semester\AnGp121 - Programming project\Student_File-2024\TableTennis\Ball.png")
starfield_image = pygame.image.load(r"D:\Aero 1\2nd semester\AnGp121 - Programming project\Student_File-2024\Starfield\img\playerShip1_orange.png")
snake_rect = snake_image.get_rect(topleft=(200, 200))
table_tennis_rect = table_tennis_image.get_rect(topleft=(600, 200))
starfield_rect = starfield_image.get_rect(topleft=(1000, 200))

return_button = Button("Return", (screen.get_width() - 120, screen.get_height() - 60), font=36)

run = True
while run:
    screen.fill((239, 231, 211))
    screen.blit(snake_image, snake_rect.topleft)
    screen.blit(table_tennis_image, table_tennis_rect.topleft)
    screen.blit(starfield_image, starfield_rect.topleft)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if snake_rect.collidepoint(event.pos):
                start_snake_game()
            elif table_tennis_rect.collidepoint(event.pos):
                start_table_tennis_game()
            elif starfield_rect.collidepoint(event.pos):
                start_starfield_game()
            elif return_button.click(event): 
                subprocess.Popen([sys.executable, 'Afterloginsettings.py'])
                pygame.quit()
                sys.exit()
    
    return_button.show()

    pygame.display.update()
