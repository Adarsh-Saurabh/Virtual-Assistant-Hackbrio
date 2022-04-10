import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS




def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)
        said= ""
        # speak()
        print(said)

        try:
            said = r.recognize_google(audio)
            print(said)
            spear(said)
        except Exception as e:
            print('Exception: ' + str(e))

    return said

# # speak("Hello kaddu, Namaste Devi ji, Good Morning Sudha, how you amrutha, aur jadugar kya hal hai")
# text = get_audio().lowercase()
speak("Hello ") 

# get_audio()

# # Audio to text
# text = get_audio().lower()
# # audio to text function using speech recognition

