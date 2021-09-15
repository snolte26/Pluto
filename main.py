import ctypes
import datetime
import json
import os
import random
import sys
import time
import types
import webbrowser
import pyautogui
import pyttsx3
import requests
import speech_recognition as sr
import wikipedia
import wolframalpha
from dotenv import load_dotenv
from threading import Timer
import asyncio

# Importing config.py for environment variable setup
import config

is_windows = sys.platform.startswith('win32')

# Initialize recognizer outside function body so that its state changes,
# and also so that it only runs once. 
r = sr.Recognizer()

# Collect ambient noise (runs only once) and save it to the recognizer instance for later
with sr.Microphone() as source:
    print('\nA moment of silence please.\nAdjusting for ambient noise...')
    r.adjust_for_ambient_noise(source, 3)

# TODO: Add Linux support <3
# is this ^ "to do" done? can i get rid of it? -snolte26
# Checks to see if you are running windows, then imports some more modules,
# or throws a fit if you are not, for now
if is_windows:
    import win32gui
    import win32con
    import winsound
else:
    import beepy

    print('\nThe ' + sys.platform + ' platform is not fully supported yet. :(\nSome features may work, but no guarantees.')
    print('Continuing...')

# Looks for a .env file and loads it.
# See: https://pypi.org/project/python-dotenv/
load_dotenv()

# Set up environment if needed
if not os.path.exists('./.env') or not os.getenv('OWM_KEY') or not os.getenv('MUSIC_PATH') or not os.getenv('WOLF_ALPH_KEY'):
    config.initialize()


'''
This top-level empty object will hold the speech engine to be used. This starts out as empty, then gets populated
later. What gets populated depends on the current OS. `types.SimpleNamespace()` is the python way of instantiating
an empty object that allows creating and setting attributes.
See: https://stackoverflow.com/questions/19476816/creating-an-empty-object-in-python
'''
speech = types.SimpleNamespace()


def init_speech_engine_windows():
    speech.engine = pyttsx3.init('sapi5')
    voices = speech.engine.getProperty('voices')
    speech.engine.setProperty('voice', voices[0].id)  # 0 is male, 1 is female. -snolte26
    speech.engine.setProperty('rate', 155)


def init_speech_engine_linux():
    speech.engine = pyttsx3.init('espeak')
    speech.engine.setProperty('voice', 'default')


# Takes string input, then outputs that string as speech
def speak(audio):
    speech.engine.say(audio)
    speech.engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 11:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening")

    speak("I am JARVIS, how may I help you?")


def timer(alarmTime):

    time.sleep(alarmTime)
    for i in range(3):
        if is_windows:
            frequency = 2600
            duration = 500  # duration is in milliseconds, 250 ms = .25 seconds
            winsound.Beep(frequency, duration)
        else:
            beepy.beep(4)
        time.sleep(.15)


# Weather function
def weather(zip):
    base = "https://api.openweathermap.org/data/2.5/weather?"

    # TODO: add zipcode to environment variable - preferably automated in config.py if it doesn't exist
    # For now, you can edit this zip code variable instead
    '''
    if os.getenv('OWM_ZIP'):
        zipcode = os.getenv('OWM_ZIP')
    '''
    # Setup OWM_KEY in the .env if there is none
    if not os.getenv('OWM_KEY'):
        config.initialize()

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
def takeCommands(beep):
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        if beep:
            if is_windows:
                frequency = 2500
                duration = 250  # duration is in milliseconds, 250 ms = .25 seconds
                winsound.Beep(frequency, duration)
            else:
                beepy.beep(1)

            audio = r.listen(source)
        else:
            audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"You said: {query}\n")
    except Exception:
        print("Say that again, please...")
        return "None"
    return query


