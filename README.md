# Meeting Minutes Generator with Translation & Topic Extraction

## Description
This project provides an application that automatically transcribes English meeting audio recordings, generates professional meeting minutes, extracts key discussion topics, and translates the minutes into Greek.

It uses open-source models only (Whisper for transcription, Mistral or similar for minutes generation, KeyBERT for topic extraction, and MarianMT for translation) and is built with a Gradio UI for easy interaction.

---

## Features
- **Audio Upload**: Upload `.mp3` or `.wav` audio files containing English meetings.
- **Transcription**: Automatic speech-to-text transcription.
- **Minutes Generation**: Generate professional meeting minutes including summary, discussion points, takeaways, and action items.
- **Topic Extraction**: Extract key topics from the meeting.
- **Translation**: Automatically translate meeting minutes to Greek.

---

## Usage

### 1. Installation

Install required packages with:

```bash
pip install -r requirements.txt
```

### 2. Run the app
```bash
python gradio_app.py
```

### 3. How to Use
-The Gradio UI will open in your browser.  
-Upload your meeting audio file.  
-View the transcript, English minutes, extracted topics, and Greek translation.  
