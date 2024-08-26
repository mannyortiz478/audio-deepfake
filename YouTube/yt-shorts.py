import os
import yt_dlp
from pydub import AudioSegment

def download_youtube_short_as_mp3(link, output_path='downloads'):
    try:
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'quiet': True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        
        print(f"Downloaded and converted: {link}")
    except Exception as e:
        print(f"Failed to download {link}: {e}")

def download_shorts_from_file(file_path):
    with open(file_path, 'r') as file:
        links = file.readlines()
        for link in links:
            link = link.strip()
            if link:
                download_youtube_short_as_mp3(link)

if __name__ == "__main__":
    text_file_path = 'shorts_links.txt'  # Replace with your text file path
    download_shorts_from_file(text_file_path)