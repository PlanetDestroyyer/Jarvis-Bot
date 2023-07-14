import pyttsx3
import speech_recognition as sr
import requests
import json


Assistant = pyttsx3.init('sapi5')

voice = Assistant.getProperty('voices')

Assistant.setProperty('voice', voice[1].id)

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
            speak("Say that again please...")
            return "None"
    return query.lower()

def movie():
    url = "https://imdb8.p.rapidapi.com/auto-complete"
    speak("Name a movie to recommend?")
    movieName = takeCommand()
    movieName.replace("movie","")
    querystring = {f"q":{movieName}}
    headers = {
    	"X-RapidAPI-Key": "132d97dc1emsh74614bee7028c43p1ce01bjsna30851e6698e",
    	"X-RapidAPI-Host": "imdb8.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)


    datas = json.loads(response.text)
    for new in datas['d']:
        if new['l'] is None or new['s'] is None:
            pass
        else:
            print(".............................New................................")
            print("\n")
            print(f"Title of the movie : {str(new['l'])}")
            print(f"Cast : {str(new['s'])}")
            print("\n")
            print("________________________________________________________________")

if __name__ == "__main__":
    movie()