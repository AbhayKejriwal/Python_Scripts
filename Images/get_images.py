import os
from PIL import Image

def load_images_as_objects(folder_path):
	image_objects = []

	# Get a list of image files in the current folder
	image_files = [file for file in os.listdir(folder_path) if file.lower().endswith('.png')]

	if os.path.isdir(folder_path):
	for file in image_files:
		image_path = os.path.join(folder_path, file)
		image = Image.open(image_path)
		image_objects.append(image)

	return image_objects

if __name__ =="__main__":
	folder_path = " "  # Specify the folder path you want to process
	image_objects = load_images_as_objects(folder_path)

	for image in image_objects:
    
