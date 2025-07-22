import gradio as gr
from tools import transcribe_audio
from prompts import generate_minutes
from topics import extract_topics
from translate import translate_text

def process_audio(file):
    transcript = transcribe_audio(file)
    minutes_en = generate_minutes(transcript)
    topics = extract_topics(minutes_en)
    minutes_el = translate_text(minutes_en, target_lang="el")
    return transcript, minutes_en, topics, minutes_el

iface = gr.Interface(
    fn=process_audio,
    inputs=gr.Audio(type="filepath", label="🎙️ Upload meeting audio (.mp3/.wav)"),
    outputs=[
        gr.Textbox(label="📝 Transcript"),
        gr.Textbox(label="📄 Minutes (English)"),
        gr.JSON(label="🧠 Extracted Topics"),
        gr.Textbox(label="📑 Μετάφραση στα Ελληνικά"),
    ],
    title="Meeting Minutes Generator with Translation & Topics",
    description="🎧 Upload an English meeting recording to get auto-generated minutes, topics, and Greek translation."
)

if __name__ == "__main__":
    iface.launch()