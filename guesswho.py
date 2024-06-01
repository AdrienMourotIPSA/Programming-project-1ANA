## Created by Sarah Houyoux & André Pavlov & Adrien Mourot ##
##########################01/06/2024#########################

import pygame
from pygame_menu import themes
from typing import Tuple, Any
import csv
import os
import random

Profile_name=r"D:\Aero 1\2nd semester\AnGp121 - Programming project\Student_File-2024\profile.csv"
File_username_path=r"D:\Aero 1\2nd semester\AnGp121 - Programming project\Student_File-2024\File_username.csv"
image_dir=r"D:\Aero 1\2nd semester\AnGp121 - Programming project\Student_File-2024\charIcons"



def read_current_player():
    with open(Profile_name, 'r') as profile_file:
        return profile_file.readline().strip()

def update_player_score(username, score_change):
    with open(File_username_path, 'r') as infile:
        reader = list(csv.reader(infile))
    
    with open(File_username_path, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        for row in reader:
            if row[3] == username:
                row[2] = str(int(row[2]) + score_change)
            writer.writerow(row)

def Game():
    pygame.init()

    screen_width = 1300
    screen_height = 750
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Game Platform")
    screen.fill((239, 231, 211))


    image_files = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))] #these lines allow to pick up somes images in the charIcons repertory
    random.shuffle(image_files)
    selected_images = image_files[:22]
    first_11_images = selected_images[:11]
    second_11_images = selected_images[11:22]


    loaded_images_first_set = [pygame.image.load(os.path.join(image_dir, img)) for img in first_11_images]
    loaded_images_second_set = [pygame.image.load(os.path.join(image_dir, img)) for img in second_11_images]

    random_image_first_set = random.choice(loaded_images_first_set) #these two lines allow to choose a card for both players
    random_image_second_set = random.choice(loaded_images_second_set)

    margin = 10
    images_per_row = [6, 5]

    def calculate_positions(loaded_images):
        positions = []
        y_offset = 50
        x_offset = (screen_width - sum([img.get_width() + margin for img in loaded_images[:6]]) + margin) // 2
        for i in range(6):
            x_pos = x_offset + i * (loaded_images[i].get_width() + margin)
            positions.append((x_pos, y_offset))
        y_offset += loaded_images[0].get_height() + margin
        x_offset = (screen_width - sum([img.get_width() + margin for img in loaded_images[6:11]]) + margin) // 2
        for i in range(5):
            x_pos = x_offset + i * (loaded_images[6 + i].get_width() + margin)
            positions.append((x_pos, y_offset))
        return positions

    positions_first_set = calculate_positions(loaded_images_first_set)
    positions_second_set = calculate_positions(loaded_images_second_set)

    font = pygame.font.Font(None, 36)
    text = "Your card"
    text_color = (0, 0, 0)
    text_surface = font.render(text, True, text_color)

    text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height - 50))

    button_width = 200
    button_height = 50
    delete_button_rect = pygame.Rect(50, screen_height - 100, button_width, button_height)
    guess_button_rect = pygame.Rect(screen_width - 200, screen_height - 200, button_width, button_height)
    switch_frame_button_rect = pygame.Rect(screen_width - 200, screen_height - 100, button_width, button_height)


    button_text_color = (0, 0, 0)
    delete_mode = False
    guess_mode = False
    first_frame = True
    waiting_frame = False
    current_player = 1
    current_player_username = read_current_player()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if delete_button_rect.collidepoint(mouse_pos):
                    delete_mode = not delete_mode
                    guess_mode = False  

                elif guess_button_rect.collidepoint(mouse_pos):
                    guess_mode = not guess_mode
                    delete_mode = False  

                elif switch_frame_button_rect.collidepoint(mouse_pos):
                    if waiting_frame:
                        first_frame = not first_frame
                        waiting_frame = False
                    else:
                        waiting_frame = True
                        current_player = 2 if current_player == 1 else 1  

                elif delete_mode:
                    for i, pos in enumerate(positions_first_set if first_frame else positions_second_set):
                        img_rect = (loaded_images_first_set if first_frame else loaded_images_second_set)[i].get_rect(topleft=pos)
                        if img_rect.collidepoint(mouse_pos):
                            del (loaded_images_first_set if first_frame else loaded_images_second_set)[i]
                            del (positions_first_set if first_frame else positions_second_set)[i]
                            break

                elif guess_mode:
                    correct_guess = False
                    for i, pos in enumerate(positions_first_set if first_frame else positions_second_set):
                        img_rect = (loaded_images_first_set if first_frame else loaded_images_second_set)[i].get_rect(topleft=pos)
                        if img_rect.collidepoint(mouse_pos):
                            if (first_frame and (loaded_images_first_set[i] == random_image_first_set)) or \
                                (not first_frame and (loaded_images_second_set[i] == random_image_second_set)):
                                screen.fill((239, 231, 211))
                                win_frame_rect = pygame.Rect((screen_width // 2 - 100, screen_height // 2 - 50, 200, 100))
                                pygame.draw.rect(screen, (239, 231, 211), win_frame_rect)
                                win_text = font.render(f"Player {current_player} wins!", True, (0, 0, 0))
                                screen.blit(win_text, win_text.get_rect(center=win_frame_rect.center))
                                pygame.display.flip()
                                pygame.time.wait(3000)
                                update_player_score(current_player_username, 1)
                                correct_guess = True
                                running = False
                            break

                    if not correct_guess:
                        screen.fill((239, 231, 211))
                        lose_frame_rect = pygame.Rect((screen_width // 2 - 100, screen_height // 2 - 50, 200, 100))
                        pygame.draw.rect(screen, (239, 231, 211), lose_frame_rect)
                        lose_text = font.render(f"Player {current_player} lost!", True, (0, 0, 0))
                        screen.blit(lose_text, lose_text.get_rect(center=lose_frame_rect.center))
                        pygame.display.flip()
                        pygame.time.wait(3000)
                        update_player_score(current_player_username, -1)
                        running = False

                    guess_mode = False

            screen.fill((239, 231, 211))

            if waiting_frame:
                waiting_text = font.render("Next player's turn", True, (0, 0, 0))
                screen.blit(waiting_text, waiting_text.get_rect(center=(screen_width // 2, screen_height // 2)))
            else:
                for img, pos in zip((loaded_images_first_set if first_frame else loaded_images_second_set),
                                    (positions_first_set if first_frame else positions_second_set)):
                    screen.blit(img, pos)

                random_image = random_image_first_set if not first_frame else random_image_second_set
                random_image_rect = random_image.get_rect(center=(screen_width // 2, screen_height - 100 - random_image.get_height() // 2))
                screen.blit(random_image, random_image_rect)
                screen.blit(text_surface, text_rect)

            button_color = (4, 47, 58)
            pygame.draw.rect(screen, button_color, delete_button_rect)
            delete_button_text = font.render("Delete", True, button_text_color)
            screen.blit(delete_button_text, delete_button_text.get_rect(center=delete_button_rect.center))

            pygame.draw.rect(screen, button_color, guess_button_rect)
            guess_button_text = font.render("Your Guess", True, button_text_color)
            screen.blit(guess_button_text, guess_button_text.get_rect(center=guess_button_rect.center))

            pygame.draw.rect(screen, button_color, switch_frame_button_rect)
            switch_frame_button_text = font.render("Switch Frame", True, button_text_color)
            screen.blit(switch_frame_button_text, switch_frame_button_text.get_rect(center=switch_frame_button_rect.center))

        pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

    pygame.display.update()

Game()