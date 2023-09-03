from moviepy.editor import VideoFileClip
import os

# Directory containing the MP4 files
input_directory = r"C:\Users\LENOVO\Music\Cosmic"

# Directory to save the converted MP3 files
output_directory = r"C:\Users\LENOVO\Desktop\Cosmic"

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Iterate through each file in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith(".mp4"):
        input_path = os.path.join(input_directory, filename)
        
        # Construct the output file path with a .mp3 extension
        output_filename = os.path.splitext(filename)[0] + ".mp3"
        output_path = os.path.join(output_directory, output_filename)
        
        print(f"Converting: {input_path} -> {output_path}")
        
        # Load the MP4 video and convert it to MP3
        video_clip = VideoFileClip(input_path)
        video_clip.audio.write_audiofile(output_path)
        
        print("Conversion complete!")

print("All files converted successfully!")
