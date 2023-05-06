# file path is python -u C:\Users\sihoc\Documents\GitHub\OC-Hackathon-Voice-Converter\Whisper-Detection.py
# python -u Whisper-Detection.py
import whisper
def whisperDetect(file):
    model = whisper.load_model("large")
    result = model.transcribe(file, fp16=False)
    return result['text']