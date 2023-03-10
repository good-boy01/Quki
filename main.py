#moudels 
import subprocess
import wolframalpha 
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
import random
import pygame
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen

#voice settings and engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
#functions
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Sir !")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon Sir !")  
  
    else:
        speak("Good Evening Sir !") 
  
    assname =("Quki")
    speak("I am your Assistant")
    speak(assname)
def username():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns
     
    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))
     
    speak("How can i Help you, Sir")
def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
     
    return query
##def sendEmail(to, content):
    #server = smtplib.SMTP('smtp.gmail.com', 587)
    #server.ehlo()
    #server.starttls()
    #server.login('kh.ilia@yahoo.com', 'Dalam123')
    #server.sendmail('your email id', to, content)
    #server.close()
#main
if __name__ == '__main__':
    clear = lambda: os.system('cls')
    clear()
    wishMe()
    username()

    while True:
         
        query = takeCommand().lower()
         
        # All the commands said by user will be
        # stored here in 'query' and will be
        # converted to lower case for easily
        # recognition of command
        if 'Wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            speak("Here you go to Stack Over flow  , Good luck ")
            webbrowser.open("stackoverflow.com")

        
        elif 'the time' in query:
            strtime = datetime.datetime.now()

            speak(f"the time is {strtime}")
        
    
        

        elif 'how are you' in query:
            speak("I am great , thank you ")
            speak("How are you, Sir")

        elif "I'm fine" in query or " I'm good" in query:
            speak("It's good to know that your fine")
        
        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query

        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")
        
        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Ilia khanmohamedi")
        
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        
        
        
        elif 'search' in query :
             
            query = query.replace("search", "")
            query = query.replace("play", "")         
            webbrowser.open(query)

        elif "who am I" in query:
            speak("Your human  , im AI , we are not the same ! ")
        
        elif "why you came to world" in query:
            speak("Thanks to ilia . further It's a secret , but you can ask ilia by emailing ")
        
        elif "who are you" in query:
            speak("I am your virtual assistant , Quki")
        

        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                       0,
                                                       "Location of wallpaper",
                                                       0)
            speak("Background changed successfully")

        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

        #elif 'shut down system' in query:
                #speak("Hold On a Sec ! Your system is on its way to shut down")
                #subprocess.call('shutdown / p /f')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")
        
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop Quki from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
        
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")
        
        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Quki Camera ", "img.jpg")
        
        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
        
        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")
        
        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])
        
        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('Quki.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now()
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("Quki.txt", "r")
            print(file.read())
            speak(file.read(6))
        
        elif "Quki" in query:
             
            wishMe()
            speak("Quki in your service Mister")
            

        elif "weather" in query:
             
            # Google Open weather website
            # to get API of Open weather
            api_key = "AIzaSyDw_p0ea7zzAk7PGtFtC0zO4yGOnNfsRco"
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak(" City name ")
            print("City name : ")
            city_name = takeCommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()
             
            if x["code"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
             
            else:
                speak(" City Not Found ")

        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")

        elif "good morning" in query:
            speak("A warm" + query)
            speak("How are you Mister")
            
        elif "will you be my gf" in query or "will you be my bf" in query:  
            speak("But Im not real ")
        
        elif "how are you" in query:
            speak("I'm fine, glad you asked that")

        elif "i love you" in query:
            speak("It's hard to understand , because im an AI and dont have feelings , but thanks")
        
        elif "what is" in query or "who is" in query:
             
            # Use the same API key
            # that we have generated earlier
            client = wolframalpha.Client("AIzaSyDw_p0ea7zzAk7PGtFtC0zO4yGOnNfsRco")
            res = client.query(query)

            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results")
        elif "i love salad" in query:
            speak("ilia does to !")

        elif 'flip a coin' in query:
            chance = random.randint(0,100)
            if chance%2 == 0:
                speak("its head")
            if chance%2 == 1:
                speak('its tails')
        
        elif 'i am your dad' in query:
            speak("then ario is my grandfather")
        
        elif "bet" in query:
            speak("here you go , good luck")
            webbrowser.open("1xbet.com")
        
        elif "buy something" in query or "boy something" in query:
            speak("here you go to digikala dot com")
            webbrowser.open("digikala.com")
        
        elif "open linked in " in query or "open linkedin" in query :
            speak("Ok , on it ")
            webbrowser.open("linkedin.com")
        
        elif "open spotify" in query or "open spotifi" in query :
            speak("opening spotify , have a good time vibing ")
            webbrowser.open("open.spotify.com")
        
        elif "play a game" in query:
            speak("ok , hear you go , have fun ")
            exec(file("game.py"))
            execfile("game.py")
        
        elif "i need food" in query or "i am hungry" in query:
                webbrowser.open("snappfood.ir")
        
        elif " I love seminar" in query: 
            speak("good to hear that, Welcome to the thirty seventh seminar ! ")

        elif "how do you work " in query:
            speak("its a secret , but you can ask ilia or ario ")

        elif "Can you swear" in query:
            speak('no , swearing is not in my programs')


        
        
