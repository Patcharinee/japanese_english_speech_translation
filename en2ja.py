import speech_recognition as sr
from gtts import gTTS
import os
from googletrans import Translator
from pykakasi import kakasi
from time import sleep
import warnings
# warnings.filterwarnings("ignore", category=DeprecationWarning)


def speak_text(command):
    tts = gTTS(text=command, lang='ja')
    tts.save('speech.mp3')
    os.system('start speech.mp3')


translator = Translator()
kks = kakasi()
kks.setMode('J', 'H')  # Japanese to Kana
conv = kks.getConverter()


def speech_chat():
    # r = sr.Recognizer()
    r = sr.Recognizer(language='en')
    with sr.Microphone() as source:
        print(' ** Please Speak to me in English. I will translate it to Japanese for you **')
        audio = r.listen(source)

        try:
            text = r.recognize(audio)
            print(f'You said {text}')
            translated_text = translator.translate(text, dest='ja').text
            translated_text_kana = conv.do(translated_text)
            print('**********************************')
            print(f'Japanese: {translated_text}')
            print(f'Kana:     {translated_text_kana}')
            print(f'English   {text}')
            print('**********************************')
            speak_text(translated_text)

        except LookupError:
            print("Sorry, I couldn't recognize your voice")


keep_going = True

while keep_going:
    speech_chat()
    sleep(4)
