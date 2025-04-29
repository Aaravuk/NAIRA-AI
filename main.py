import pyttsx3
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
import datetime
import os
import random
import pyautogui

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 5)

    try:
        print("Understanding...")
        query = r.recognize_google(audio, language="en-in")
        print(f"You said: {query}\n")
    except sr.UnknownValueError:
        print("Could not understand. Please try again.")
        return "None"
    except sr.RequestError:
        print("Could not request results. Check your network connection.")
        return "None"
    return query.lower()

def set_alarm(query):
    try:
        with open("Alarmtext.txt", "a") as time_file:
            time_file.write(query + "\n")
        os.startfile("alarm.py")
    except Exception as e:
        print(f"Error setting alarm: {e}")

def fetch_temperature(location):
    try:
        url = f"https://www.google.com/search?q=temperature in {location}"
        response = requests.get(url)
        data = BeautifulSoup(response.text, "html.parser")
        temp = data.find("div", class_="BNeawe").text
        return temp
    except Exception as e:
        print(f"Error fetching temperature: {e}")
        return None

def main():
    while True:
        query = take_command()
        if "wake up" in query:
            from GreetMe import greetME
            greetME()

            while True:
                query = take_command()

                if "go to sleep" in query:
                    speak("Ok sir, you can call me anytime.")
                    break

                elif "hello" in query:
                    speak("Hello sir, how are you?")

                elif "i am fine" in query:
                    speak("That's great, sir.")

                elif "how are you" in query:
                    speak("Perfect, sir.")

                elif "thank you" in query:
                    responses = [
                        "You're most welcome, sir.",
                        "Anytime, sir.",
                        "Is there anything else I can help you with, sir?",
                        "Happy to help, sir.",
                    ]
                    speak(random.choice(responses))

                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)

                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)

                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)

                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)

                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

                elif "temperature" in query:
                    location = query.split("in")[-1].strip()
                    temp = fetch_temperature(location)
                    if temp:
                        speak(f"Current temperature in {location} is {temp}.")
                    else:
                        speak("Sorry, I couldn't fetch the temperature.")

                elif "set alarm" in query:
                    speak("Tell me the time to set alarm:")
                    alarm_time = input("Please tell me the time to set alarm: ")
                    set_alarm(alarm_time)
                    speak("Alarm has been set.")

                elif "pause" in query:
                    pyautogui.press("k")
                    speak("Video paused.")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("Video played.")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("Video muted.")

                elif "volume up" in query:
                    from Keyboard import volumeup
                    speak("Turning volume up, sir.")
                    volumeup()
                elif "volume down" in query:
                    from Keyboard import volumedown
                    speak("Turning volume down, sir.")
                    volumedown()

                elif "remember that" in query:
                    remember_message = query.replace("remember that", "").strip()
                    speak("You told me to remember that " + remember_message)
                    with open("Remember.txt", "a") as remember_file:
                        remember_file.write(remember_message + "\n")

                elif "what do you remember" in query:
                    with open("Remember.txt", "r") as remember_file:
                        memories = remember_file.readlines()
                        if memories:
                            speak("You told me to remember that " + ''.join(memories))
                        else:
                            speak("I don't remember anything.")

                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()

                elif "calculate" in query:
                    from Calculatenumbers import Calc
                    query = query.replace("naira", "").replace("calculate", "").strip()
                    Calc(query)

                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()

                elif "shutdown the system" in query:
                    speak("Are you sure you want to shut down?")
                    shutdown = input("Do you wish to shutdown your computer? (y/n): ")
                    if shutdown.lower() == "y":
                        speak("Shutting down the system.")
                        os.system("shutdown /s /t 1")
                    elif shutdown.lower() == "n":
                        break

                elif "the time" in query:
                    str_time = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is {str_time}.")

                elif "finally sleep" in query:
                    speak("Okay, sir, I will go to sleep now.")
                    break


if __name__ == "__main__":
    main()