# Main function
def main():
    WAKE = "jarvis"
    if is_windows:
        init_speech_engine_windows()
    else:
        init_speech_engine_linux()

    wishMe()

    # TODO: Feel free to add more responses to this list here
    responses = ["ok", "alright", "sounds good", "hows this", "here you go"]
    while True:
        wakeUp = takeCommands(False).lower()
        if WAKE in wakeUp:

            query = takeCommands(True).lower()

            # Begin looking at what user has said

            if ("timer" or "alarm") in query:
                speak("How many hours")
                hours = int(takeCommands(True).lower())
                speak("How many minutes")
                minutes = int(takeCommands(True).lower())
                speak("How many seconds")
                seconds = int(takeCommands(True).lower())

                if hours > 0:
                    hour = hours * 3600
                else:
                    hour = 0
                if minutes > 0:
                    minute = minutes * 60
                else:
                    minute = 0
                AlarmTime = hour + minute + seconds
                speak("Ok, set an alarm for " + str(hours) + " hours, " + str(minutes) + " minutes, " + str(seconds) + " seconds from now")

                timerFunc = Timer(0.0, timer, [AlarmTime])
                timerFunc.start()

            elif 'open youtube' in query:
                webbrowser.open_new("youtube.com")
            elif 'open stackoverflow' in query:
                webbrowser.open_new("stackoverflow.com")
            elif 'open github' in query:
                webbrowser.open_new("github.com")

            elif 'add event' in query:
                speak("Whats the name?")
                name = takeCommands(True).lower()
                speak("What year?")
                year = int(takeCommands(True).lower())
                speak("What month?")
                month = takeCommands(True).lower()
                speak("What day?")
                day = int(takeCommands(True).lower())
                speak("What time?")
                eventTime = takeCommands(True).lower()

                try:
                    events = json.load(open('events.json'))
                    if type(events) is dict:
                        events = [events]
                    events.append({
                        "name": name,
                        "year": year,
                        "month": month,
                        "day": day,
                        "time": eventTime
                    })
                    with open('events.json', 'w') as outfile:
                        json.dump(events, outfile)
                    speak("OK, event created")
                except FileNotFoundError:
                    events = [{
                        "name": name,
                        "year": year,
                        "month": month,
                        "day": day,
                        "time": eventTime
                    }]
                    with open('events.json', 'w') as outfile:
                        json.dump(events, outfile)
                    speak("OK, event created")

            # If the user wants to know the weather
            elif 'weather' in query or 'temperature' in query:
                speak("For what zipcode would you like the weather?")
                zip = takeCommands(True)
                weather(zip)

            # Basically another wikipedia call, but is like asking a question
            elif 'who is' in query or 'how to' in query or 'what is' in query or 'who was' in query or "what was" in query or "what are" in query:
                if not os.getenv('WOLF_ALPH_KEY'):
                    config.initialize()
                searchResponses = ["Gimme a sec", "Let me look for that", "good question, lets see...", "lets see..."]
                speak(random.choice(searchResponses))
                try:
                    appID = os.getenv('WOLF_ALPH_KEY')
                    client = wolframalpha.Client(appID)
                    res = client.query(query)
                    answer = next(res.results).text
                    speak("Alright, here's what i found")
                    speak(answer)
                except Exception:
                    speak("Hmmm, couldn't find it there. lets try Wikipedia...")
                    resultsw = wikipedia.summary(query, sentences=2)
                    speak("Alright, " + resultsw)
                    speak("That's it")
                    print(resultsw)
                except wikipedia.PageError:
                    speak("Damn. Sorry, I couldn't find what you were looking for.")
                    pass

            # Playing music
            elif 'play music' in query or 'play some music' in query:
                if not os.getenv('MUSIC_PATH'):
                    config.initialize()

                musicDir = os.getenv('MUSIC_PATH')

                # music_dir = ""  # add your music dir
                songs = os.listdir(musicDir)
                chosenSong = random.randint(1, len(songs))
                speak(random.choice(responses))

                slash = "\\"
                if not is_windows:
                    slash = "/"

                os.system(musicDir + slash + songs[chosenSong - 1])
                # os.system(os.path.join(music_dir, songs[1]))

            elif 'the time' in query or 'what is time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            # Opens Firefox, really only works if you have firefox
            # TODO: Support for default browser? idk
            elif 'open firefox' in query:
                speak(random.choice(responses))
                if is_windows:
                    codePathf = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
                    os.startfile(codePathf)
                else:
                    import webbrowser
                    webbrowser.get('firefox').open_new('about:blank')

            elif 'hide window' in query or 'hide work' in query or 'change window' in query or 'minimise window' in query:
                # close in window
                speak(random.choice(responses))
                Minimize = win32gui.GetForegroundWindow()
                win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)

            elif 'full window' in query or 'full screen window' in query or 'fullscreen' in query or 'maximize window' in \
                    query:
                speak(random.choice(responses))
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
                speak(random.choice(responses))

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
