import pyaudio
import wave

def playAudio(audio_file, device_index):
    chunk = 1024

    # Open the audio file
    audio = wave.open(audio_file, 'rb')

    # Initialize PyAudio
    p = pyaudio.PyAudio()

    # Open the audio stream
    stream = p.open(format=p.get_format_from_width(audio.getsampwidth()),
                    channels=audio.getnchannels(),
                    rate=audio.getframerate(),
                    output=True,
                    output_device_index=device_index)

    # Read data from the audio file and play it
    data = audio.readframes(chunk)
    while data:
        stream.write(data)
        data = audio.readframes(chunk)

    # Cleanup
    stream.stop_stream()
    stream.close()
    p.terminate()

    audio.close()

playAudio("output.mp3", 13)