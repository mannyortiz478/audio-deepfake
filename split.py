from pydub import AudioSegment
import os

def split_audio_file(input_file, output_dir):
    # Load the audio file
    audio = AudioSegment.from_file(input_file)
    
    # Calculate the midpoint of the audio file
    midpoint = len(audio) // 2
    
    # Split the audio into two parts
    first_half = audio[:midpoint]
    second_half = audio[midpoint:]
    
    # Get the base name of the input file without extension
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    
    # Define output file paths
    first_half_output = os.path.join(output_dir, f"{base_name}_part1.mp3")
    second_half_output = os.path.join(output_dir, f"{base_name}_part2.mp3")
    
    # Export the first half
    first_half.export(first_half_output, format="mp3")
    print(f"First half saved as {first_half_output}")
    
    # Export the second half
    second_half.export(second_half_output, format="mp3")
    print(f"Second half saved as {second_half_output}")

# Input audio file
input_file = "/home/em3923/combinedMilton.mp3"

# Output directory
output_dir = "/home/em3923/split_audio"

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

split_audio_file(input_file, output_dir)