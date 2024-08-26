import os
import json
import torch
import logging
from tqdm import tqdm
from styletts2 import tts

# Setup logging
logging.basicConfig(filename='process.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Initialize the StyleTTS2 model
model_checkpoint_path = './epoch_2nd_00012.pth'
config_path = './config_ft.yml'

logging.info("Initializing StyleTTS2 model...")
if torch.cuda.is_available():
    my_tts = tts.StyleTTS2(model_checkpoint_path=model_checkpoint_path, config_path=config_path)
else:
    my_tts = None
    logging.error("CUDA not available. Exiting...")
    exit(1)

# Function to parse JSON file
def parse_json(json_path):
    audio_dict = {}
    try:
        with open(json_path, 'r') as file:
            json_data = json.load(file)
            for audiofile, text in json_data.items():
                audio_dict[audiofile] = text
    except Exception as e:
        logging.error(f"Failed to parse JSON file: {e}")
    return audio_dict

# Function to synthesize speech using StyleTTS2
def synthesize_speech(text, reference_audio_path, output_file):
    if my_tts:
        try:
            logging.info(f"Synthesizing text: {text}")
            my_tts.inference(text, reference_audio_path, output_wav_file=output_file)
            logging.info(f"Generated audio saved to: {output_file}")
        except IndexError as e:
            logging.error(f"IndexError during synthesis for text: {text} - {e}")
            log_error_file(output_file)
        except Exception as e:
            logging.error(f"Error during synthesis: {e}")
            log_error_file(output_file)
    else:
        logging.error("StyleTTS2 model not initialized.")

# Function to log error files
def log_error_file(file_path):
    with open('error_files.txt', 'a') as error_file:
        error_file.write(f"{file_path}\n")

# Function to process audio files with a progress bar
def process_audio_files(audio_dir, dst_dir, audio_dict, file_limit=None):
    # Count total files to process
    total_files = sum(len(files) for _, _, files in os.walk(audio_dir))
    files_processed = 0

    # Initialize tqdm progress bar
    with tqdm(total=total_files, desc="Processing audio files") as pbar:
        for root, _, files in os.walk(audio_dir):
            for file in files:
                if file_limit and files_processed >= file_limit:
                    return

                relative_path = os.path.relpath(os.path.join(root, file), audio_dir)
                reference_audio_path = os.path.join(root, file)
                dst_path = os.path.join(dst_dir, relative_path)
                os.makedirs(os.path.dirname(dst_path), exist_ok=True)

                key = os.path.basename(file)
                if key in audio_dict:
                    if not os.path.exists(dst_path):
                        text = audio_dict[key]
                        synthesize_speech(text, reference_audio_path, dst_path)
                        files_processed += 1
                    else:
                        logging.info(f"File already exists, skipping: {dst_path}")
                
                # Update progress bar
                pbar.update(1)

# Main execution block
if __name__ == "__main__":
    destination = 'volkanTTS_bona_deepfakes'
    filepath = 'bona_fide_audio/'
    json_path = 'bona_fide_asr.json'  # Update with your new JSON path if different
    file_limit = 3  # Limit to 3 files for testing

    logging.info("Parsing JSON file...")
    audio_dict = parse_json(json_path)
    if audio_dict and my_tts:
        logging.info("Starting to process audio files...")
        process_audio_files(filepath, destination, audio_dict, file_limit)
        logging.info("Processing completed.")
    else:
        logging.error("Error: JSON file parsing failed or StyleTTS2 model not initialized.")
