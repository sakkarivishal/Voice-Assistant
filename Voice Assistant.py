import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def start():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning,Vishal")
    elif hour>=12 and hour<18:
        speak("Good Afternoon,Vishal")
    else:
        speak("Good Evening,Vishal")
    speak("I am your Voice assistant. Please tell me how may I help you")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print("You said: ",query)
    except Exception as e:
        #print(e)
        print("Didn't get you,say that again") 
        return "None"
    return query
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('********@gmail.com','*******')
    server.sendmail('******@gmail.com',to,content)
    server.close()



if __name__=="__main__":
    start()
    #while True:
    if 1:
        query=takecommand().lower()

        if 'wikipedia' in query:
            speak("searching wikpedia..")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(result)
            speak(result)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif query=='play music' :
            music_dir="C:\\Users\\Lenovo\\Music\\songs"
            songs=os.listdir(music_dir)
            #print(songs)
            x=random.randrange(0,len(songs)-1)
            os.startfile(os.path.join(music_dir,songs[x]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif 'send an email' in query:
            try:
                speak("what should i send?")
                content=takecommand()
                #speak("to whom should i send?")
                to='********@gmail.com'
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry,Error sending Email")
        #elif query=='quit':
         #   break
        