import pandas as pd
import pyttsx3
import speech_recognition 
# from pynput.keyboard import Key, Controller
import time
import keyboard
import pywhatkit

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
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
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
#recognition voice function
def listen():
    recognizer = speech_recognition.Recognizer()
    while True:
        try:
            with speech_recognition.Microphone() as mic:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(mic,duration=0.5)
                audio = recognizer.listen(mic)
                text = recognizer.recognize_google(audio, language='en-in')
                text = text.lower()
                print("Recognizing...")
                print(f"You said : {text}")
                break
            
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
    return text

def data(name): 
    df = pd.read_csv("Your CSV file path")
    number = df['Numbers'].tolist()
    names = df['Names'].tolist()
    if name in names:
        index = names.index(name)
        number = number[index]
        number = int(number)
        whatappp(number)
        
    else:
        speak("Invalid name or the name u have given is not in contact")
        
    return number

def whatappp(num):
    num = "+91" + str(num)
    speak("What u want to send")
    query = listen()
    try:
        pywhatkit.sendwhatmsg_instantly(num,
    						query)
        time.sleep(25)
        keyboard.press("Enter")

    except:
        speak("Check ur internet connection!")


if __name__ =="__main__":
    # while True:
    #     speak("Whom to send mesage?")
    #     query = takeCommand()
    
    data(query)