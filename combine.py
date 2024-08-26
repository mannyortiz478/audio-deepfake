# Combining multiple small audio files, into making it one giant combined file for syntheszing

# You can alter the script so that only a certain amount of files, not all of them

from pydub import AudioSegment
import os

def combine_audio_files_from_directory(directory, output_file):
    # List all audio files (MP3 and WAV) in the directory
    input_files = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith(('.mp3', '.wav'))]
    
    # Sort the files if you want them in a specific order
    input_files.sort()
    
    # Create an empty audio segment
    combined = AudioSegment.empty()
    
    # Iterate through each file in the list
    for file in input_files:
        # Load the audio file based on its extension
        if file.endswith('.mp3'):
            audio = AudioSegment.from_mp3(file)
        elif file.endswith('.wav'):
            audio = AudioSegment.from_wav(file)
        # Add the audio file to the combined audio segment
        combined += audio
    
    # Export the combined audio segment to a file
    combined.export(output_file, format="mp3")
    print(f"Combined file saved as {output_file}")

# Directory containing input audio files
directory = "/home/em3923/VokanTTS_bona/bona_fide_audio/Bill Clinton"

# Output MP3 file
output_file = "/home/em3923/combinedClinton.mp3"

combine_audio_files_from_directory(directory, output_file)