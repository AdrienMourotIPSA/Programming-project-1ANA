import pygame
import pygame_textinput
import sys
from tkinter import Tk, filedialog
import os

run=True
uploaded_image = None
pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Profile")

image_dir = "D:/Aero 1/2nd semester/AnGp121 - Programming project/Student_File-2024/charIcons/"
WHITE = (255, 255, 255)
BLUE = (0, 0, 128)

files = os.listdir(image_dir)
image_files = [f for f in files if f.endswith(".png")]
images = [pygame.image.load(os.path.join(image_dir, f)) for f in image_files]
image_names = [f.replace(".png", "") for f in image_files]
current_images = {i: {"image": images[i], "name": image_names[i]} for i in range(len(images))}

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

def upload_image():
    Tk().withdraw()
    file_path = filedialog.askopenfilename()
    if file_path:
        try:
            return pygame.image.load(file_path)
        except pygame.error:
            print("Unable to load image.")
    return None

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for pos, img_rect in enumerate(image_rects):
                if img_rect.collidepoint(event.pos):
                    current_images[pos]["image"] = images[(images.index(current_images[pos]["image"]) + 1) % len(images)]
                    current_images[pos]["name"] = image_names[(image_names.index(current_images[pos]["name"]) + 1) % len(image_names)]

    screen.fill((239,231,211))

    image_rects = []
    font = pygame.font.Font(None, 36)

    img_rect = screen.blit(current_images[0]["image"], (280, 300))
    image_rects.append(img_rect)
    text = font.render(current_images[0]["name"], True, (0, 0, 0))
    screen.blit(text, (275, 390))
    choice1 = font.render("By clicking the image", True, (0, 0, 0))
    choice2= font.render("By upload your image", True, (0, 0, 0))
    between=font.render("OR", True, (0, 0, 0))
    pseudo=font.render("write a nickname", True, (0, 0, 0))
    title=font.render("Choose your charater", True, (0, 0, 0))
    screen.blit(choice1, (200, 250))
    screen.blit(choice2, (830, 250))
    screen.blit(between, (625, 330))
    screen.blit(pseudo, (860, 390))
    screen.blit(title, (515, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if 930 <= event.pos[0] <= 1005 and 300 <= event.pos[1] <= 375:
                uploaded_image = upload_image()

    pygame.draw.rect(screen, WHITE, (930,300, 75, 75))
    pygame.draw.rect(screen, WHITE, (875,430, 175, 40))

    if uploaded_image:
        screen.blit(uploaded_image, (930, 300))
    
        

    pygame.display.update()