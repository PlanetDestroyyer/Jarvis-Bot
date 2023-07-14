import requests
import json
import pyttsx3
import speech_recognition as sr

#getting the voice from the system
Assistant = pyttsx3.init('sapi5')
voice = Assistant.getProperty('voices')
Assistant.setProperty('voice', voice[0].id)

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
    return query

def joke():
    url = "https://dad-jokes.p.rapidapi.com/random/joke"

    headers = {
    	"content-type": "application/octet-stream",
    	"X-RapidAPI-Key": "132d97dc1emsh74614bee7028c43p1ce01bjsna30851e6698e",
    	"X-RapidAPI-Host": "dad-jokes.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    for joke in data['body']:
        speak(str(joke['setup']))
        speak(str(joke['punchline']))

if __name__ == "__main__":
    joke()