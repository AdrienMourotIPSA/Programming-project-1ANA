import pygame
import sys
 
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('How to play Menu')

def profile():
    file = open('profile.csv', 'r')
    lines = file.readlines()
    for line in lines:
        l = line.split(',')
        file.close()
        return(l[0])
# Load images
image1 = pygame.image.load("img_allchar.png")


 
# List of images
images = [image1]
 
 
# Dictionary to keep track of the current image and its name for each position
current_images = {i: {"image": images[i]} for i in range(len(images))}


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Change the image at the clicked position
            for pos, img_rect in enumerate(image_rects):
                if img_rect.collidepoint(event.pos):
                    current_images[pos]["image"] = images[(images.index(current_images[pos]["image"]) + 1) % len(images)]
                

    # Clear the screen
    screen.fill((239, 231, 211))

    # Draw the images and their names
    image_rects = []
    font = pygame.font.Font(None, 36)

    img_rect = screen.blit(current_images[0]["image"], (150, 150))
    image_rects.append(img_rect)

    hello=font.render(f"Hello {profile} ,Let me explain how to play the game", True, (0, 100, 0))
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



    # Update the display
    pygame.display.flip()