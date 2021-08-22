import ctypes
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import win32gui
import win32con
import requests
import pyautogui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # 0 is male, 1 is female. I went with female. -snolte26
engine.setProperty('rate', 155)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening")

    speak("I am JARVIS, how may I help you?")


def weather():

    base = "https://api.openweathermap.org/data/2.5/weather?"
    city = "Your City Here!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    apiKey = "Your API Key Here!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    url = base + "q=" + city + "&appid=" + apiKey
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        tmpma = main['temp']
        humidity = main['humidity']
        temperature = int((((tmpma - 273.15) * 9) / 5) + 32)
        tmpmax = main['temp_max']
        tmpmin = main['temp_min']
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


def main():
    wishMe()
    while True:
        query = takeCommands().lower()

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

        elif 'weather' in query or 'temperature' in query or 'today reports' in query:
            weather()

        elif 'who is' in query or 'how to' in query or 'what is' in query:
            speak('Searching Wikipedia...')
            resultsw = wikipedia.summary(query, sentences=2)
            speak("Sir, " + resultsw)
            speak("That's it")
            print(resultsw)

        elif 'play music' in query:
            music_dir = "C:\\Users\\13174\\PycharmProjects\\MusicPlayer\\Music"  # add your music dir
            songs = os.listdir(music_dir)
            chosenSong = random.randint(1, len(songs))
            os.system(music_dir + "\\" + songs[chosenSong-1])
            # os.system(os.path.join(music_dir, songs[1]))
            speak('ok sir. playing ' + songs[chosenSong-1])

        elif 'the time' in query or 'what is time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open firefox' in query:
            speak("opening firefox ")
            codePathf = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
            os.startfile(codePathf)

        elif 'hide window' in query or 'hide work' in query or 'change window' in query or 'minimise window' in query:
            # close in window
            speak("ok.")
            Minimize = win32gui.GetForegroundWindow()
            win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)

        elif 'full window' in query or 'full screen window' in query or 'fullscreen' in query or 'maximize window' in\
                query:
            # full in window
            speak("sure.")
            hwnd = win32gui.GetForegroundWindow()
            win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)

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

        elif 'clean' in query:
            speak("ok.")

            def clear():
                return os.system('cls')

            clear()

        elif 'what can you do' in query:
            speak("I can give you the time, give info from wikipedia, give you the weather, play music, lock things "
                  "down, open certain pages, take screenshots, and other small tasks. I try to help you where I can")


if __name__ == '__main__':
    main()
