import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()
frame = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Pygame Window')

# frame color
color = (228, 230, 246)
frame.fill(color)

# load an image  
image = pygame.image.load("D:/Aero 1/2nd semester/AnGp121 - Programming project/Student_File-2024/img_allchar.png").convert()

# add text font, color, size
BLUE = (0, 0, 128)
fontObj = pygame.font.Font('freesansbold.ttf', 32)  
text = fontObj.render('Hello world!', True, BLUE)

run = True
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
	# use blit function to put your image and text on the frame that you want to present
	frame.blit(image, (120, 120))
	frame.blit(text, (100, 50))
	pygame.display.update()

