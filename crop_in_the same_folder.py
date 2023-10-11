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

# Define the cropping rectangle as (left, upper, right, lower)
crop_box_for_theatre = (0, 170, 1900, 1000)  
crop_box_for_normal = (100, 200, 1260, 860)  
# Adjust the values as needed

# Get a list of image files in the current folder
image_files = [file for file in os.listdir() if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff'))]

if not image_files:
    print("No image files found in the current folder.")
else:
    # Create a subfolder for cropped images
    cropped_folder = "cropped_images"
    os.makedirs(cropped_folder, exist_ok=True)

    # Crop each image and save it to the cropped folder
    for image_file in image_files:
        input_path = os.path.join(os.getcwd(), image_file)
        output_path = os.path.join(cropped_folder, image_file)
        crop_image(input_path, output_path, crop_box_for_theatre)

print("Cropping complete.")
