import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib
import pyjokes
engine = pyttsx3.init('sapi5')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 6:
        speak("Hey Amine")

    elif hour >= 6 and hour < 12:
        speak("Good Morning")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak("Hello sir")

    speak("I'm Alexa")
    speak("Please tell me how may i help you ?")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognising.....")
        query = r.recognize_google(audio, language='en')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please.....")
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('hamadhahbi2020@gmail.com', 'xxxxxxxx')
    server.sendmail('hamadhahbi2020@gmail.com', to, content)
    server.close()


def joke():
    joke_text = pyjokes.get_joke(language='en', category='all')
    speak(joke_text)
    print(joke_text)
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            speak(results)
            print(results)
        elif 'open college website' in query:
            webbrowser.open("http://www.isetr.rnu.tn/")

        elif 'start youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open soft' in query:
            webbrowser.open("https://www.didousoft.com/redirect?nConnection")

        elif 'open LinkedIn' in query:
            webbrowser.open("Linkedin.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H,%M,%S")
            speak(f"Sir, the time is {strTime}")
        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "hamadhahbi2020@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(f"An error occurred: {e}")
                speak("Sorry sir. I am not able to send this email")

        elif 'shut down' in query:
            print("shutting down...")
            speak("shutting down")
            quit()

        elif 'joke' in query:
            joke()

        elif 'search youtube' in query:
            speak("What would you like to see, Amine?")
            search= takeCommand().lower()
            speak('I found these videos')
            webbrowser.open('https:/www.youtube.com/results?search_query='+search)

        elif 'search google' in query:
            speak("What would you like to see, Amine?")
            search=takeCommand().lower()
            speak('this is what i found')
            webbrowser.open('https:/www.google.com/search?pglt=43&q='+search)
