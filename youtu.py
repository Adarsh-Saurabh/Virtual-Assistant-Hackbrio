import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)
    text1 = r.recognize_google(audio)
    print(text1)
    try:
        text = r.recognize_google(audio)
        print("working on .........")
        print(text)
    except:
        print("error")