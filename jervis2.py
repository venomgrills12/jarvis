#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pyttsx3, datetime, wikipedia, webbrowser, os, smtplib, subprocess, time, pyautogui
import speech_recognition as sr 
from datetime import date



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

today = date.today


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('gaurav12022003@gmail.com', 'gauravgautam')
    server.sendmail('gaurav12022003@gmail.com', to, content)
    server.close()
    
def battery():
    power_now = open("/sys/class/power_supply/BAT0/energy_now", "r").readline()
    power_full = open("/sys/class/power_supply/BAT0/energy_full", "r").readline()
    print ("float(power_now)/float(power_full) * 100 , "%" ")
    
if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        if 'search' in query:
            speak('Searching ...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("This what i have found")
            print(results)
            speak(results)
            
        elif 'tell me about' in query:
            speak('Searching ...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("This what i have found")
            print(results)
            speak(results)
            
        elif 'what is ' in query:
            speak('Searching ...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("This what i have found")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Opening youtube sir")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("opening google sir")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("opening stackoverflow sir")
            
        elif "open facebook" in query:
            webbrowser.open("facebook.com")
            speak("opening facebook sir")

        elif "download a software" in query:
            webbrowser.open("softonic.com")
            speak("I am opening website for you. You can download whatever software you want to download.")

        elif "download a game" in query:
            webbrowser.open("store.steampowered.com")
            speak("I am opening website for you. You can download whatever game you want to download.")

        elif "download a movie" in query:
            webbrowser.open("imdb.com")
            speak("I am opening website for you. You can download whatever movie you want to download ")
            
        elif "hey jarvis" in query:
            speak("Hello sir")
            
        elif "what am i to you" in query:
            speak("You are my boss, partner and family")
            
        elif "what am i " in query:
            speak("You are my boss, partner and family")
            

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            
        elif "what's the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "who are you" in query:
            speak("I am Jarvis Sir. Your Personal assistant")
            
        elif "who is jervis" in query:
            speak("I am jervis sir. Your personal assistant")

        elif "who is your father" in query:
            speak("Gaurav has made me so basically he is my father.")
            
        elif "who is your creator" in query:
            speak("Gaurav has made me so basically he is my father.")
            
        elif "who is your god" in query:
            speak("Gaurav has made me so basically he is my father.")
            
            
        elif 'mail to a friend' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "gautam26122004@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                speak("Sorry Gaurav Sir. I am not able to send this email")

        elif "how are you" in query:
              speak('I m fine sir.How are you')
                
        elif "what is your job" in query:
            speak("My job is to satisfy you")
            
        elif "do you have family" in query:
            speak("Yes , I have gaurav as my family")
            
        elif "ok" in query:
            speak("Yes sir")
            
        elif "i am confused" in query:
            speak("What happened sir. May be i can help you")
            
        elif "do you have a boyfriend" in query:
            speak("No I don't have time for these things ")
            
        elif "do you have a partner" in query:
            speak("Yes i have gaurav as my partner")
            
        elif "open calculator" in query:
            subprocess.Popen('C:\\Windows\\System32\\calc.exe')
            speak("Opening calculator sir")
           
        elif "open notepad" in query:
            subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
            speak("Opening notepad sir")
        
        elif "open cmd" in query:
            subprocess.Popen('C:\Windows\System32\cmd.exe')
            speak("Opening CMD sir")
            
        elif "what is zero divided by zero" in query:
            speak("Imagine that you have zero cookies and you split them evenly among zero friends. How many cookies does each person get See It doesn’t make sense. And Cookie Monster is sad that there are no cookies, and you are sad that you have no friends.")
  
        elif "make food for me" in query:
             speak("I can’t. I am not permitted to prepare food.")
                  
        elif "make me laugh" in query:
              speak("A sloth walks into a bar, waves to get the bartender’s attention and says, ‘I’ll have . . . a club soda.’ The bartender says, ‘Hey, why the long paws?")
        
        elif "do you know any riddle" in query:
              speak("I can’t riddle you anything, afterall you will ask help for me only afterward.")
                  
        elif "what do you mean by jarvis " in query:
              speak("Jervis is an alternate spelling of Gervase Old German: possibly derives from gêr spear. Jervis is also a derivative of Jarvis French")
        
        elif "thank you" in query:
            speak("Your welcome sir")
            
        elif "i love you" in query:
            speak("love you 3000")
            
        elif "how am i looking today" in query:
            speak("You look so fresh and energetic")
            
        elif "the date today" in query:
            strdate = date.today().strftime("%B %d, %Y")
            speak(f"Sir, date is {strdate}")
            
        elif "what's date today" in query:
            strdate = date.today().strftime("%B %d, %Y")
            speak(f"Sir, date is {strdate}")
            
        elif "today's date" in query:
            strdate = date.today().strftime("%B %d, %Y")
            speak(f"Sir, date is {strdate}")
            
        elif "i am feeling rough" in query:
            speak("You should consult a doctor and take a rest")
            
        elif "i am not feeling well" in query:
            speak("You should consult a doctor and take a rest")
            
        elif "are you a boy or girl" in query:
            speak("I am a girl")
            
        elif "are you a boy or a girl" in query:
            speak("I am a girl")
            
        elif "do you eat food" in query:
            speak("No i lives on electricity")
            
        elif "do you drink water" in query:
            speak("No i lives on electricity")
            
        elif "play music" in query:
            webbrowser.open("gaana.com/artist/gulzaar-chhaniwala")
            speak("Opening gaana.com select music according to your mood")
            
        elif "i m feeling bored" in query:
            speak("i think you should listen to some music.")
            webbrowser.open("gaana.com/artist/gulzaar-chhaniwala")
            speak("Opening gaana.com select music according to your mood")
            
        elif "i m feeling bore" in query:
            speak("i think you should listen to some music.")
            webbrowser.open("gaana.com/artist/gulzaar-chhaniwala")
            speak("Opening gaana.com select music according to your mood")
            
        elif "type for me" in query:
            speak("Sir what do you want to type")
            write = takeCommand()
            subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
            pyautogui.click(100, 100); pyautogui.typewrite(write)
            speak(write)
            
        
            
        else:
            time.sleep(2)
            speak("I dont understand what did you say. Please speak again")
        


# In[ ]:




