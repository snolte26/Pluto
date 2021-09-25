# PyJARVIS
a python voice assistant

----------------------------------

This script will check for a `.env` file in the project root.
It should contain a line such as:
```
OWM_KEY = <YOUR_API_KEY_HERE>
MUSIC_PATH = <YOUR_MUSIC_PATH_HERE>
WOLF_ALPH_KEY = <YOUR_API_KEY_HERE>
```
Replace `<YOUR_API_KEY>` with your Open Weather Map API key.

Replace `<YOUR_MUSIC_PATH_HERE>` with your Music Directory.

Replace `<YOUR_API_KEY_HERE>` with your Wolfram Alpha API key.

If you don't have an OWM API key yet:
1. Go to https://openweathermap.org/
2. Create an account if you haven't yet
3. Click the [API Keys](https://home.openweathermap.org/api_keys) tab
4. Create a key by naming it and clicking "Generate"

If you dont have a Wolfram Alpha API key yet:
1. Go to https://account.wolfram.com/
2. Create an account if you haven't yet
3. Generate an api key [Here](https://developer.wolframalpha.com/portal/myapps/)

If you don't have this environment variable set, the script will ask for one
on the command line and do all of this for you.

Beepy relies on simpleaudio. Simpleaudio relies on Microsoft Visual C++ 14.0 or greater if on windows. You can download Microsoft Visual C++ [here](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

----------------------------------

## Features/Commands
Here are some of the features and commands you can use to interact with PyJARVIS. There are also some small Easter eggs to find as you interact with JARVIS. 

### Wake Word
To wake up PyJARVIS to take commands, say `Jarvis` and you will hear a beep when JARVIS is ready for your commands. If JARVIS needs some other input in order to carry out a function, such as a zip code for the weather, you will hear a beep when it is ready for your input 

### Timers/Alarms
Here you can have PyJARVIS set a timer that runs in the background. It will ask for the duration of the alarm and then run the timer in the background. 

Say something like `Set a Timer` to set up a timer/alarm.

### Calendars
Here is where PyJARVIS will interact with its onboard calendar. PyJARVIS can add new events to the calendar, list off any events for the day, and deletes old events.

Say something like `Add an Event to the Calendar` to add a new event to the calendar.

Say something like `What are my Events for today?` to here what you have going on today.

#### Note
WIP - Connectivity with Proton Calendar is in the works. Eventually this will be added alongside the onboard calendar.

### Weather
PyJARVIS can look up the local weather for the day, using your zip code. The zip code can be added as an environment variable, or can be requested manually.

Say something like `Whats the Weather like for Today` to hear the current weather

### Internet Functionality
Here you can ask PyJARVIS to search the internet for something, including some math questions, trivia, conversions, and other small requests

Say something like `Who is Dick Freeland` as an example of who someone is

### Music
PyJARVIS will also play music hosted onboard from wherever you tell it to look for music. JARVIS will play a random song for you from that music folder

Say something like `Can you Play Some Music` to listen to a random song 

### *DESKTOP ONLY*
Some features only make sense when PyJARVIS is running on a desktop. These include taking a screenshot, locking the screen, and minimizing/full screen windows. Because JARVIS runs in a terminal window, you can use the `clean` command to clear all the past requests from the session

`Lockdown` will lock your screen. You can still interact with JARVIS, but you will need to unlock the screen to interact with the rest of the computer

`Screenshot` prepares the computer to take a screenshot. The user will have to select the area of the screenshot

`Hide window` will minimise the current window

`Fullscreen` will maximize the window

----------------------------------
