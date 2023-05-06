import pyaudio
import wave
import keyboard
from time import perf_counter

pttKey = "a"

def recordAudio():
    chunk = 1024
    format = pyaudio.paInt16
    channels = 1
    rate = 44100

    p = pyaudio.PyAudio()

    stream = p.open(format=format, channels=channels, rate=rate, input=True,
                frames_per_buffer=chunk)
    print("started recording")

    frames = []
    seconds = 3
    for i in range(0, int(rate/chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    print("stopped recording")
    stream.stop_stream()
    stream.close()
    p.terminate

    wf = wave.open("output.wav", "wb")
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(format))
    wf.setframerate(rate)
    print(len(frames))
    wf.writeframes(b''.join(frames))
    wf.close() 

while(True):
    if(input() == pttKey):
        print("fard")
        break

print("larding")
#recordAudio()