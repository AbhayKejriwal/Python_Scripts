import sys
from pytube import YouTube

# Function to download YouTube video
def download_video(url):
    try:
        # Create a YouTube object with the provided URL
        yt = YouTube(url)

        # Get the highest resolution video stream
        stream = yt.streams.get_highest_resolution()

        # Download the video to the current directory
        stream.download()

        print(f'Video downloaded successfully: {yt.title}')
    except Exception as e:
        print(f'Error: {str(e)}')

if __name__ == '__main__':
    # Check if the URL is provided as a command line argument
    if len(sys.argv) < 2:
        print("Usage: python download_video.py <YouTube URL>")
        sys.exit(1)

    # Get the URL from the command line argument
    video_url = sys.argv[1]

    # Call the function to download the video
    download_video(video_url)
