import speech_recognition as sr
from googletrans import Translator
import os
import csv
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

# Initialize translator
translator = Translator()

# Function to convert voice note to English text and translate
def voice_note_to_text_and_translate(audio_file_path, lang_code):
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Recognize the speech in the audio file
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)

        # Attempt to recognize speech with specified language
        try:
            recognized_text = recognizer.recognize_google(audio_data, language=lang_code)
            print(f"Recognized Text: {recognized_text}")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")
            return None, lang_code
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None, lang_code

        # Translate to English if the recognized text is not in English
        if lang_code.lower() != "en":
            try:
                translated_text = translator.translate(recognized_text, src=lang_code, dest="en").text
                print(f"Translated Text: {translated_text}")
                return translated_text, lang_code
            except Exception as e:
                print(f"Translation error: {e}")
                return None, lang_code
        else:
            print(f"Text already in English: {recognized_text}")
            return recognized_text, lang_code

# Function to handle GUI creation and interaction
def create_gui():
    def browse_file():
        file_path = filedialog.askopenfilename(
            title="Select an audio file",
            filetypes=[("Audio Files", "*.wav *.mp3 *.m4a *.flac")]
        )
        file_path_var.set(file_path)

    def submit():
        selected_language = language_var.get()
        language_code_map = {
            "English": "en",
            "Tamil": "ta",
            "Hindi": "hi",
            "Telugu": "te",
            "Malayalam": "ml"
        }
        language_code = language_code_map.get(selected_language, "en")
        
        audio_file_path = file_path_var.get()
        if not os.path.exists(audio_file_path):
            raise FileNotFoundError(f"The file {audio_file_path} does not exist")

        # Recognize speech and translate to English
        translated_text, lang_code = voice_note_to_text_and_translate(audio_file_path, language_code)
        if translated_text:
            print(f"Final Translated Text: {translated_text}")

            # Display translated text in GUI
            translated_text_var.set(translated_text)

            # Save the translated text to a CSV file
            csv_file_path = r"VNText.csv"
            with open(csv_file_path, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([audio_file_path, translated_text, lang_code])
            print(f"Translated text saved to {csv_file_path}")
        else:
            print("Failed to recognize and translate speech.")

    root = tk.Tk()
    root.title("Vaseegrah Veda Voice Note Translator")

    # Company name and logo
    company_label = tk.Label(root, text="Vaseegrah Veda", font=("Helvetica", 16))
    company_label.pack(pady=10)
    logo = tk.PhotoImage(file=r"Images/Logo.png")  # Update the path to your logo file
    logo_label = tk.Label(root, image=logo)
    logo_label.pack(pady=10)

    # Language selection
    language_label = tk.Label(root, text="Select Preferred Language:", font=("Helvetica", 12))
    language_label.pack(pady=5)
    language_var = tk.StringVar()
    language_dropdown = ttk.Combobox(root, textvariable=language_var)
    language_dropdown['values'] = ("English", "Tamil", "Hindi", "Telugu", "Malayalam")
    language_dropdown.current(0)  # Set default to English
    language_dropdown.pack(pady=5)

    # File path entry with browse button
    file_path_label = tk.Label(root, text="Select Audio File:", font=("Helvetica", 12))
    file_path_label.pack(pady=5)
    file_path_var = tk.StringVar()
    file_path_entry = tk.Entry(root, textvariable=file_path_var, width=50)
    file_path_entry.pack(pady=5)
    browse_button = tk.Button(root, text="Browse", command=browse_file)
    browse_button.pack(pady=5)

    # Translated text display
    translated_text_var = tk.StringVar()
    translated_text_label = tk.Label(root, textvariable=translated_text_var, wraplength=400, justify='left')
    translated_text_label.pack(pady=10)

    # Submit button
    submit_button = tk.Button(root, text="Submit", command=submit)
    submit_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
