import pygame
import sys
import pygame_menu
import os

pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Profile")

# Get the directory of the images
image_dir = "D:/Aero 1/2nd semester/AnGp121 - Programming project/Student_File-2024/charIcons/"

# Get a list of all the files in the directory
files = os.listdir(image_dir)

# Filter the list to only include the image files
image_files = [f for f in files if f.endswith(".png")]

# Load the images
images = [pygame.image.load(os.path.join(image_dir, f)) for f in image_files]

# List of image names
image_names = [f.replace(".png", "") for f in image_files]

# Dictionary to keep track of the current image and its name for each position
current_images = {i: {"image": images[i], "name": image_names[i]} for i in range(len(images))}

def upload_profile_image():
    # Open a file dialog to select the image file
    file_path = pygame_menu.locals.files.get_open_file_name(title="Select Profile Image", file_filter=["*.png", "*.jpg", "*.jpeg"])

    # Check if a file was selected
    if file_path is not None:
        # Load the selected image
        image = pygame.image.load(file_path)

        # Add the image to the list of images
        images.append(image)

        # Add the image name to the list of image names
        image_name = os.path.basename(file_path).replace(".png", "").replace(".jpg", "").replace(".jpeg", "")
        image_names.append(image_name)

        # Update the current_images dictionary
        current_images[len(images) - 1] = {"image": image, "name": image_name}

# Create the menu
menu = pygame_menu.Menu('Profile', 500, 300)

# Add the "Upload Profile Image" button
menu.add.button('Upload Profile Image', upload_profile_image)

# Add the rest of the buttons
#...

# Display the menu
menu.mainloop(screen)