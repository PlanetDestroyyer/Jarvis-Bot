#importing all requried Libary 
import pyttsx3
import speech_recognition as sr
import AppOpener
import webbrowser
import time
import pywhatkit
import datetime
import Recommendationmovie
import jokes
import whatapp
from playsound import playsound
import wikipedia
# from pywinauto import application
from news import Technology,science,sports,business,Entertainment,Health,headLine

#getting the voice from the system
Assistant = pyttsx3.init('sapi5')
voice = Assistant.getProperty('voices')
Assistant.setProperty('voice', voice[0].id)
Assistant.setProperty('rate',200)
# app = application.Application()
#speaking function
def speak(audio):
    Assistant.say(audio)
    print("\n")
    print(audio)
    Assistant.runAndWait()

#recognition voice function
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"You said: {query}\n")
        except Exception as e:
            return "None"
    return query

#greeting Function
def greeting():
    current_time = datetime.datetime.now()
    if current_time.hour < 12:
        speak("Good Morning")
    elif 12 <= current_time.hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

#opening site function
def site():
    speak("Which site to open?")
    query = takeCommand()
    if 'Instagram' in query:
        query = query.replace("open", "")
        webbrowser.open("http://Instagram.com")
    elif 'Facebook' in query:
        query = query.replace("open", "")
        webbrowser.open("http://www.Facebook.com")
    elif 'Twitter' in query:
        query = query.replace("open", "")
        webbrowser.open("http://www.Twitter.com")
    else:
        query = query.replace("open", "")
        query = query.replace(" ", "")
        webbrowser.open(f"http://{query}.com")

# Opening Application Function
def openApps(query):
    try:
        AppOpener.open(query)
    except FileNotFoundError as e:
        print("The system cannot find the file")

# closing Application Function   
def closeApp(query):
    try:
        AppOpener.close(query)
    except FileNotFoundError as e:
        print("The system cannot find the file")

#Google search function   
def googleSearch(query):
    pywhatkit.search(query)
    speak("Done")

#displaying news Function
def TopHeadLines(query):
    try:
        if ('business') in query:
            business()
        elif('health') in query:
            Health()
        elif ('sports') in query:
            sports()
        elif ('technology') in query:
            Technology()
        elif ('science') in query:
            science()
        elif ('entertainment') in query:
            Entertainment()
        else:
            headLine()
    except:
        print("Error")

#wikipidea
def wiki(query):
    speak(wikipedia.summary(query,sentences = 2))

#Get the Movie
def recomMovie():
    Recommendationmovie.movie()

#WhatsApp command
def whatsApp(query):
    whatapp.data(query)

#Jokes Command
def Jokes():
    jokes.joke()

#byee    
def bye():
    speak("Thanks for Using me")
    speak("Bye , Take care")
    quit()

#taking input form users to do task respectively
def task():
   
   while True:
       query = takeCommand()
       
       if ('hey Jarvis how are you') in query:
           speak("I am all Good")
           speak("What about You? How are you?")
           
       elif ('take rest') in query:
           speak("OK , Just say Hey when u needed me")
           break
       
       elif ('I am good') in query:
           speak("Good to know , How can i Help u?")
       
       elif ('search') in query.lower():
           query = query.replace("google search", "")
           googleSearch(query)
           speak("What else I should do for u?")
       
       elif ('open a website') in query:
           site()
           speak("What else I should do for u?")
       
       elif ('open') in query:
            query = query.replace("open", "")
            openApps(query)
            speak("What else I should do for u?")
       
       elif('close') in query:
            query = query.replace("close", "")
            closeApp(query)
            speak("What else I should do for u?")
       
       elif ('top headline') in query:
           TopHeadLines(query)
           speak("What else I should do for u?")

       elif ('recommend a good movie') in query:
           recomMovie()
           speak("What else I should do for u?")

       elif ('tell me a joke') in query:
           Jokes()
           speak("What else I should do for u?")
        
       elif ('send message') in query:
           query =query.replace('send message','')
           query =query.replace('to','')
           query =query.replace(' ', '')
           print(query)
           whatsApp(query)
           
           speak("What else I should do for u?")
       elif ('who is') in query:
           query = query.replace('who is',"")
           query = query.replace('what is ',"")
           wiki(query)
           
           
       elif ('bye') in query:
           speak("Thanks for Using me")
           speak("Bye , Take care")
           bye()

       else:
        
           speak("Say that again please..")

#main Function
def main():
    greeting()
    playsound('audio.MP3')
    time.sleep(2)
    speak("All ready to go!")
    speak("Hey")
    task()

if __name__ == '__main__':
    main()