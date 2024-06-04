## Created by Sarah Houyoux & André Pavlov & Adrien Mourot ##
##########################24/05/2024#########################
                      ## Global code ##

import pygame
import pygame_menu
from pygame_menu import themes
import pygame_textinput
from typing import Tuple, Any
from tkinter import Tk, filedialog
import sys
import subprocess
import os
import csv
import random

global difficulty
difficulty = 1
theme=1

global languages
languages = {
            'en': {
                'main_menu': 'Main Menu',
                'Profile': 'Profile',
                'How to play': 'How to Play',
                'How to Play Menu':'How to play Menu',
                'Guess Who Game': 'Guess Who Game',
                'Score Board': 'Score Board',
                'More Games': 'More Games',
                'More Games Menu': 'More Games Menu',
                'Settings': 'Settings',
                'Choose language': 'Choose Language',
                'Back to Main Menu': 'Back to Main Menu',
                'Quit': 'Quit',
                'Welcome to main menu!': 'Bienvenue sur la plateforme de jeux!',
                'Log in': 'Log In',
                'Sign up': 'Sign Up',
                'Email: ': 'Email: ',
                'Password: ': 'Password: ',
                'Difficulty: ':'Difficulty:',
                'Delete User': 'Delete account',
                'New user is registered!': 'New user is registered',
                'Already signed up email!': 'Already signed up email!',
                'The password is too short (min 6 characters)': 'The password is too short (min 6 characters)',
                'IPSA GAME PLATFORM': 'IPSA GAME PLATFORM',
                'Return': 'Return',
                'Ranks':'Ranks',
                'Names':'Names',
                'Score Board Menu': 'Score Board Menu',
                'Switch Frame': 'Switch Frame',
                'Your Guess': 'Your Guess',
                'Delete': 'Delete',
                'Next player\'s turn':'Next payer\'s turn',
                'Your card':'Your card',
                'wins!':'wins!',
                'Player':'Player',
                'Hello':'Hello',
                'Let me explain how to play the game':'Let me explain how to play',
                'Guess Who ?':'Guess Who ?',
                'It\'s a two-player board game where players each':'It\'s a two-player board game where players each',
                'guess the identity of the others chosen character.':'guess the identity of the others chosen character.',
                'Player ask each other yes_no questions.':'Player ask each other closed questions.',
                'For instance , hair color of the chosen character':'For instance , hair color of the chosen character',
                'will help to evaluate many characters to':'will help to evaluate many characters to',
                'make correct guest.':'make correct guest.',
                'By clicking the image':'By clicking the image',
                'By upload your image':'By uploading your image',
                'OR':'OU',
                'write a nickname':'write a nickname',
                'Choose your character':'Choose your character',
                'Unable to load image.':'Unable to load image.',
                'Profile Menu':'Profile Menu',
                'lost!':'lost!'
            },
            'fr': {
                'main_menu': 'Menu Principal',
                'Profile': 'Profil',
                'How to play': 'Comment Jouer',
                'How to Play Menu':'Menu "Comment Jouer"',
                'Guess Who Game': 'Jeu Qui est-ce',
                'Score Board': 'Tableau des Scores',
                'More Games': 'Plus de Jeux',
                'More Games Menu': 'Menu avec plus de Jeux',
                'Settings': 'Paramètres',
                'Choose language': 'Choisir la langue',
                'Back to Main Menu': 'Retour au menu principal',
                'Quit': 'Quitter',
                'Welcome to main menu!': 'Bienvenue sur la plateforme de jeux!',
                'Log in': 'Se connecter',
                'Sign up': 'S\'inscrire',
                'Email': 'Courriel: ',
                'Password: ': 'Mot de passe: ',
                'Difficulty: ': 'Difficulté:',
                'Delete User': 'Supprimer le compte',
                'New user is registered!': 'Nouveau compte enregistré',
                'Already signed up email!': 'Courriel déjà enregistré',
                'The password is too short (min 6 characters)': 'Le mot de passe est trop court (min 6 caractères)',
                'IPSA GAME PLATFORM': 'PLATEFORME DE JEUX IPSA',
                'Return': 'Retour',
                'Ranks':'Rangs',
                'Names':'Noms',
                'Score Board Menu': 'Menu Podium',
                'Switch Frame': 'Changer',
                'Your Guess': 'Votre choix',
                'Delete': 'Supprimer',
                'Next player\'s turn':'Tour de l\'autre joueur',
                'Your card':'Votre Carte',
                'wins!':'gagnant!',
                'Player':'Joueur',
                'Hello':'Bonjour',
                'Let me explain how to play the game':'Voici comment jouer au jeu',
                'Guess Who ?':'Qui est-ce ?',
                'It\'s a two-player board game where players each':'C\'est un jeu de plateau où chaque joueur',
                'guess the identity of the others chosen character.':'choisit un personnage',
                'Player ask each other yes_no questions.':'Le joueur demande à l\'autre des questions fermées.',
                'For instance , hair color of the chosen character':'Par exemple, la couleur des cheveux',
                'will help to evaluate many characters to':'va aider à évaluer plusieurs personnages',
                'make correct guest.':'et faire le bon choix.',
                'By clicking the image': 'En cliquant l\'image',
                'By upload your image': 'En chargeant votre image',
                'OR':'OU',
                'write a nickname':'écrivez votre pseudo',
                'Choose your character':'choisissez votre image',
                'Unable to load image.':'impossible de charger l\'image',
                'Profile Menu':'Menu du Profil',
                'lost!':'perdant!'
            },
            'tr': {
                'main_menu': 'Ana Menü',
                'Profile': 'Profil',
                'How to play': 'Oyunu Nasıl Oynanır',
                'How to Play Menu': 'Nasıl Oynanır Menüsü',
                'Guess Who Game': 'Kimse Söyle',
                'Score Board': 'Puan Tablosu',
                'More Games': 'Başka oyunlar',
                'More Games Menu': 'Çıkış',
                'Settings': 'Ayarlar',
                'Choose language': 'Dil Seçin',
                'Back to Main Menu': 'Ana Menüye Dön',
                'Quit': 'Çıkış Yap',
                'Welcome to main menu!': 'Oyun platformuna hoş geldiniz!',
                'Log in': 'Giriş',
                'Sign up': 'Kaydol',
                'Email': 'E-posta: ',
                'Password: ': 'Şifre: ',
                'Difficulty: ': 'Zorluk:',
                'Delete User': 'Kullanıcı Sil',
                'New user is registered!': 'Yeni kullanıcı kaydedildi!',
                'Already signed up email!': 'Bu e-posta zaten kayıtlı!',
                'The password is too short (min 6 characters)': 'Şifre çok kısa (en az 6 karakter)',
                'IPSA GAME PLATFORM': 'OYUN PLATFORMU IPSA',
                'Return': 'Geri Dön',
                'Ranks':'Sıralamalar',
                'Names':'İsimler',
                'Score Board Menu': 'Puan Tablosu Menüsü',
                'Switch Frame': 'Değiştir',
                'Your Guess': 'Tahmininiz',
                'Delete': 'Sil',
                'Next player\'s turn':'Sonraki oyuncunun turu',
                'Your card':'Kartınız',
                'wins!':'kazandı!',
                'Player':'Oyuncu',
                'Hello':'Merhaba',
                'Let me explain how to play the game':'Oyun nasıl oynanırı öğreteyim',
                'Guess Who ?':'Kimse Söyle?',
                'It\'s a two-player board game where players each':'İki oyuncu için bir plaka oyunudur. Her oyuncu',
                'guess the identity of the others chosen character.':'diğer oyuncunun seçtiği karakteri tahmin eder.',
                'Player ask each other yes_no questions.':'Oyuncular birbirlerine evet-hayır sorular sorarlar.',
                'For instance , hair color of the chosen character':'Örneğin, seçili karakterin saç rengi',
                'will help to evaluate many characters to':'çok sayıda karakteri değerlendirmek için yardımcı olur.',
                'make correct guest.':'doğru tahmin yapmak için.',
                'By clicking the image': 'Resmi tıklayarak',
                'By upload your image': 'Resim yükleyerek',
                'OR':'VEYA',
                'write a nickname':'bir takma ad yazın',
                'Choose your character':'Karakterinizi seçin',
                'Unable to load image.':'Resim yüklenemiyor.',
                'Profile Menu':'Profil Menüsü',
                'lost!':'kaybetti!'
            }
        }
