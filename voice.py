from gtts import gTTS
import os


def speak(text: str):
    file = 'temp.mp3'
    tts = gTTS(text, lang='pt')
    tts.save(file)
    os.system(f'mpg123 {file}')
