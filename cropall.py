import os
from PIL import Image

# Function to get a list of image files in a folder
def get_image_files(folder_path):
    image_files = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
            image_files.append(os.path.join(folder_path, filename))
    return image_files

# Function to crop an image using specified coordinates
def crop_image(input_path, output_path, crop_box):
    try:
        with Image.open(input_path) as img:
            cropped_img = img.crop(crop_box)
            cropped_img.save(output_path)
        print(f"Cropped '{input_path}' and saved as '{output_path}'")
    except Exception as e:
        print(f"Error cropping '{input_path}': {str(e)}")

# Function to process images in a folder and crop them
def crop_images_in_folder(folder_path, crop_box):
    # Get a list of image files in the specified folder
    image_files = get_image_files(folder_path)

    if not image_files:
        print(f"No image files found in the folder: {folder_path}")
    else:
        # Create a subfolder for cropped images within the specified folder
        cropped_folder = os.path.join(folder_path, "cropped_images")
        os.makedirs(cropped_folder, exist_ok=True)

        # Crop each image and save it to the cropped folder
        for image_file in image_files:
            input_path = image_file
            output_path = os.path.join(cropped_folder, os.path.basename(image_file))
            crop_image(input_path, output_path, crop_box)

        print(f"Cropping complete in folder: {folder_path}")

# Function to process all subfolders recursively
def process_subfolders(root_folder, crop_box):
    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)
        if os.path.isdir(folder_path):
            crop_images_in_folder(folder_path, crop_box)


if __name__ == "__main__":
    # Get the current folder where the script is executed
    current_folder = "C:\\Users\\LENOVO\\Documents\\#My Second Brain\\1-Projects\\Notion"

    # Define the cropping rectangle as (left, upper, right, lower)
    crop_box = (0, 170, 1900, 1000)  # Adjust the values as needed

    # Call the function to process images in all subfolders and crop them
    process_subfolders(current_folder, crop_box)
