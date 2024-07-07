from pytube import YouTube
import os
import sys

def download_video(video_url):
  # Create a YouTube object
    yt = YouTube(video_url)
    
    try:
      # Get the highest resolution stream
      video_stream = yt.streams.get_highest_resolution()
      
      # Construct the output file path
      video_filename = yt.title + ".mp4"
      output_directory = os.getcwd()
      output_path = os.path.join(output_directory, video_filename)
      
      # Check if the video file already exists
      if os.path.exists(output_path):
          print(f"Video '{video_filename}' already exists. Skipping.")
      else:
          print(f"Downloading video: {video_filename}")
          video_stream.download(output_path=output_directory)
          print(f"Downloaded")
    except Exception as e:
      raise

if __name__=="__main__":
  for url in sys.argv[1:]:
    download_video(url)