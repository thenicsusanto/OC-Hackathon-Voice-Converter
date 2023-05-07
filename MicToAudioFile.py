import pyaudio
import wave
import keyboard

audioFileName = 0

def audioListener():
    chunk = 1024
    format = pyaudio.paInt16
    channels = 1
    rate = 44100

    audio = pyaudio.PyAudio()

    stream = audio.open(format=format, channels=channels, rate=rate, input=True,
                frames_per_buffer=chunk)

    frames = []

    global audioFileName
    while(True): #checks first time user pushes to talk
        if(keyboard.is_pressed('a')):
            break

    while(True): #checks if the user is still hitting the a key
        if(keyboard.is_pressed('a')): #if he is, data and frams are read
            data = stream.read(chunk)
            frames.append(data)
        else: #if user lets go of a key it stops the stream and creates an audio file
            stream.stop_stream()
            stream.close()
            audio.terminate()

            wave_file = wave.open('recorded_audio' + str(audioFileName) + '.wav', 'wb')
            wave_file.setnchannels(channels)
            wave_file.setsampwidth(audio.get_sample_size(format))
            wave_file.setframerate(rate)
            wave_file.writeframes(b''.join(frames))
            wave_file.close()

            frames.clear()
            
            print('recorded_audio' + str(audioFileName) + '.wav')
            val = 'recorded_audio' + str(audioFileName) + '.wav'
            audioFileName += 1
            return val