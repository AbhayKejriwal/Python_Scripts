from pytube import YouTube, exceptions, request
import os
import sys
import requests
from http.cookiejar import MozillaCookieJar

def load_cookies(cookie_file):
    # Load cookies from the file using MozillaCookieJar
    cj = MozillaCookieJar(cookie_file)
    cj.load(ignore_discard=True, ignore_expires=True)
    session = requests.Session()
    session.cookies.update(cj)
    return session

def download_video(video_url, session):
    # Function to replace pytube's request function with a session with cookies
    def request_func(url, *args, **kwargs):
        response = session.get(url, *args, **kwargs)
        response.raise_for_status()
        return response.content

    # Patch the pytube request to use our custom request function
    request.default_range_request = request_func
    request.default_retry = request_func
    request._execute_request = request_func

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
            print("Downloaded")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    cookie_file = os.path.join(os.getcwd(), "ytcookies.txt")  # Ensure this path is correct
    session = load_cookies(cookie_file)
    for url in sys.argv[1:]:
        download_video(url, session)