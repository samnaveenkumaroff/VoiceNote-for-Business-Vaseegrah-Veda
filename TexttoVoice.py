import csv
import os
from googletrans import Translator
from gtts import gTTS

# Initialize translator
translator = Translator()

# Function to translate text to preferred language and convert to audio
def text_to_voice(csv_file_path, output_folder):
    # Read the CSV file
    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 3:
                audio_file_path, translated_text, lang_code = row
                try:
                    # Translate text back to the preferred language
                    translated_back_text = translator.translate(translated_text, dest=lang_code).text
                    print(f"Original Translated Text: {translated_text}")
                    print(f"Translated Back Text: {translated_back_text}")

                    # Convert text to speech
                    tts = gTTS(translated_back_text, lang=lang_code)
                    output_audio_path = os.path.join(output_folder, os.path.basename(audio_file_path).replace('.wav', '_translated.wav'))
                    tts.save(output_audio_path)
                    print(f"Audio saved to {output_audio_path}")
                except Exception as e:
                    print(f"Error in translation or TTS: {e}")
            else:
                print(f"Invalid row format: {row}")

# Paths
csv_file_path = r"VNText.csv"
output_folder = r"Voice-Notes/Sent"

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Translate text back to preferred language and convert to audio
text_to_voice(csv_file_path, output_folder)
