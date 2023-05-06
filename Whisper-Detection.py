# file path is python -u C:\Users\sihoc\Documents\GitHub\OC-Hackathon-Voice-Converter\Whisper-Detection.py
# python -u Whisper-Detection.py
import whisper
def whisperDetect():
    model = whisper.load_model("base")
    result = model.transcribe("audio/TestAudio.wav", fp16=False)
    print(result['text'])

whisperDetect()