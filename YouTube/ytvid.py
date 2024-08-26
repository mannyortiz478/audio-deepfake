import os
from pytube import YouTube
from pydub import AudioSegment
from ffmpeg import input as ffmpeg_input

# Function to download and convert YouTube video to mp3
def download_youtube_as_mp3(youtube_url, output_path):
    yt = YouTube(youtube_url)
    video = yt.streams.filter(only_audio=True).first()
    audio_file_path = video.download(output_path=output_path, filename=yt.title)
    
    mp3_file_path = os.path.splitext(audio_file_path)[0] + '.mp3'
    
    # Convert to mp3 using ffmpeg through pydub
    audio = AudioSegment.from_file(audio_file_path)
    audio.export(mp3_file_path, format="mp3")
    
    # Remove the original video file
    os.remove(audio_file_path)
    return mp3_file_path

# Function to split mp3 file into 15 second intervals
def split_mp3_into_intervals(mp3_file_path, output_dir, interval_ms=18000):
    audio = AudioSegment.from_mp3(mp3_file_path)
    duration_ms = len(audio)
    file_name = os.path.splitext(os.path.basename(mp3_file_path))[0]
    
    for i in range(0, duration_ms, interval_ms):
        split_audio = audio[i:i + interval_ms]
        split_file_name = f"{file_name}_part{i//interval_ms}.mp3"
        split_file_path = os.path.join(output_dir, split_file_name)
        split_audio.export(split_file_path, format="mp3")

# Main function to process the input file
def process_youtube_links(input_file_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    with open(input_file_path, 'r') as file:
        youtube_links = file.readlines()
    
    for youtube_url in youtube_links:
        youtube_url = youtube_url.strip()
        if youtube_url:
            print(f"Processing: {youtube_url}")
            try:
                mp3_file_path = download_youtube_as_mp3(youtube_url, output_dir)
                split_mp3_into_intervals(mp3_file_path, output_dir)
                os.remove(mp3_file_path)  # Remove the original mp3 file after splitting
            except Exception as e:
                print(f"Failed to process {youtube_url}: {e}")

# Example usage
if __name__ == "__main__":
    input_file_path = 'vids.txt'  # Path to your input file with YouTube links
    output_dir = 'split'  # Directory to save the split mp3 files
    process_youtube_links(input_file_path, output_dir)