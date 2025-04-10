# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 11:45:38 2025

@author: maryt
"""
#importing all the necessary libraries
from textblob import TextBlob #TextBlob helps with sentaimental analysis in English
#google text to Speech librarary
from gtts import gTTS #can be used for basic level sentence translations 
import os
import random
import time

# Make sure folders exist (auto-create if missing)
os.makedirs("Input", exist_ok=True)
os.makedirs("Output", exist_ok=True)


# Step 1: Get input 
#text = input("Enter a sentence from the story: ")
'''
story = [
    "I love pandas!",
    "They are calm and kind.",
    "But sometimes they get scared during storms.",
    "They still help each other and stay strong.",
    "Everything becomes peaceful again."
]

'''
'''
# Read story lines from a text file
with open("story.txt", "r", encoding="utf-8") as file:
    story = [line.strip() for line in file if line.strip()]

'''
with open("Input/story.txt", "r", encoding="utf-8") as file:
    story = [line.strip() for line in file if line.strip()]

# Step 2: Analyze sentiment
'''
blob = TextBlob(text)
polarity = blob.sentiment.polarity

if polarity > 0.2:
    emotion = "positive"
elif polarity < -0.2:
    emotion = "negative"
else:
    emotion = "neutral"

print(f"Detected Emotion: {emotion} (Polarity: {polarity})")
'''
def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.2:
        return "positive"
    elif polarity < -0.2:
        return "negative"
    else:
        return "neutral"


# Step 3: Speak the sentence with emotion emoji
'''
def speak(text, emotion):
    if emotion == "positive":
        text = "😊 " + text
    elif emotion == "negative":
        text = "😟 " + text
    else:
        text = "😐 " + text

    tts = gTTS(text=text, lang='en')
    filename = f"output_{random.randint(1000, 9999)}.mp3"
    tts.save(filename)
    os.system(f"start {filename}")  # For Windows

speak(text, emotion)
'''

'''
def speak(text, emotion):
    if emotion == "positive":
        text = "Smile, " + text
    elif emotion == "negative":
        text = "Hmm, " + text
    else:
        text = "Okay, " + text

    tts = gTTS(text=text, lang='en')
    filename = f"line_{random.randint(1000,9999)}.mp3"
    tts.save(filename)
    os.system(f"start {filename}")  # Use 'afplay' or 'xdg-open' on macOS/Linux
    time.sleep(4)
'''


def speak(text, emotion):
    if emotion == "positive":
        text = "Smile, " + text
    elif emotion == "negative":
        text = "Hmm, " + text
    else:
        text = "Okay, " + text

    tts = gTTS(text=text, lang='en')
    filename = f"Output/line_{random.randint(1000,9999)}.mp3"
    tts.save(filename)
    os.system(f"start {filename}")
    time.sleep(4)


#Loop through story
for line in story:
    print(f"\nStory Line: {line}")
    emotion = analyze_sentiment(line)
    print(f"Detected Emotion: {emotion}")
    speak(line, emotion)
