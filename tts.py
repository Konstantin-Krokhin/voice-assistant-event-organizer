from TTS.api import TTS
import os

# Download and load a Coqui model
# "tts_models/en/ljspeech/tacotron2-DDC" is simple & fast
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")

def synthesize(text: str, out_file: str = "output.wav"):
    tts.tts_to_file(text=text, file_path=out_file)
    return out_file
