import os

# Directory containing the files
directory_path = r""

# Iterate through all files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".mp4"):
        # Generate new filename with ".mp3" extension
        new_filename = os.path.splitext(filename)[0] + ".mp3"
        
        # Construct full file paths
        old_filepath = os.path.join(directory_path, filename)
        new_filepath = os.path.join(directory_path, new_filename)
        
        # Rename the file
        os.rename(old_filepath, new_filepath)
        print(f"Renamed '{filename}' to '{new_filename}'")

print("File renaming complete!")
