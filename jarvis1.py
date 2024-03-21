import pyttsx3
import  speech_recognition as sr
import  datetime
import os
import  cv2
import random
import  requests
from  requests import get
import wikipedia
import  webbrowser
import pywhatkit
import sys
import tkinter





engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
print(voices[0].id)
engine.setProperty("voices",voices[0].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listning...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=5,phrase_time_limit=10)


        try:
            print("Recognizing...")
            query=r.recognize_google(audio, language="en-in")
            print(f"user said:{query}")

        except Exception as e:
            speak("say that again please...")
            return "none"
        return query

def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12:
            speak("good morning")
    elif hour > 12 and hour < 18:
            speak("good afternoon")
    else:
            speak("good evening")
    speak("Sir i am advanced jarvis please tell me how can i help you")


if __name__ == "__main__":
    wish()
    while True:
    #if 1:


         query=takecommand().lower()






         if "open notepad" in query:
            npath="C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
         elif "open notepad" in query:
                npath = ""
                os.startfile(npath)
         elif "open command prompt" in query:
            os.system("start cmd")

         elif "open cammera" in query:
            cap=cv2.VideoCapture(1)
            while True:
                ret,img=cap.read()
                cv2.imshow("webcam",img)
                k=cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()


         elif "play music" in query:
           music_dir= "C:\\music"
           songs= os.listdir(music_dir)
           rd=random.choice(songs)
           os.startfile(os.path.join(music_dir,rd))


         elif "ip address" in query:
            ip= get('https://api.ipify.org').text
            speak(f"Your IP address is{ip}")




         elif "open youtube" in query:
           webbrowser.open("www.youtube.com")
         elif "open spotify" in query:
           webbrowser.open("www.spotify.com")
         elif "open chrome" in query:
           webbrowser.open("www.chrome.com")
         elif "open classroom" in query:
           webbrowser.open("https://classroom.google.com/u/0/h")
         elif "google" in query:
            speak('Sir what should i search on google')
            cm=takecommand().lower()
            webbrowser.open(f"{cm}")
         elif "send message" in query:
            pywhatkit.sendwhatmsg("+919373996202",'Hello',19,12)

         elif 'no thanks' in query:
            speak('thanks for using me sir,have a good day')
            sys.exit()
         speak('sir do you have anyother work')
