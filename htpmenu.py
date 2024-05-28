import pygame
import sys
import subprocess
 
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('How to play Menu')

def profile():
    with open('profile.csv', 'r') as file:
        lines = file.readlines()  # Read all lines
        if lines:
            last_line = lines[-1]  # Get the last line
            l = last_line.split(',')
            return l[0]

image1 = pygame.image.load("img_allchar.png")
images = [image1]
 
current_images = {i: {"image": images[i]} for i in range(len(images))}

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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for pos, img_rect in enumerate(image_rects):
                if img_rect.collidepoint(event.pos):
                    current_images[pos]["image"] = images[(images.index(current_images[pos]["image"]) + 1) % len(images)]
            if return_button.click(event): 
                subprocess.Popen([sys.executable, 'Afterloginsettings.py'])
                pygame.quit()
                sys.exit()

    screen.fill((239, 231, 211))

    image_rects = []
    font = pygame.font.Font(None, 36)

    img_rect = screen.blit(current_images[0]["image"], (150, 150))
    image_rects.append(img_rect)

    profile_name=profile()

    hello=font.render(f"Hello {profile_name} ,Let me explain how to play the game", True, (0, 100, 0))
    screen.blit(hello, (80,50 ))

    rule= font.render("Guess Who ?", True, (0, 0, 100))
    rule2= font.render("It's a two-player board game where players each", True, (0, 0, 100))
    rule3= font.render("guess the identity of the others chosen character.", True, (0, 0, 100))
    rule4= font.render("Player ask each other yes_no questions.", True, (0, 0, 100))
    rule5= font.render("For instance , hair color of the chosen character", True, (0, 0, 100))
    rule6= font.render("will help to evaluate many characters to", True, (0, 0, 100))
    rule7= font.render("make correct guest.", True, (0, 0, 100))
    screen.blit(rule, (640,150 ))
    screen.blit(rule2, (640,200 ))
    screen.blit(rule3, (640,250 ))
    screen.blit(rule4, (640,300 ))
    screen.blit(rule5, (640,350 ))
    screen.blit(rule6, (640,400 ))
    screen.blit(rule7, (640,450 ))

    return_button.show()

    pygame.display.flip()