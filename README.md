# Emotion-Aware Story Reader

**Emotion-Aware Story Reader** is a Python-based NLP tool that reads stories aloud and detects the emotional tone of each sentence. Designed to support neurodiverse children, it adapts how it speaks based on the sentiment detected (positive, negative, or neutral), using TextBlob and Google Text-to-Speech.

> **One-liner**: A Python-based NLP tool that reads stories aloud with emotion-aware voice feedback to support neurodiverse children.


## 🚀 Features

- 📖 Reads story text line by line from a `.txt` file
- 🧠 Detects sentiment using TextBlob
- 🗣️ Speaks each line aloud with emotional tone using Google TTS
- 💬 Uses friendly emotional expressions (like “Smile,” “Hmm,” “Okay”)
- 🌱 Project is under active development with plans to expand


## 🛠️ Technologies Used

- Python 3.x
- [TextBlob](https://textblob.readthedocs.io/en/dev/) – for sentiment analysis
- [gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/) – for converting text to speech
- Optionally uses `os.system()` for audio playback


## 📂 Files Included

- `emotion_reader.py` – Main Python script
- `story.txt` – Sample input story file (edit or replace as needed)
- `README.md` – Project documentation


## 📌 Setup Instructions

1. Clone the repository or download the files.
2. Install dependencies:

```
pip install textblob gtts
python -m textblob.download_corpora
```

# Run the script in your preferred IDE (e.g., Spyder):
```
python emotion_reader.py
```

Make sure your `story.txt` file is in the same folder as the script.

## 🧩 Future Enhancements

- 🌍 Multilingual story support and translation
- 🎨 Graphical interface using Tkinter or Streamlit
- 🎭 Emotion-based voice pitch/speed variation
- 📚 Interactive story builder for kids and educators



## 🧑‍💻 Author

Developed with ❤️ by [marytessjoseph](https://github.com/marytessjoseph)


## 📄 License
```
This project is open source and available under the [MIT License](LICENSE).
```


Let me know if you'd like a matching `LICENSE` file (MIT or any other), or if you'd like to personalize the author section with a short bio or email! 😊
