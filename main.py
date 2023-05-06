from AudioPlayer import playAudio
from DeepL import translate
from Narakeet import tts
from MicToAudioFile import audioListener
from WhisperDetection import whisperDetect

while (True):
    playAudio(13, tts(translate(whisperDetect(audioListener()), 'KO')))