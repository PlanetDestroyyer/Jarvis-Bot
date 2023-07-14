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

def headLine():
    query_params = {
	"source": "bbc-news",
	"sortBy": "top",
	"apiKey": "d0991d9186da4c259f29b078bd9d7550"
	}
    url = " https://newsapi.org/v1/articles"
    response = requests.get(url,params=query_params)
    data = json.loads(response.text)
    news = data
    for new in news['articles'][::10]:
        print("______________________________New_______________________________")
        speak(str(new['title']))
        print('---------------------------Description-----------------------------')
        print("\n\n")
        print(str(new['description']))
        print("............................End................................")

def sports():   
    url = "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=d0991d9186da4c259f29b078bd9d7550"
    response = requests.get(url)
    data = json.loads(response.text)
    news = data
    for new in news['articles'][::10]:
        print("______________________________New_______________________________")
        speak(str(new['title']))
        print('---------------------------Description-----------------------------')
        print("\n\n")
        print(str(new['description']))
        print("............................End................................")

def business():   
    url = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=d0991d9186da4c259f29b078bd9d7550"
    response = requests.get(url)
    data = json.loads(response.text)
    news = data
    for new in news['articles'][::10]:
        print("______________________________New_______________________________")
        speak(str(new['title']))
        print('---------------------------Description-----------------------------')
        print("\n\n")
        print(str(new['description']))
        print("............................End................................")

def Entertainment():   
    url = "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=d0991d9186da4c259f29b078bd9d7550"
    response = requests.get(url)
    data = json.loads(response.text)
    news = data
    for new in news['articles'][::10]:
        print("______________________________New_______________________________")
        speak(str(new['title']))
        print('---------------------------Description-----------------------------')
        print("\n\n")
        print(str(new['description']))
        print("............................End................................")

def Health():   
    url = "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=d0991d9186da4c259f29b078bd9d7550"
    response = requests.get(url)
    data = json.loads(response.text)
    news = data
    for new in news['articles'][::10]:
        print("______________________________New_______________________________")
        speak(str(new['title']))
        print('---------------------------Description-----------------------------')
        print("\n\n")
        print(str(new['description']))
        print("............................End................................")

def science():   
    url = "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=d0991d9186da4c259f29b078bd9d7550"
    response = requests.get(url)
    data = json.loads(response.text)
    news = data
    for new in news['articles'][::10]:
        print("______________________________New_______________________________")
        speak(str(new['title']))
        print('---------------------------Description-----------------------------')
        print("\n\n")
        print(str(new['description']))
        print("............................End................................")

def Technology():   
    url = "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=d0991d9186da4c259f29b078bd9d7550"
    response = requests.get(url)
    data = json.loads(response.text)
    news = data
    for new in news['articles'][::10]:
        print("-------------------------------New----------------------------------")
        speak(str(new['title']))
        print('---------------------------Description-----------------------------')
        print("\n\n")
        print(str(new['description']))
        print("............................End................................")



if __name__ == "__main__":
    # query = "business"
    # if ('business') in query:
    #     business()
    # elif('health') in query:
    #     Health()
    # elif ('sports') in query:
    #     sports()
    # elif ('technology') in query:
    #     Technology()
    # elif ('science') in query:
    #     science()
    # elif ('entertainment') in query:
    #     Entertainment()
    # else:
    #     headLine()
    pass