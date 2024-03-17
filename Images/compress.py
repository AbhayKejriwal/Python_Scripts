import os
from PIL import Image

# Function to compress an image
def compress_image(input_path, output_path, quality=85):
    try:
        with Image.open(input_path) as img:
            img.save(output_path, optimize=True, quality=quality)
        print(f"Compressed '{input_path}' and saved as '{output_path}'")
    except Exception as e:
        print(f"Error compressing '{input_path}': {str(e)}")

# Get a list of image files in the current folder
image_files = [file for file in os.listdir() if file.lower().endswith('.png')]

if not image_files:
    print("No image files found in the current folder.")
else:
    # Create a subfolder for compressed images
    compressed_folder = "compressed_images"
    os.makedirs(compressed_folder, exist_ok=True)

    # Set the compression quality (adjust as needed)
    compression_quality = 85  # You can change this value (0-100) to control the compression level

    # Compress each image and save it to the compressed folder
    for image_file in image_files:
        input_path = os.path.join(os.getcwd(), image_file)
        output_path = os.path.join(compressed_folder, image_file)
        compress_image(input_path, output_path, compression_quality)

print("Compression complete.")
