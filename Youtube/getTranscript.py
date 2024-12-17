from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import sys

def get_video_id(url):
    """
    Extracts the video ID from a YouTube URL.
    """
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    else:
        raise ValueError("Invalid YouTube URL")

def save_transcript(video_id, filename="transcript.txt"):
    """
    Fetches the transcript for the given YouTube video ID and saves it to a file.
    """
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        formatter = TextFormatter()
        transcript_text = formatter.format_transcript(transcript_list)

        with open(filename, "w", encoding="utf-8") as file:
            file.write(transcript_text)
        print(f"Transcript saved to {filename}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <YouTube URL>")
    else:
        video_url = sys.argv[1]
        video_id = get_video_id(video_url)
        save_transcript(video_id)