global current_language
current_language = 'en'

def t(key):
    return languages[current_language][key]

pygame.init() #here, we define the bases characteristics of the window to launch
screen = pygame.display.set_mode((1280 , 720))
pygame.display.set_caption(t('IPSA GAME PLATFORM'))

class Button:
    def __init__(self, text, pos, font, bg="black"):
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

run =True

while run:

    def profile():
                with open('profile.csv', 'r') as file:
                    lines = file.readlines()  # Read all lines
                    if lines:
                        last_line = lines[-1]  # Get the last line
                        l = last_line.split(',')
                        return l[0]

    ## Main menu after log in##
    #########25/05/2024########

    def afterloginmenu():
        profilemenu = pygame_menu.Menu('Menu', 1280, 720, theme=themes.THEME_SOLARIZED) #theses few lines set up the different things to show on the main menu
        profilemenu.add.button(t('Profile'), profile_menu)
        profilemenu.add.button(t('How to play'), htp_menu)
        profilemenu.add.button(t('Guess Who Game'), guess_who_menu)
        profilemenu.add.button(t('Score Board'), sb_menu)
        profilemenu.add.button(t('More Games'), mg_menu)
        profilemenu.add.button(t('Settings'), settings_menu)
        profilemenu.add.text_input('',maxchar=0)
        profilemenu.add.button(t('Quit'), pygame_menu.events.EXIT) #type: ignore
        profilemenu.mainloop(screen)
    
    ## Profile Menu ##
    ### 28/05/2024 ###

    def profile_menu():
        pygame.display.set_caption(t("Profile Menu"))
        uploaded_image = None
        image_dir = "D:/Aero 1/2nd semester/AnGp121 - Programming project/Student_File-2024/charIcons/"
        WHITE   = (255, 255, 255)
        files = os.listdir(image_dir)
        image_files = [f for f in files if f.endswith(".png")]
        images = [pygame.image.load(os.path.join(image_dir, f)) for f in image_files]
        image_names = [f.replace(".png", "") for f in image_files]
        current_images = {i: {"image": images[i], "name": image_names[i]} for i in range(len(images))}

        textinput = pygame_textinput.TextInputVisualizer()

        def upload_image():
            Tk().withdraw()
            file_path = filedialog.askopenfilename()
            if file_path:
                try:
                    return pygame.image.load(file_path)
                except pygame.error:
                    print(t("Unable to load image."))
            return None

        def save_profile(nickname, image_path):
            with open('profile.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Nickname', 'ImagePath'])
                writer.writerow([nickname, image_path])

        def update_username_file(email, nickname):
            # Read the current data from the file
            with open('File_username.csv', mode='r', newline='') as file:
                reader = csv.reader(file)
                rows = list(reader)

            # Find the row with the given email and update the nickname
            for row in rows:
                if row[0] == email:
                    row[2] = nickname
                    break

            # Write the updated data back to the file
            with open('File_username.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)

        def get_logged_in_email():
            with open('temp_email.txt', 'r') as f:
                return f.read().strip()
            
        return_button = Button(t("Return"), (screen.get_width() - 120, screen.get_height() - 60), font=36)

        logged_in_email = get_logged_in_email()
        running_profile=True
        while running_profile:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for pos, img_rect in enumerate(image_rects): #type: ignore
                        if img_rect.collidepoint(event.pos):
                            current_images[pos]["image"] = images[(images.index(current_images[pos]["image"]) + 1) % len(images)]
                            current_images[pos]["name"] = image_names[(image_names.index(current_images[pos]["name"]) + 1) % len(image_names)]
                        elif return_button.click(event):
                            pygame.display.set_caption(t('IPSA GAME PLATFORM'))
                            running_profile=False

            screen.fill((239, 231, 211))

            image_rects = []
            font = pygame.font.Font(None, 36)

            img_rect = screen.blit(current_images[0]["image"], (280, 300))
            image_rects.append(img_rect)
            text = font.render(current_images[0]["name"], True, (0, 0, 0))
            screen.blit(text, (275, 390))
            choice1 = font.render(t("By clicking the image"), True, (0, 0, 0))
            choice2 = font.render(t("By upload your image"), True, (0, 0, 0))
            between = font.render(t("OR"), True, (0, 0, 0))
            pseudo = font.render(t("write a nickname"), True, (0, 0, 0))
            title = font.render(t("Choose your character"), True, (0, 0, 0))
            screen.blit(choice1, (200, 250))
            screen.blit(choice2, (830, 250))
            screen.blit(between, (625, 330))
            screen.blit(pseudo, (860, 390))
            screen.blit(title, (515, 100))

            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if 930 <= event.pos[0] <= 1005 and 300 <= event.pos[1] <= 375:
                        uploaded_image = uploaded_image_path = upload_image()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    nickname = textinput.value
                    image_path = uploaded_image_path if uploaded_image else os.path.join(image_dir, current_images[0]["name"] + ".png")
                    save_profile(nickname, image_path)
                    update_username_file(logged_in_email, nickname)

            pygame.draw.rect(screen, WHITE, (930,300, 75, 75))
            pygame.draw.rect(screen, WHITE, (875,430, 175, 40))

            textinput.update(events) #type:ignore
            screen.blit(textinput.surface, (880, 435))

            if uploaded_image:
                screen.blit(uploaded_image, (930, 300))

            return_button.show()

            pygame.display.update()


    ## How to Play Menu ##
    ##### 28/05/2024 #####

    def htp_menu():
        pygame.display.set_caption(t('How to Play Menu'))
        running_htp=True
        while running_htp: 
            image1 = pygame.image.load("img_allchar.png")
            images = [image1]
            current_images = {i: {"image": images[i]} for i in range(len(images))}

            return_button = Button(t("Return"), (screen.get_width() - 120, screen.get_height() - 60), font=36)

            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        for pos, img_rect in enumerate(image_rects): #type: ignore
                            if img_rect.collidepoint(event.pos):
                                current_images[pos]["image"] = images[(images.index(current_images[pos]["image"]) + 1) % len(images)]
                        if return_button.click(event):
                            pygame.display.set_caption(t('IPSA GAME PLATFORM')) 
                            running_htp=False
            screen.fill((239, 231, 211))

            image_rects = []
            font = pygame.font.Font(None, 36)

            img_rect = screen.blit(current_images[0]["image"], (150, 150))
            image_rects.append(img_rect)

            profile_name=profile()

            hello=font.render(f"{t('Hello')} {profile_name}. {t('Let me explain how to play the game')}", True, (0, 100, 0))
            screen.blit(hello, (80,50 ))

            rule= font.render(t("Guess Who ?"), True, (0, 0, 100))
            rule2= font.render(t("It's a two-player board game where players each"), True, (0, 0, 100))
            rule3= font.render(t("guess the identity of the others chosen character."), True, (0, 0, 100))
            rule4= font.render(t("Player ask each other yes_no questions."), True, (0, 0, 100))
            rule5= font.render(t("For instance , hair color of the chosen character"), True, (0, 0, 100))
            rule6= font.render(t("will help to evaluate many characters to"), True, (0, 0, 100))
            rule7= font.render(t("make correct guest."), True, (0, 0, 100))
            screen.blit(rule, (640,150))
            screen.blit(rule2, (640,200))
            screen.blit(rule3, (640,250))
            screen.blit(rule4, (640,300))
            screen.blit(rule5, (640,350))
            screen.blit(rule6, (640,400))
            screen.blit(rule7, (640,450))

            return_button.show()

            pygame.display.flip()
        
    
    ## Guess Who Game ##
    #### 01/06/2024 ####

    def guess_who_menu():
        Profile_name="profile.csv"
        File_username_path="File_username.csv"
        image_dir=r"D:\Aero 1\2nd semester\AnGp121 - Programming project\Student_File-2024\charIcons"
        running_game=True 
        
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

        while running_game:
            pygame.init()

            screen_width = 1280
            screen_height = 720
            screen = pygame.display.set_mode((screen_width, screen_height))
            pygame.display.set_caption(t("Guess Who Game"))
            screen.fill((239, 231, 211))


            image_files = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))] #these lines allow to pick up somes images in the charIcons repertory
            random.shuffle(image_files)
            selected_images = image_files[:29]
            first_32_images = selected_images[:14]
            second_32_images = selected_images[14:29]


            loaded_images_first_set = [pygame.image.load(os.path.join(image_dir, img)) for img in first_32_images]
            loaded_images_second_set = [pygame.image.load(os.path.join(image_dir, img)) for img in second_32_images]

            random_image_first_set = random.choice(loaded_images_first_set) #these two lines allow to choose a card for both players
            random_image_second_set = random.choice(loaded_images_second_set)
            
            margin = 10
                     
            def calculate_positions(loaded_images):
                positions = []
                y_offset = 50
                if difficulty==1:
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
                elif difficulty==2:
                    x_offset = (screen_width - sum([img.get_width() + margin for img in loaded_images[:8]]) + margin) // 2
                    for i in range(8):
                        x_pos = x_offset + i * (loaded_images[i].get_width() + margin)
                        positions.append((x_pos, y_offset))
                    y_offset += loaded_images[0].get_height() + margin
                    x_offset = (screen_width - sum([img.get_width() + margin for img in loaded_images[8:15]]) + margin) // 2
                    for i in range(7):
                        x_pos = x_offset + i * (loaded_images[8 + i].get_width() + margin)
                        positions.append((x_pos, y_offset))
                    return positions

            positions_first_set = calculate_positions(loaded_images_first_set)
            positions_second_set = calculate_positions(loaded_images_second_set)

            font = pygame.font.Font(None, 36)
            text = t("Your card")
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
            return_button = Button(t("Return"), (screen.get_width() - 100, screen.get_height() - 400), font=36)
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
                            for i, pos in enumerate(positions_first_set if first_frame else positions_second_set): #type:ignore
                                img_rect = (loaded_images_first_set if first_frame else loaded_images_second_set)[i].get_rect(topleft=pos) #type:ignore
                                if img_rect.collidepoint(mouse_pos):
                                    del (loaded_images_first_set if first_frame else loaded_images_second_set)[i]
                                    del (positions_first_set if first_frame else positions_second_set)[i] #type:ignore
                                    break

                        elif guess_mode:
                            correct_guess = False
                            for i, pos in enumerate(positions_first_set if first_frame else positions_second_set): #type:ignore
                                img_rect = (loaded_images_first_set if first_frame else loaded_images_second_set)[i].get_rect(topleft=pos)
                                if img_rect.collidepoint(mouse_pos):
                                    if (first_frame and (loaded_images_first_set[i] == random_image_first_set)) or \
                                        (not first_frame and (loaded_images_second_set[i] == random_image_second_set)):
                                        screen.fill((239, 231, 211))
                                        win_frame_rect = pygame.Rect((screen_width // 2 - 100, screen_height // 2 - 50, 200, 100))
                                        pygame.draw.rect(screen, (239, 231, 211), win_frame_rect)
                                        win_text = font.render(f"{t('Player')} {current_player} {t('wins!')}", True, (0, 0, 0))
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
                                lose_text = font.render(f"{t('Player')} {current_player} {t('lost!')}", True, (0, 0, 0))
                                screen.blit(lose_text, lose_text.get_rect(center=lose_frame_rect.center))
                                pygame.display.flip()
                                pygame.time.wait(3000)
                                update_player_score(current_player_username, -1)
                                running = False

                            guess_mode = False

                    screen.fill((239, 231, 211))

                    if waiting_frame:
                        waiting_text = font.render(t("Next player's turn"), True, (0, 0, 0))
                        screen.blit(waiting_text, waiting_text.get_rect(center=(screen_width // 2, screen_height // 2)))
                    else:
                        for img, pos in zip((loaded_images_first_set if first_frame else loaded_images_second_set),
                                            (positions_first_set if first_frame else positions_second_set)): #type:ignore
                            screen.blit(img, pos)

                        random_image = random_image_first_set if not first_frame else random_image_second_set
                        random_image_rect = random_image.get_rect(center=(screen_width // 2, screen_height - 100 - random_image.get_height() // 2))
                        screen.blit(random_image, random_image_rect)
                        screen.blit(text_surface, text_rect)

                    button_color = (4, 47, 58)
                    pygame.draw.rect(screen, button_color, delete_button_rect)
                    delete_button_text = font.render(t("Delete"), True, button_text_color)
                    screen.blit(delete_button_text, delete_button_text.get_rect(center=delete_button_rect.center))

                    pygame.draw.rect(screen, button_color, guess_button_rect)
                    guess_button_text = font.render(t("Your Guess"), True, button_text_color)
                    screen.blit(guess_button_text, guess_button_text.get_rect(center=guess_button_rect.center))

                    pygame.draw.rect(screen, button_color, switch_frame_button_rect)
                    switch_frame_button_text = font.render(t("Switch Frame"), True, button_text_color)
                    screen.blit(switch_frame_button_text, switch_frame_button_text.get_rect(center=switch_frame_button_rect.center))

                    if return_button.click(event):
                        pygame.display.set_caption(t('IPSA GAME PLATFORM')) 
                        running_game=False
                        afterloginmenu()
                    
                pygame.display.flip()

                return_button.show()
            pygame.display.update()
        
    
    
    ## Score Board ##
    ### 30/05/2024 ##

    def sb_menu():
        running_sb=True
        pygame.display.set_caption(t('Score Board Menu'))
        def profile():
            with open('profile.csv', 'r') as file:
                lines = file.readlines()  # Read all lines
                if lines:
                    last_line = lines[-1]  # Get the last line
                    l = last_line.split(',')
                    return l[0]
                
        return_button = Button(t("Return"), (screen.get_width() - 120, screen.get_height() - 60), font=36)
        while running_sb:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if return_button.click(event):
                        pygame.display.set_caption(t('IPSA GAME PLATFORM')) 
                        running_sb=False

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

            scoreboard = dict(zip(listname, scores))
            scoreboard_trie = dict(sorted(scoreboard.items(), key=lambda item: item[1], reverse=True))
            profile_name=profile()

            font = pygame.font.Font(None, 36)
            hello=font.render(f"Hello {profile_name}, here is the Leaderboard!", True, (100, 100, 200))
            screen.blit(hello, (140,100 ))
            first=font.render("#1", True, (100, 0, 0))
            second=font.render("#2", True, (100, 0, 0))
            third=font.render("#3", True, (100, 0, 0))
            screen.blit(first, (450,325 ))
            screen.blit(second, (450,400 ))
            screen.blit(third, (450,475 ))
            rank=font.render(t("Ranks"), True, (100, 0, 0))
            screen.blit(rank, (450,250 ))
            names=font.render(t("Names"), True, (0, 0, 100))
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
    

    ## More Games Menu ##
    ##### 30/05/2024 ####

    def mg_menu():
        pygame.display.set_caption(t('More Games Menu'))
        def start_snake_game():
            subprocess.Popen([sys.executable, r'D:\Aero 1\2nd semester\AnGp121 - Programming project\Student_File-2024\Snake\snake.py'])

        def start_table_tennis_game():
            subprocess.Popen([sys.executable, r'D:\Aero 1\2nd semester\AnGp121 - Programming project\Student_File-2024\TableTennis\Pong7_Score.py'])

        def start_starfield_game():
            subprocess.Popen([sys.executable, r"D:\Aero 1\2nd semester\AnGp121 - Programming project\Student_File-2024\Starfield\Starfield.py"])

        snake_image = pygame.image.load(r"D:\Aero 1\2nd semester\AnGp121 - Programming project\Student_File-2024\Snake\Graphics\apple.png")
        table_tennis_image = pygame.image.load(r"D:\Aero 1\2nd semester\AnGp121 - Programming project\Student_File-2024\TableTennis\Ball.png")
        starfield_image = pygame.image.load(r"D:\Aero 1\2nd semester\AnGp121 - Programming project\Student_File-2024\Starfield\img\playerShip1_orange.png")
        snake_rect = snake_image.get_rect(topleft=(200, 200))
        table_tennis_rect = table_tennis_image.get_rect(topleft=(600, 200))
        starfield_rect = starfield_image.get_rect(topleft=(1000, 200))

        return_button = Button(t("Return"), (screen.get_width() - 120, screen.get_height() - 60), font=36)

        running_sb=True

        while running_sb:
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
                        pygame.display.set_caption(t('IPSA GAME PLATFORM')) 
                        running_sb=False
            
            return_button.show()

            pygame.display.update()


    ## Settings Menu ##
    #### 31/05/2024 ###
 
    def settings_menu():
        pygame.display.set_caption(t('Settings'))

        def set_language(value, lang):
            global current_language
            current_language = lang

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
        
        def deleteuser_button():
            name_of_the_profile=profile()
            with open('File_username.csv','r')as file:
                reader = csv.reader(file)
                rows = list(reader)

            with open('FIle_username.csv','w',newline='')as file:
                writer=csv.writer(file)
                for row in rows:
                    if row[2] != name_of_the_profile:
                        writer.writerow(row)  
            main_menu()

        def return_button():
            pygame.display.set_caption(t('IPSA GAME PLATFORM'))
            afterloginmenu()
        
        running_settings=True

        while running_settings:
            settings_menu = pygame_menu.Menu(t('Settings'), 1280, 720, theme=themes.THEME_SOLARIZED)
            settings_menu.add.selector(t('Difficulty: '), [('Easy', 1), ('Hard', 2)], onchange=set_difficulty)
            settings_menu.add.selector(t('Choose language'), [('English', 'en'), ('Français', 'fr'), ('Türkçe', 'tr')], onchange=set_language)
            settings_menu.add.button(t('Delete User'), deleteuser_button)
            settings_menu.add.button(t('Back to Main Menu'), return_button)
            settings_menu.mainloop(screen)

    
    ## Main menu parameters ##

    def main_menu():
            ## Main Menu - log in & Sign up##

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
                    colour1 = (200, 0, 0) #we choose colour red in RGB for all messages important messages 
                    fontObj = pygame.font.Font('freesansbold.ttf', 15)  
                    text = fontObj.render(t("Already signed up email!"), True, colour1)
                    screen.blit(text, (550,320))
                    pygame.display.update()
                    pygame.time.delay(1000)
                    flag=1
            if flag==0: #if not, it returns that the user is now registered
                if len(m1)>6:
                    file=open("File_username.csv", "a")
                    file.write(f"{c1},{m1},no nickname,0\n")
                    colour1 = (200, 0, 0)
                    fontObj = pygame.font.Font('freesansbold.ttf', 15)  
                    text = fontObj.render(t("New user is registered!"), True, colour1)
                    screen.blit(text, (560,320))
                    pygame.display.update()
                    pygame.time.delay(1000)
                    file.close()
                elif len(m1)<6: #these few lines check if the password is much long as necessary
                    colour1 = (200, 0, 0)
                    fontObj = pygame.font.Font('freesansbold.ttf', 15)  
                    text = fontObj.render(t("The password is too short (min 6 characters)"), True, colour1)
                    screen.blit(text, (475,320))
                    pygame.display.update()
                    pygame.time.delay(1000)


        def login_button(): #this function check in the data base if the email associated to the password are in the database
            global c2
            c2 = courriel2.get_value()
            m2 = mdp2.get_value()
            flag=0
            file = open('File_username.csv', 'r')
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                l = line.split(',')
                if l[0] == c2 and l[1] == m2: #if yes, it imports another python file which is another window to open
                    file.close()
                    with open('temp_email.txt', 'w') as temp_file:
                        temp_file.write(c2)
                        file.close()
                    afterloginmenu()   
                    flag=1
                
            if flag==0 and (l[0] != c2 or l[1] != m2): #if not, it returns to the user that there is an incorrect parameter
                colour1 = (200, 0, 0)
                fontObj = pygame.font.Font('freesansbold.ttf', 15)  
                text = fontObj.render("Username or password is not correct!", True, colour1)
                screen.blit(text, (500,320))
                pygame.display.update()
                pygame.time.delay(1000)
                flag=1 

        mainmenu = pygame_menu.Menu(t('Welcome to main menu!'), 1280, 720, theme=themes.THEME_SOLARIZED) #theses few lines set up the different things to show on the main menu
        courriel1 = mainmenu.add.text_input(t('Email: '), default='Email', maxchar=30)
        mdp1 = mainmenu.add.text_input(t('Password: '), default='Password', maxchar=20)
        mainmenu.add.button(t('Sign up'), signup_button)
        mainmenu.add.text_input('',maxchar=0)
        courriel2 = mainmenu.add.text_input(t('Email: '), default='Email', maxchar=30)
        mdp2 = mainmenu.add.text_input(t('Password: '),default='Password', maxchar=20)
        mainmenu.add.button(t('Log in'), login_button)
        mainmenu.add.text_input('',maxchar=0)
        mainmenu.add.button(t('Quit'), pygame_menu.events.EXIT) # type: ignore
        mainmenu.mainloop(screen)
    
    
    main_menu()
