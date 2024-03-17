from pytube import Playlist, YouTube
import os

# URL of the YouTube playlist
playlist_url = "https://www.youtube.com/playlist?list=PL3iN2vsqIoQRnw68IiF8FWx4JbdHwtc_t"

# Directory to save the downloaded videos
output_directory = getcwd()

# Create a Playlist object
playlist = Playlist(playlist_url)

# Iterate through each video in the playlist
for video_url in playlist.video_urls:
    print(f"Checking video: {video_url}")
    
    # Create a YouTube object
    yt = YouTube(video_url)
    
    # Get the highest resolution stream
    video_stream = yt.streams.get_highest_resolution()
    
    # Construct the output file path
    video_filename = yt.title + ".mp4"
    output_path = os.path.join(output_directory, video_filename)
    
    # Check if the video file already exists
    if os.path.exists(output_path):
        print(f"Video '{video_filename}' already exists. Skipping.")
    else:
        print(f"Downloading video: {video_filename}")
        video_stream.download(output_path=output_directory)
    
print("All videos checked/downloaded successfully!")
