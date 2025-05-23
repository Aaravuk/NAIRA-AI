import pywhatkit
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os
from datetime import timedelta
from datetime import datetime

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
# rate = engine.getProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Please Say that again...")
        return "None"
    return query

strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now() + timedelta(minutes=2)).strftime("%H"))

def sendMessage():
    speak("who do you want to send message to?")
    a = int(input('''Person 1 - 1
                Person 2 - 2'''))
    if a == 1:
        speak("What's the message you want to send?")
        message = str(input("Enter the message- "))
        pywhatkit.sendwhatmsg("+91**********", message, time_hour = strTime, time_min = update)
    elif a == 2:
        pass