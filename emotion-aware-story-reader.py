# -*- coding: utf-8 -*-
"""
Optimized: Emotion-Aware Multilingual Story Reader
Author: marytessjoseph

- Validates input
- Efficient gTTS + cleanup
- Auto-deletes audio after use
- User-friendly error handling
"""

import os
import hashlib
from gtts import gTTS
from deep_translator import GoogleTranslator
from textblob import TextBlob
from playsound import playsound

# Supported languages
supported_langs = {
    "en": "English", "hi": "Hindi", "ml": "Malayalam", "fr": "French",
    "es": "Spanish", "de": "German", "it": "Italian", "ta": "Tamil", "te": "Telugu"
}

# Create folders if they don't exist
os.makedirs("Input", exist_ok=True)
os.makedirs("Output", exist_ok=True)

# Clean old audio files
for file in os.listdir("Output"):
    if file.endswith(".mp3"):
        os.remove(os.path.join("Output", file))

# Helper: Get validated user input
def get_language_choice():
    print("Select the language you want to read and hear the story in:")
    for code, name in supported_langs.items():
        print(f"{code} → {name}")
    lang = input("Enter language code (e.g., ml): ").strip()
    if lang not in supported_langs:
        print("Invalid language code.")
        exit()
    return lang

# Helper: List stories and get selection
def select_story():
    story_files = [f for f in os.listdir("Input") if f.endswith(".txt")]
    if not story_files:
        print("No story files found in the Input folder.")
        exit()

    print("\nAvailable stories:")
    story_options = []
    for i, file in enumerate(story_files):
        src_code = file.split("_")[-1].replace(".txt", "")
        src_lang = supported_langs.get(src_code, "Unknown")
        print(f"{i + 1}. {file} (written in {src_lang})")
        story_options.append((file, src_code))

    try:
        choice = int(input("Select story number: ")) - 1
        if choice < 0 or choice >= len(story_options):
            raise ValueError
    except ValueError:
        print("Invalid selection.")
        exit()

    return story_options[choice]

# Helper: Analyze sentiment from English translation
def analyze_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.2:
        return "positive"
    elif polarity < -0.2:
        return "negative"
    return "neutral"

# Helper: Speak the sentence and clean up
def get_filename_from_text(text):
    # Generate a unique filename based on the text content
    hash_object = hashlib.md5(text.encode())
    return f"Output/{hash_object.hexdigest()}.mp3"

def speak(text, emotion, lang):
    prefix = {
        "positive": "Smile, ",
        "negative": "Hmm, ",
        "neutral": "Okay, "
    }.get(emotion, "")
    speech = prefix + text
    filename = get_filename_from_text(speech)

    try:
        if not os.path.exists(filename):
            gTTS(text=speech, lang=lang).save(filename)
        playsound(filename)
    except Exception as e:
        print(f"Speech Error: {e}")


# --- Main program ---
target_lang = get_language_choice()
story_file, source_lang = select_story()
story_path = os.path.join("Input", story_file)

# Read the selected story
with open(story_path, "r", encoding="utf-8") as f:
    story = [line.strip() for line in f if line.strip()]

# Process each sentence
for line in story:
    try:
        # Translate to English for sentiment detection
        line_en = GoogleTranslator(source=source_lang, target='en').translate(line)
        emotion = analyze_sentiment(line_en)

        # Translate to target language for playback
        line_out = GoogleTranslator(source=source_lang, target=target_lang).translate(line)

        print(f"\nOriginal: {line}")
        print(f"Translated: {line_out}")
        print(f"Detected Emotion: {emotion}")

        speak(line_out, emotion, target_lang)

    except Exception as e:
        print(f"Error processing line: {e}")
