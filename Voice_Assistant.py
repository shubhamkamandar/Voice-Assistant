import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import sys
import time
import pyjokes
import pyautogui
import os.path
import pywhatkit as kit


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)
#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


#To convert voice into text
def  takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=5,phrase_time_limit=8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query

#to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour <= 12:
        speak(f"good morning, its {tt}")
    elif hour >= 12 and hour <= 18:
        speak(f"good afternoon, its {tt}")
    else:
        speak(f"good evening, its {tt}")
    speak("i am Anna!. please tell me how may i help you")

if __name__ == "__main__": 
    wish()
    while True:

        query = takecommand().lower()

        if "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
            speak("Opening notepad")
    
        elif "open command prompt" and "cmd"in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(1)
                if k==1:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif 'play song' and 'play music'and 'song' in query:
            rand = random.randint(1, 4)
            music_dir = 'F:\song'    #Give Your Song File Path
            songs = os.listdir(music_dir)
            #print(songs)    
            os.startfile(os.path.join(music_dir, songs[rand]))

        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            # print(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "open google" in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        #elif "send whatsapp message" in query:
        #   kit.sendwhatmsg("+91_To_number_you_want_to_send", "this is testing protocol",4,13)
        #    time.sleep(120)
        #    speak("message has been sent")

        elif "song on youtube" in query:
            kit.playonyt("see you again")
            
        elif 'timer' in query or 'stopwatch' in query:
            speak("For how many minutes?")
            timing = takecommand()
            timing =timing.replace('minutes', '')
            timing = timing.replace('minute', '')
            timing = timing.replace('for', '')
            timing = float(timing)
            timing = timing * 60
            
            speak(f'I will remind you in {timing} seconds')

            time.sleep(timing)
            speak('Your time has been finished sir')



        elif 'calculator' in query:
            codePath="C:\\Windows\\System32\\calc.exe"
            os.startfile(codePath)
            speak("Opening Calculator")

#to close any application
        elif "close notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")


#to find a joke
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif 'switch the screen' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "thank you"in query:
            speak("thanks for using me sir, have a good day.")
            sys.exit()
