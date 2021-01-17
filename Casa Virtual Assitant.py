import speech_recognition as sr
import pyttsx3
import pywhatkit
import time
import wikipedia
import pyjokes
import os
import playsound
import subprocess
from gtts import gTTS


#Understand my voice
listener = sr.Recognizer()
#speech to text
engine = pyttsx3.init()
#switching to female voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_data():
    try:
    #incase my microphone doesn't work.
    #Listening to the source and then calling the SpeechRecognizer to listen to it
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            data = listener.recognize_google(voice)
            data = data.lower()
            if 'casa' in data:
                #in case data being searched up has the word 'casa'
                data = data.replace('casa', '')
    except sr.UnknownValueError:
        #too much background noice
        print('Casa did not understand. Please try again')
        #pass
    except sr.RequestError as e:
        #request fails
        print('Request Failed; {0}'.format(e))
    return data


def running_casa():
    data = take_data()
    if 'play' in data:
        #in case song being searched up has the word play
        song = data.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'what time is it' in data:
        print (time.ctime())
        talk(time.ctime())
        
    elif 'search' in data:
        command = data.replace('search', '')
        info = wikipedia.summary(command, 1)
        print(info)
        talk(info)

    elif 'joke' in data:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())
        
    elif 'weather' in data:
        api_key = "Your_API_key"
        weather_url = "http://api.openweathermap.org/data/2.5/weather?"
        data = data.split(" ")
        location = str(data[5])
        url = weather_url + "appid=" + api_key + "&q=" + location 
        js = requests.get(url).json() 
'''
def note(data):
    date = datetime.datetime.now()
    file = str(date).replace(':', '-') + "-note.txt"
    with open(file_name, 'w') as f:
        f.write(data)

    subprocess.Popen(['notepad.exe', file_name])
'''

running_casa()

