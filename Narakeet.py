apikey = 'Sk86nNAHbJ8VGGGWREMkk2Fc1IUh1Xga50aVDVvB'
voice = 'Chae-Won'
url = f'https://api.narakeet.com/text-to-speech/mp3?voice={voice}'
import requests

def tts(text):
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
    print("TTS output to output.mp3 with voice " + voice)
    return 'output.mp3'