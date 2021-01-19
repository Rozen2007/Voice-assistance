import sys
import time
import kit as kit
import pyautogui
import pyttsx3
import requests
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import pyjokes
from number import dad
from number import mom
from number import sis
import cv2
import json

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am  Mombee 2.O Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    query = query.lower()
    return query


def speak_news():
    url = 'http://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=1fd3a53382344ff2b401038a09e4d473'
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    speak('Source: The Times Of India')
    speak('Todays Headlines are..')
    for index, articles in enumerate(arts):
        speak(articles['title'])
        if index == len(arts) - 1:
            break
        speak('Moving on the next news headline..')
    speak('These were the top headlines, Have a nice day Sir!!..')


def getNewsUrl():
    return 'http://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=yourapikey'





def TakeExecuttion():
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'hello' in query or 'hi' in query:
            speak("Hi sir,with what can i help you?")

        elif 'open notepad' in query:
            speak("opening notepad")
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif "open command prompt" in query:
            speak("opening C M D")
            os.system("start cmd")
        elif 'youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif 'google' in query:
            speak("Sir, What Should I search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'songs' in query:
            speak("playing song")
            music_dir = 'C:\\Users\\Deedimj2000\\OneDrive\\Pictures\\Documents\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            speak("opening vs code")
            codePath = "C:\\Users\\Deedimj2000\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'send message' in query:
            speak("Sir, What message Should I send")
            pywhatkit.sendwhatmsg("+91 xxxx xxxx receivers number", "Hi", 19, 30)

        elif 'open camera' in query:
            speak("opening camera")
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        # sleep
        elif 'thank you' in query:
            speak("my pleasure")
            break

        elif "exit" in query:
            speak('If you want me to do anything else just call me !!')
            break

        elif "you can sleep" in query:
            speak('If you want me to do anything else just call me !!')
            break

        # close apps
        elif "close notepad" in query:
            speak("okay sir closing,Notepad")
            os.system("taskkill /f /im notepad.exe")
        elif "close code" in query:
            speak("okay sir closing,Notepad")
            os.system("taskkill /f /im Code.exe")
        elif "set alarm" in query:
            nn = int(13.5.now().hour)
            if nn == 22:
                music_dir = 'C:\\Users\\Deedimj2000\\OneDrive\\Pictures\\Documents\\alarm'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))
        # jokes
        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        # shut down
        elif 'shut down' in query:
            os.system("shutdown /s / t 5")

        # restart
        elif 'restart' in query:
            os.system("shutdown /r / t 5")

        # sleep
        elif 'sleep the system' in query:
            os.system("rund1132.exe powrprof.dil,SetSuspendedState 0,1,0")

        # switch window
        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        # news
        elif 'news' in query:
            speak('Of course sir..')
            speak_news()
            speak('Do you want to read the full news...')
            test = takeCommand()
            if 'yes' in test:
                speak('Ok Sir, Opening browser...')
                webbrowser.open(getNewsUrl())
                speak('You can now read the full news from this website.')
            else:
                speak('No Problem Sir')


if __name__ == "__main__":
    while True:
        permission = takeCommand()
        if 'hello' in permission:
            TakeExecuttion()
        elif "good bye" in permission or "goodbye" in permission:
            speak("Thank you for using mombee 2.O,Have a great day!!")
            sys.exit()
