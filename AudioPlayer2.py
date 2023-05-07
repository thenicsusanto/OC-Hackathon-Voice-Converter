import vlc
def playAudio5(fileName):
    p = vlc.MediaPlayer(fileName)
    p.play()

playAudio5("output.mp3")