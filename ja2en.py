import speech_recognition as sr
from gtts import gTTS
import os
from googletrans import Translator
from pykakasi import kakasi
from time import sleep
import warnings
# warnings.filterwarnings("ignore", category=DeprecationWarning)


def speak_text(command):
    tts = gTTS(text=command, lang='en')
    tts.save('speech.mp3')
    if os.name == 'nt':  # For Windows
        os.system('start speech.mp3')
    else:  # For MacOS
        os.system('afplay speech.mp3')


translator = Translator()
kks = kakasi()
kks.setMode('J', 'H')  # Japanese to Kana
conv = kks.getConverter()


def speech_chat():
    # r = sr.Recognizer()
    r = sr.Recognizer(language='ja')
    with sr.Microphone() as source:
        print(' ** Please Speak to me in Japanese. I will translate it to English for you **')
        audio = r.listen(source)

        try:
            text = r.recognize(audio)
            print(f'You said {text}')
            translated_text = translator.translate(text, dest='en').text
            translated_text_kana = conv.do(text)
            print('**********************************')
            print(f'English: {translated_text}')
            print(f'Kana:    {translated_text_kana}')
            print(f'Japanese {text}')
            print('**********************************')
            speak_text(translated_text)

        except LookupError:
            print("Sorry, I couldn't recognize your voice")


keep_going = True

while keep_going:
    speech_chat()
    sleep(4)
