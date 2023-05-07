from AudioPlayer3 import playAudio
from DeepL import translate
from Narakeet import tts
from MicToAudioFile import audioListener
from WhisperDetection import whisperDetect

while (True):
    playAudio(tts(translate(whisperDetect(audioListener()), 'JA'), 'Yuriko', 'fast'))
# Korean Chae-Won
# Japanese Yuriko