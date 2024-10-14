# VoiceNote for Business - Vaseegrah Veda 🌿

## Empowering Businesses to Thrive Through WhatsApp Voice Communication

Welcome to **VoiceNote for Business - Vaseegrah Veda**! 🌟 This project was crafted with love and dedication by **Sam Naveenkumar V❤️**, during his 2nd-year internship at Vaseegrah Veda, Tech Vaseegrah. This unpaid internship was not just a project but a **noble cause** to bridge the digital divide between rural communities and advanced tech solutions. With **VoiceNote**, clients can communicate their business needs through simple **WhatsApp voice notes**, allowing them to interact with businesses without visiting a website or an offline store.

### 🌟 Project Overview

**VoiceNote for Business** is a comprehensive solution created for **Vaseegrah Veda**, an **organic store**, which offers a revolutionary approach for businesses to handle customer queries and requirements, especially through **WhatsApp Business** voice messages. It allows customers to **speak** their **problems or requirements** in their **local vernacular language**, and the company's dedicated team, **Tech Vaseegrah**, handles the rest.

This project helps customers receive tailored product recommendations from Vaseegrah Veda, which align with their requirements, delivered back to them via a **personalized voice note** in their **local language**. The aim is to **simplify access** to products and services for rural customers, offering them a **seamless experience** without needing to step into an offline store.

---

## 🌐 Features of the Project

- **Multi-language support:** Works with any **vernacular language** spoken across the world.
- **WhatsApp Integration:** Handles **WhatsApp Business Accounts** seamlessly.
- **Automatic Translation:** Converts **voice messages** into **text** and **translates** them into English for internal processing.
- **Tech Vaseegrah Team:** A dedicated tech team processes customer queries and matches them with the appropriate products.
- **Text-to-Voice:** Replies to customer queries in their **original language** with the relevant product information via **voice note**.
- **Ease of Use for Rural Communities:** Built to help customers in **rural areas** interact with businesses **without visiting websites or stores**.
- **Cross-Platform:** This project is designed to work on **Windows**, **Mac**, and **Ubuntu** with support for **multiple OS** environments.
- **Premium GUI:** A beautiful, intuitive, and simple **Tkinter GUI** for seamless interaction.
  
---
## 🌍 Setting Up the Virtual Environment

1. **Install `virtualenv`** (if not already installed):
   ```bash
   pip install virtualenv
Create a virtual environment in your project directory:
 --On Windows:
    .\env\Scripts\activate
 -- On MacOS/Linux:
    source env/bin/activate

# Install the required dependencies:

pip install -r requirements.txt

# Download and install ffmpeg:

# Visit the official FFmpeg download page:
# https://ffmpeg.org/download.html

# Place your WhatsApp audio files in the Voice-Notes/Received directory.

## 🚀 Getting Started

### Prerequisites
Ensure you have the following installed on your system:
- Python 3.7+
- Tkinter
- SpeechRecognition library
- Googletrans library (for translation)
- `ffmpeg` for audio file conversion and handling
- Python packages: `pydub`, `gTTS`, `playsound`, etc.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/samnaveenkumaroff/VoiceNote-for-Business-Vaseegrah-Veda.git

---

## 🛠 Project Files Breakdown

### 1. `VoicetoText.py`
This script is the **core component** responsible for:
- Receiving **audio files** from **WhatsApp**.
- Converting **voice messages** into **text** using **Google Speech Recognition**.
- Supporting **multiple languages** like **Tamil, Hindi, Telugu, Malayalam, and English**, with dynamic **language detection** and translation to **English**.
- Saving the translated text into a **CSV file** (`VNText.csv`) for further product matching.
- Providing an elegant **Tkinter GUI** where the user can select the audio file, choose the language, and see the translated text directly on the interface.

### 2. `TexttoVoice.py`
This script handles the **reverse process**, where:
- The product description is translated back into the **customer's preferred language**.
- Converts the **translated text** into a **voice note** using text-to-speech conversion.
- Sends back the **reply** in the **original language** via **WhatsApp**, stored in the path `Voice-Notes/Sent`.

### 3. `VNText.csv`
This CSV file stores all **translated text** from customer voice messages along with:
- The **file path** of the original voice note.
- The **translated text** in English.
- The **language code** for later reference and response in the correct language.

### 4. `Voice-Notes` (Directory)
This directory contains two subfolders:
- **Received**: Stores the **incoming voice notes** from customers via WhatsApp.
- **Sent**: Stores the **response voice notes** generated and sent back to the customer.

### 5. `Images` (Directory)
Contains relevant assets like **logos** and **images** used in the **GUI**.

### 6. `ffmpeg-7.0.1` (Dependency)
The project depends on **ffmpeg** for efficient handling of audio files. This ensures smooth conversion between audio formats during speech recognition and text-to-voice operations.

---

## 🎨 Elegant Tkinter GUI

This project includes an incredibly **user-friendly** and **intuitive Tkinter GUI** that allows the Tech Vaseegrah team to:
- Easily **browse and select audio files**.
- Choose from a **dropdown menu** of supported languages.
- Display the **translated text** in real-time.
- View relevant product recommendations to assist customers efficiently.

The GUI also includes:
- The company name "**Vaseegrah Veda**" displayed elegantly at the top.
- The **company logo** for a premium, professional look.

---

## 🌟 Cross-Platform Support

This project works flawlessly on multiple operating systems:

### Windows:
- Simply run `VoicetoText.py` and follow the GUI prompts to select audio files and process them.
- Works seamlessly with WhatsApp Business API integration.

### MacOS:
- The GUI supports Mac with native Tkinter, providing a smooth user experience.
- Ensure ffmpeg is correctly installed using `brew install ffmpeg`.

### Ubuntu/Linux:
- Ideal for deployment on Linux-based servers or desktops.
- Tkinter and ffmpeg must be pre-installed.

---

## ❤️ Crafted with Love

This project was crafted with love and dedication by Sam Naveenkumar V❤️ during his 2nd-year internship at Vaseegrah Veda. This was an unpaid internship, undertaken with the belief that technology should connect people, especially in rural areas, and make businesses thrive using the power of vernacular language.

---

## Mission:
To build a bridge between villages and technology, and provide easy access to business products and services using the simplest form of communication — voice.

---

## 🔐 License

This project is licensed under the Apache 2.0 License — feel free to use, modify, and distribute this project for both personal and commercial purposes.

---

## ⭐ Acknowledgements
Special thanks to:
- Vaseegrah Veda for the opportunity to contribute to this noble project.
- The dedicated Tech Vaseegrah team for their support.
- All communities relying on WhatsApp for their business communications.
- **Sam Naveenkumar V❤️** — for contributing this powerful project for rural empowerment and business enhancement.

## 💬 Support & Feedback

For any queries or feedback, feel free to reach out to samnaveenkumaroff@gmail.com . Your support helps in connecting more rural areas with technology.

---


