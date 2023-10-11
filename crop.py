import os
from PIL import Image

# Function to crop an image using a specified rectangle
def crop_image(input_path, output_path, crop_box):
    try:
        with Image.open(input_path) as img:
            cropped_img = img.crop(crop_box)
            cropped_img.save(output_path)
        print(f"Cropped '{input_path}' and saved as '{output_path}'")
    except Exception as e:
        print(f"Error cropping '{input_path}': {str(e)}")

# Get a list of subdirectories (folders) in the current folder
subdirectories = [d for d in os.listdir() if os.path.isdir(d)]

if not subdirectories:
    print("No subfolders found in the current folder.")
else:
    print("Available subfolders:")
    for i, subdirectory in enumerate(subdirectories, 1):
        print(f"{i}. {subdirectory}")

    try:
        # Ask the user to select a subfolder
        selection = int(input("Enter the number of the subfolder to crop images in: ")) - 1
        selected_subfolder = subdirectories[selection]

        # Define the cropping rectangle as (left, upper, right, lower)
        crop_box_for_theatre = (0, 170, 1900, 1000)  
        crop_box_for_normal = (100, 200, 1260, 860)    # Adjust the values as needed

        # Get a list of image files in the selected subfolder
        subfolder_path = os.path.join(os.getcwd(), selected_subfolder)
        image_files = [file for file in os.listdir(subfolder_path) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff'))]

        if not image_files:
            print("No image files found in the selected subfolder.")
        else:
            # Create a subfolder for cropped images within the selected subfolder
            cropped_folder = os.path.join(selected_subfolder, "cropped_images")
            os.makedirs(cropped_folder, exist_ok=True)

            # Crop each image and save it to the cropped folder
            for image_file in image_files:
                input_path = os.path.join(subfolder_path, image_file)
                output_path = os.path.join(cropped_folder, image_file)
                crop_image(input_path, output_path, crop_box_for_theatre)

            print("Cropping complete.")
    except (ValueError, IndexError):
        print("Invalid selection. Please enter a valid number.")
