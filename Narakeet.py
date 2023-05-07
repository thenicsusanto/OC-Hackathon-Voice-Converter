apikey = 'ENTER KEY HERE'
import requests

def tts(text, voice, speed):
    url = f'https://api.narakeet.com/text-to-speech/mp3?voice={voice}'
    # text = '(voice-speed: ' + speed + ') ' + text
    options = {
        'headers': {
            'Accept': 'application/octet-stream',
            'Content-Type': 'text/plain',
            'x-api-key': apikey,
        },
        'data': text.encode('utf8')
    }
    with open('output.mp3', 'wb') as f:
        f.write(requests.post(url, **options).content)
    print("TTS output to output.wav with voice " + voice)
    return 'output.mp3'
