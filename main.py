from AudioPlayer import playAudio
from DeepL import translate
from Narakeet import tts
from MicToAudioFile import audioListener
from WhisperDetection import whisperDetect
from menu import select_language

# select_language()
while (True):
    language = 'KO'
    print(language)
    person = "Chae-Won"
    if (language == "ES"): 
        person = "Ignacio"
    elif (language == "KO"): 
        person = "Chae-Won"
    elif (language == "JA"): 
        person = "Yuriko"
    elif (language == "ZH"): 
        person = "Hai"
    elif (language == "ID"): 
        person = "Budiwati"
    elif (language == "RU"): 
        person = "Vladimir"
    elif (language == "FR"): 
        person = "Marion" 
    playAudio(tts(translate(whisperDetect(audioListener()), language), person, 'fast'))
# Korean Chae-Won KO
# Japanese Yuriko JA
# Chinese Hai ZH
# English 