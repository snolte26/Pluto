# Importing necessary modules
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

# Set up environment if needed
if not os.path.exists('./.env') or not os.getenv('OWM_KEY'):
    setup.init_env()

# Looks for a .env file and loads it.
# See: https://pypi.org/project/python-dotenv/
load_dotenv()

# Setting up the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0 is male, 1 is female. I went with female. -snolte26
engine.setProperty('rate', 155)


# Takes string input, then outputs that string as speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Checks the current time, then speaks the result
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening")

    speak("I am JARVIS, how may I help you?")


# Weather function
def weather(zip):
    # Beginning of the API calling url
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

    # Setting the API key froom the .env file
    apiKey = os.getenv('OWM_KEY')

    # Putting together API calling url, with the base, zip code from earlier, and API key, then sends a request to
    # the url
    url = base + "zip=" + zip + "&appid=" + apiKey
    response = requests.get(url)

    # If the response is successful, get the data requested from the JSON
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
        # Speaking the requested data from weather request
        speak(f"Sir, the current temperature is {temperature} Degrees Fahrenheit")
        speak(f"and {report[0]['description']}")
        speak(f"The humidity is currently {humidity}%")
        speak(f"The high for today is {tempMax} degrees and a low of {tempMin} degrees")
    else:
        # If cannot give weather, or something goes wrong, display and speak this
        print("no data today")
        speak("Sorry, I cant find any weather data right now")


# Listening to the command
def takeCommands():
    # Setting up microphone
    r = sr.Recognizer()

    # Listening to noise input
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    # Attempts to recognise what was said
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    # If it cannot recognise what you said, returns nothing
    except Exception:
        print("Say that again, please...")
        return "None"
    # Returns what you said if it could recognise what you said
    return query


# Main function
def main():
    wishMe()
    # After wishMe(), starts listening, then does something if it hears a trigger
    while True:
        # Gets query from user
        query = takeCommands().lower()

        # Begin looking at what user has said

        # if the user said wikipedia, search wikipedia for whatever was also said in the request, and output the
        # result from the wiki page
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("Sir, " + results)
            print(results)

        # Open Youtube, stackoverflow, or github
        elif 'open youtube' in query:
            webbrowser.open_new("youtube.com")
        elif 'open stackoverflow' in query:
            webbrowser.open_new("stackoverflow.com")
        elif 'open github' in query:
            webbrowser.open_new("github.com")

        # If the user wants to know the weather
        elif 'weather' in query or 'temperature' in query:
            # Get the zip code from the user
            speak("For what zipcode would you like the weather?")
            zip = takeCommands()
            # send the zip code to the weather() function
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
            # Setting music directory
            # TODO: Add music directory to environment variables
            music_dir = "C:\\Users\\13174\\PycharmProjects\\MusicPlayer\\Music"  # add your music dir
            # Get list of songs in that directory
            songs = os.listdir(music_dir)
            # Pick a random song
            chosenSong = random.randint(1, len(songs))
            # Announce the chosen song, and start playing it
            speak('ok sir. playing ' + songs[chosenSong - 1])
            os.system(music_dir + "\\" + songs[chosenSong - 1])
            # os.system(os.path.join(music_dir, songs[1]))

        # Returns the current time
        elif 'the time' in query or 'what is time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        # Opens Firefox, really only works if you have firefox
        # TODO: Support for default browser? idk
        elif 'open firefox' in query:
            speak("opening firefox ")
            codePathf = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
            os.startfile(codePathf)

        # Hide/minimize the current window
        elif 'hide window' in query or 'hide work' in query or 'change window' in query or 'minimise window' in query:
            # close in window
            speak("ok.")
            Minimize = win32gui.GetForegroundWindow()
            win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)

        # Maximizes the current window
        elif 'full window' in query or 'full screen window' in query or 'fullscreen' in query or 'maximize window' in \
                query:
            # full in window
            speak("sure.")
            hwnd = win32gui.GetForegroundWindow()
            win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)

        # Locks the screen, essentially like pressing "Win + L"
        # <>Pretty proud of this one, ngl. -snolte26</>
        elif 'lockdown' in query or 'lock everything down' in query or 'lock down' in query:
            speak("Locking things down...")
            ctypes.windll.user32.LockWorkStation()
            speak("Locked down, I'll be waiting")

        # Sets up a screenshot
        elif 'screenshot' in query or 'screen shot' in query:
            speak("Screenshot, coming up...")
            pyautogui.hotkey('win', 'shift', 's')

        # Small talk with PyJARVIS
        elif 'who are you' in query or 'about you' in query or "your details" in query:
            speak("i am JARVIS, your work partner. I'm all ear's")

        # Blah blah blah, who cares? Its small talk with a bot
        elif 'how are you' in query:
            speak("I am doing alright. How can i help you?")

        # closes PyJarvis
        elif 'exit' in query or 'goodbye' in query or 'good bye' in query or 'bye' in query:
            speak("thank you, see you later")
            quit()

        # More small talk, allows you to be polite with an AI
        elif 'thank you' in query or 'thanks' in query:
            speak("No problem sir.")

        # Even more small talk
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

        # Gives a brief description of what PyJarvis can do
        elif 'what can you do' in query:
            speak("I can give you the time, give info from wikipedia, give you the weather, play music, lock things "
                  "down, open certain pages, take screenshots, and other small tasks. I try to help you where I can")


# run main(), is start of script
if __name__ == '__main__':
    main()
