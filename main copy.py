from importlib import import_module
from unittest import result
from pip import main
import pyjokes
from importlib_resources import path
import speech_recognition as sr
import pyttsx3
import pyaudio
import datetime
import os
from sqlalchemy import true 
from webob import hour, second
import pywhatkit
import wikipedia
import pyjokes
from requests import get, head 
import webbrowser
import sys
import pyautogui
import requests
from bs4 import BeautifulSoup
from plyer import notification
import pyautogui
import sounddevice as sd
import soundfile as sf
engine = pyttsx3.init('sapi5')

engine.setProperty('rate', 190)

engine.setProperty('volume',1.0)

voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    # print(audio)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("say that again please...!")
        return "none"
    query = query.lower()
    return query

#Volume frekwensy


def whish():

    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
         speak("Good morning")
    elif hour>=12 and hour<=18:
             speak("Good afternoon") 
    else:     
        speak("Good evening")
    print("i am zira sir. please tell me how can i help you")
    speak("i am zira sir. please tell me how can i help you")
     

   
def get_weather_report(city):
        res = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=f622ecbfa534569874903679f0a665db&units=metric").json()
        weather = res["weather"][0]["main"]
        temperature = res["main"]["temp"]
        feels_like = res["main"]["feels_like"]
        return weather, f"{temperature}℃", f"{feels_like}℃" 

def get_latest_news():
    news_headlines = []
    res = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=in&apiKey=ddd706672f864c049720c6e91392e2ea&category=general").json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])
    return news_headlines[:5]

def make_request(url):
  response = requests.get(url)
  return response.text

def Task():
    whish() 
    while True:
        query = take_command().lower()

        if "open vs code" in query:
            npath = "C:\\Users\\Abhi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(npath)
        elif 'hello' in query:
            speak('hello, sir ')

        elif "open chrome" in query:
            npath= "C:\\Program Files\\Google\Chrome\\Application\\chrome.exe"
            os.startfile(npath)
        
        elif "open download folder" in query:
            npath= "C:\\Users\\Abhi\\Downloads"
            os.startfile(npath)
        elif "open wp" in query:
            npath= "C:\\Users\\Abhi\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(npath)
            
        elif "open command prompt" in query:
            npath=('c:\\windows\\system32\\cmd.exe')
            os.startfile(npath)
        elif "open cmd" in query:
            npath=('c:\\windows\\system32\\cmd.exe')
            os.startfile(npath) 
        elif "ip address" in query: 
            ip = get('https://api.ipify.org/').text
            speak(f"Your IP address is {ip}")

        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)
            
        elif 'time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak('Current time is ' + time)
        
        elif 'date' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak('Current date is ' + date)
            
        elif 'what is ' in query:
            person = query.replace('according to wikipedia', '')
            info = wikipedia.summary(person, 1)
            print(info)
            speak(info)

        elif 'Who is ' in query:
            person = query.replace('according to wikipedia', '')
            info = wikipedia.summary(person, 2)
            #print(info)
            speak(info) 

        elif 'Who ' in query:
            person = query.replace('according to wikipedia', '')
            info = wikipedia.summary(person, 1)
            print(info)
            speak(info)

       # elif 'date' in query:
            #speak('sorry, I have a headache')

        elif 'are you single' in query:
            speak('I am in a relationship with wifi')
            
        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif "open youtube" in query:
                webbrowser.open("www.youtube.com")        
        elif "goodbye" in query:
            speak("thanks for usingnme sir, haw a goood day")
            sys.exit
        elif "shutdown the system" in query:
            os.system("shutdown /s /t 5")

        elif "tell me the news" in query:
            speak("please wait sir, fetchinf some news")
            get_latest_news()

        elif "Weather reports" in query:
            speak("please wait sir, fetchinf some news")
            get_weather_report()


        elif 'switch the window' in query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")
         
        elif "you can sleep" in query or "sleep now" in query:
            speak("it's my pleasure sir.")
            break
        
        elif 'covid reports' in query:
            html_data = make_request('https://www.worldometers.info/coronavirus/')
            # print(html_data)
            soup = BeautifulSoup(html_data, 'html.parser')
            total_global_row = soup.find_all('tr', {'class': 'total_row'})[-1]
            total_cases = total_global_row.find_all('td')[2].get_text()
            new_cases = total_global_row.find_all('td')[3].get_text()
            total_recovered = total_global_row.find_all('td')[6].get_text()
            print('total cases : ', total_cases)
            print('new cases', new_cases[1:])
            print('total recovered', total_recovered)
            notification_message = f" Total cases : {total_cases}\n New cases : {new_cases[1:]}\n Total Recovered : {total_recovered}\n"
            notification.notify(
                title="COVID-19 Statistics",
                message=notification_message,
                timeout=5
            )
            speak("here are the stats for COVID-19")

        elif 'screenshot' in query:
            image = pyautogui.screenshot()
            image.save('screenshot.png')
            speak('Screenshot taken.')
        
        elif 'Volume up' in query:
            pyautogui.press("Volumeup")
        
        elif 'Volume down' in query:
            pyautogui.press("Volumedown")
        elif 'volume mute' in query:
            pyautogui.press("volumemute")
        elif 'volume unmute' in query:
            pyautogui.press("volumemute")
            
        elif 'close chrome' in query:
            speak("okay sir,closing chrome")
            os.system("taskkill /f /is chrome.exe")

        elif 'close Brave' in query:
            speak("okay sir,closing chrome")
            os.system("taskkill /f /is Brave.exe")           

def news():
    main_url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=ddd706672f864c049720c6e91392e2ea"
   
    main_page = requests.get(main_url).json()

    articles = main_page["articles"]
    head = []
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
        for i in range (len(day)):
            speak(f"today's {day[i]} news is: {head[i]}")   

if __name__ == "__main__":
    while True: 
        permission = take_command()
        if "wake up" in permission:
            Task()
        elif "goodbye" in permission:
            speak("thanks for using me sir have a good day")
            sys.exit()
