import pygame
import sys

pygame.init()

# Set up display
width, height = 600, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Change Images on Click")

# Load images
image1 = pygame.image.load("D:/Google Drive/IPSA/2023-2024/Semester2 - GrandProject/ESCAPE_GAME_v2/images/charIcons/1-mario.png")
image38 = pygame.image.load("D:/Google Drive/IPSA/2023-2024/Semester2 - GrandProject/ESCAPE_GAME_v2/images/charIcons/38-lucas.png")
image60 = pygame.image.load("D:/Google Drive/IPSA/2023-2024/Semester2 - GrandProject/ESCAPE_GAME_v2/images/charIcons/60-cloud.png")

# List of images
images = [image1, image38, image60]
image_names = ["Image 1", "Image 38", "Image 60"]

# Dictionary to keep track of the current image and its name for each position
current_images = {i: {"image": images[i], "name": image_names[i]} for i in range(len(images))}

def main():
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
                        current_images[pos]["name"] = image_names[(image_names.index(current_images[pos]["name"]) + 1) % len(image_names)]

        # Clear the screen
        screen.fill((255, 255, 255))

        # Draw the images and their names
        image_rects = []
        font = pygame.font.Font(None, 36)

        img_rect = screen.blit(current_images[0]["image"], (250, 200))
        image_rects.append(img_rect)
        text = font.render(current_images[0]["name"], True, (0, 0, 0))
        screen.blit(text, (200, 150))

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
