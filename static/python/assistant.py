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

# speak("Hello kaddu, Namaste Devi ji, Good Morning Sudha, how you amrutha, aur jadugar kya hal hai")
speak(" So how are you all! What say lets win this one!")