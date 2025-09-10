import whisper

# Load small Whisper model (fast & free)
model = whisper.load_model("small")

def transcribe(audio_file: str) -> str:
    result = model.transcribe(audio_file)
    return result["text"]
