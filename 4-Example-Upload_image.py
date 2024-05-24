import pygame
import sys
from tkinter import Tk, filedialog

# Initialize Pygame
pygame.init()
frame = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Image Uploade')

# Set up the dimensions of the window
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 128)
frame.fill(WHITE)

# Set up fonts
font = pygame.font.SysFont(None, 30)

# Function to display text on the screen
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

# Function to handle file upload
def upload_image():
    Tk().withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename()  # Show file dialog
    if file_path:
        try:
            # Load and return the image
            return pygame.image.load(file_path)
        except pygame.error:
            print("Unable to load image.")
    return None

run = True
uploaded_image = None

while run:
   # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the upload button is clicked
            if 110 <= event.pos[0] <= 260 and 160 <= event.pos[1] <= 200:
                # Upload the image
                uploaded_image = upload_image()

    # Draw the upload button
    pygame.draw.rect(frame, BLUE, (110, 160, 150, 40))
    draw_text('Upload Image', font, WHITE, frame, 120, 170)

    # If an image is uploaded, display it
    if uploaded_image:
        frame.blit(uploaded_image, (150, 50))

    # Update the display
    pygame.display.update()


