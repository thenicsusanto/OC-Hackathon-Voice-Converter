import speech_recognition as sr

r = sr.Recognizer

with sr.AudioFile("output.mp3") as source:
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(text)
    except:
        print("Run again")