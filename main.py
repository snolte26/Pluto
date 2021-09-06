import ctypes
import sys
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from dotenv import load_dotenv
import random
import requests
import pyautogui

# Importing setup.py for environment variable setup
import setup

# TODO: Add Linux support <3
# Checks to see if you are running windows, then imports some more modules,
# or throws a fit if you are not, for now
if sys.platform.startswith('win32'):
    import win32gui
    import win32con
else:
    exit('\nSorry, but platform ' + sys.platform + ' is not supported yet. :(')

# Looks for a .env file and loads it.
# See: https://pypi.org/project/python-dotenv/
load_dotenv()

# Set up environment if needed
if not os.path.exists('./.env') or not os.getenv('OWM_KEY') or not os.getenv('MUSIC_PATH'):
    setup.init_env()


# Setting up the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0 is male, 1 is female. I went with female. -snolte26
engine.setProperty('rate', 155)


# Takes string input, then outputs that string as speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 11:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening")

    speak("I am JARVIS, how may I help you?")


# Weather function
def weather(zip):
    base = "https://api.openweathermap.org/data/2.5/weather?"
    ''' apiKey = "" '''

    # TODO: add zipcode to environment variable - preferably automated in setup.py if it doesn't exist
    # For now, you can edit this zip code variable instead
    '''
    if os.getenv('OWM_ZIP'):
        zipcode = os.getenv('OWM_ZIP')
    '''
    # Setup OWM_KEY in the .env if there is none
    if not os.getenv('OWM_KEY'):
        setup.init_env()

    apiKey = os.getenv('OWM_KEY')

    url = base + "zip=" + zip + "&appid=" + apiKey
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        Main = data['main']
        tmpma = Main['temp']
        humidity = Main['humidity']
        temperature = int((((tmpma - 273.15) * 9) / 5) + 32)
        tmpmax = Main['temp_max']
        tmpmin = Main['temp_min']
        tempMax = int((((tmpmax - 273.15) * 9) / 5) + 32)
        tempMin = int((((tmpmin - 273.15) * 9) / 5) + 32)
        report = data['weather']
        speak(f"Sir, the current temperature is {temperature} Degrees Fahrenheit")
        speak(f"and {report[0]['description']}")
        speak(f"The humidity is currently {humidity}%")
        speak(f"The high for today is {tempMax} degrees and a low of {tempMin} degrees")
    else:
        print("no data today")
        speak("Sorry, I cant find any weather data right now")


# Listening to the command
def takeCommands():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception:
        print("Say that again, please...")
        return "None"
    return query


# Main function
def main():
    wishMe()
    while True:
        query = takeCommands().lower()

        # Begin looking at what user has said

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("Sir, " + results)
            print(results)

        elif 'open youtube' in query:
            webbrowser.open_new("youtube.com")
        elif 'open stackoverflow' in query:
            webbrowser.open_new("stackoverflow.com")
        elif 'open github' in query:
            webbrowser.open_new("github.com")

        # If the user wants to know the weather
        elif 'weather' in query or 'temperature' in query:
            speak("For what zipcode would you like the weather?")
            zip = takeCommands()
            weather(zip)

        # Basically another wikipedia call, but is like asking a question
        elif 'who is' in query or 'how to' in query or 'what is' in query:
            speak('Searching Wikipedia...')
            resultsw = wikipedia.summary(query, sentences=2)
            speak("Sir, " + resultsw)
            speak("That's it")
            print(resultsw)

        # Playing music
        elif 'play music' in query or 'play some music' in query:
            if not os.getenv('MUSIC_PATH'):
                setup.init_env()

            musicDir = os.getenv('MUSIC_PATH')
            songs = os.listdir(musicDir)
            chosenSong = random.randint(1, len(songs))
            speak('ok sir. playing ' + songs[chosenSong - 1])
            os.system(musicDir + "\\" + songs[chosenSong - 1])
            # os.system(os.path.join(music_dir, songs[1]))

        elif 'the time' in query or 'what is time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        # Opens Firefox, really only works if you have firefox
        # TODO: Support for default browser? idk
        elif 'open firefox' in query:
            speak("opening firefox ")
            codePathf = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
            os.startfile(codePathf)

        elif 'hide window' in query or 'hide work' in query or 'change window' in query or 'minimise window' in query:
            # close in window
            speak("ok.")
            Minimize = win32gui.GetForegroundWindow()
            win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)

        elif 'full window' in query or 'full screen window' in query or 'fullscreen' in query or 'maximize window' in \
                query:
            speak("sure.")
            hwnd = win32gui.GetForegroundWindow()
            win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)

        # Locks the screen, essentially like pressing "Win + L"
        # <>Pretty proud of this one, ngl. -snolte26</>
        elif 'lockdown' in query or 'lock everything down' in query or 'lock down' in query:
            speak("Locking things down...")
            ctypes.windll.user32.LockWorkStation()
            speak("Locked down, I'll be waiting")

        elif 'screenshot' in query or 'screen shot' in query:
            speak("Screenshot, coming up...")
            pyautogui.hotkey('win', 'shift', 's')

        elif 'who are you' in query or 'about you' in query or "your details" in query:
            speak("i am JARVIS, your work partner. I'm all ear's")

        elif 'how are you' in query:
            speak("I am doing alright. How can i help you?")

        elif 'exit' in query or 'goodbye' in query or 'good bye' in query or 'bye' in query:
            speak("thank you, see you later")
            quit()

        elif 'thank you' in query or 'thanks' in query:
            speak("No problem sir.")

        elif "hello" in query or "hello Jarvis" in query:
            hel = "Hello  Sir ! How May i Help you.."
            print(hel)
            speak(hel)

        # Clears the console window. That thing can get full quick from all the listening it does and probably not
        # getting any useful inputs
        elif 'clean' in query:
            speak("ok.")

            def clear():
                return os.system('cls')

            clear()

        # This was just for goofs, its from an Eric Andre bit. https://www.youtube.com/watch?v=CDUlz-S11Cw
        elif "show me this guy's balls please" in query:
            speak("ok, here is this guys balls")
            webbrowser.open_new(
                'https://www.std-gov.org/blog/wp-content/uploads/2018/06/Swollen_Testicles1-640x640.jpg')

        elif 'what can you do' in query:
            speak("I can give you the time, give info from wikipedia, give you the weather, play music, lock things "
                  "down, open certain pages, take screenshots, and other small tasks. I try to help you where I can")


if __name__ == '__main__':
    main()
