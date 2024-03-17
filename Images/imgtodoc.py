import os
from docx import Document
from docx.shared import Inches
from PIL import Image

# Function to get a list of image files in a folder
def get_image_files(folder_path):
    image_files = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
            image_files.append(os.path.join(folder_path, filename))
    return image_files

# Function to create a Word document with images (keeping original aspect ratio)
def create_word_document(images, output_folder, root_folder):
    doc = Document()

    for image_path in images:
        # Open the image and get its original width and height
        with Image.open(image_path) as img:
            width, height = img.size

        # Calculate the width and height for the image in inches while maintaining the aspect ratio
        max_width = 6.0  # Maximum width for the image in inches
        ratio = max_width / width
        new_width = max_width
        new_height = height * ratio

        doc.add_picture(image_path, width=Inches(new_width), height=Inches(new_height))

    output_file = os.path.join(root_folder, os.path.basename(output_folder) + ".docx")
    doc.save(output_file)
    print(f"Word document '{output_file}' created successfully.")

def process_subfolders(root_folder):
    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)
        if os.path.isdir(folder_path):
            image_files = get_image_files(folder_path)
            if image_files:
                create_word_document(image_files, folder_path, root_folder)
            else:
                print(f"No image files found in sub-folder: {folder_path}")

if __name__ == "__main__":
    current_folder = os.getcwd()  # Get the current folder where the script is executed
    process_subfolders(current_folder)
