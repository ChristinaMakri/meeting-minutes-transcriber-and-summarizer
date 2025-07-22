import torch
from transformers import pipeline, AutoProcessor, AutoModelForSpeechSeq2Seq

def transcribe_audio(audio_path):
    model_id = "openai/whisper-medium"
    model = AutoModelForSpeechSeq2Seq.from_pretrained(model_id, torch_dtype=torch.float16, use_safetensors=True)
    processor = AutoProcessor.from_pretrained(model_id)

    model.to("cuda")
    pipe = pipeline(
        "automatic-speech-recognition",
        model=model,
        tokenizer=processor.tokenizer,
        feature_extractor=processor.feature_extractor,
        torch_dtype=torch.float16,
        device="cuda"
    )
    result = pipe(audio_path)
    return result["text"]