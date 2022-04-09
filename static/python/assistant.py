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

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print('Exception: ' + str(e))

    return said

# # speak("Hello kaddu, Namaste Devi ji, Good Morning Sudha, how you amrutha, aur jadugar kya hal hai")
# text = get_audio().lowercase()
speak("Hello ") 

get_audio()

# if "hello" in text:
#     speak("Hello Adarsh how are you")














# def main():
#     """Shows basic usage of the Google Calendar API.
#     Prints the start and name of the next 10 events on the user's calendar.
#     """
#     creds = None
#     # The file token.json stores the user's access and refresh tokens, and is
#     # created automatically when the authorization flow completes for the first
#     # time.
#     if os.path.exists('token.json'):
#         creds = Credentials.from_authorized_user_file('token.json', SCOPES)
#     # If there are no (valid) credentials available, let the user log in.
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 'credentials.json', SCOPES)
#             creds = flow.run_local_server(port=0)
#         # Save the credentials for the next run
#         with open('token.json', 'w') as token:
#             token.write(creds.to_json())

#     try:
#         service = build('calendar', 'v3', credentials=creds)

#         # Call the Calendar API
#         now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
#         print('Getting the upcoming 10 events')
#         events_result = service.events().list(calendarId='primary', timeMin=now,
#                                               maxResults=10, singleEvents=True,
#                                               orderBy='startTime').execute()
#         events = events_result.get('items', [])

#         if not events:
#             print('No upcoming events found.')
#             return

#         # Prints the start and name of the next 10 events
#         for event in events:
#             start = event['start'].get('dateTime', event['start'].get('date'))
#             print(start, event['summary'])

#     except HttpError as error:
#         print('An error occurred: %s' % error)


# if __name__ == '__main__':
#     main()