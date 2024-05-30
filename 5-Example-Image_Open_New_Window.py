import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Click Image to Open New Window")

# Set up colors
WHITE = (255, 255, 255)

# Load the images
images = [pygame.image.load(r"D:\Aero 1\2nd semester\AnGp121 - Programming project\Student_File-2024\Snake\Graphics\apple.png"), 
          pygame.image.load(r"D:\Aero 1\2nd semester\AnGp121 - Programming project\Student_File-2024\Starfield\img\starfield.png"),
          ]

# Get the image dimensions
image_rects = [image.get_rect() for image in images]

# Set initial positions for images
start_x = (SCREEN_WIDTH - sum(image.get_width() for image in images) - 200 * (len(images) - 1)) // 2
start_y = (SCREEN_HEIGHT - image_rects[0].height) // 2

for i, rect in enumerate(image_rects):
    rect.x = start_x + (image_rects[0].width + 50) * i
    rect.y = start_y

def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the mouse click is inside any of the images
                for index, rect in enumerate(image_rects):
                    if rect.collidepoint(event.pos):
                        open_new_window(index)

        # Fill the screen with white
        screen.fill(WHITE)
        
        # Draw the images on the screen
        for index, image in enumerate(images):
            screen.blit(image, image_rects[index])
        
        # Update the display
        pygame.display.flip()

def open_new_window(image_index):
    # Set up a new window
    new_screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("New Window")
    
    # Fill the new window with a different color based on the clicked image index
    new_screen.fill((200, 200, 200))

    # Display the clicked image in the new window
    clicked_image = images[image_index]
    new_screen.blit(clicked_image, (50, 50))
    
    # Update the display
    pygame.display.flip()

    # Wait for the new window to close
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Return to the main loop if the new window is closed

if __name__ == "__main__":
    main()
