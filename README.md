# Pluto
A Python voice assistant

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
Here are some of the features and commands you can use to interact with Pluto. There are also some small Easter eggs to find as you interact with Pluto. 

### Wake Word
To wake up Pluto to take commands, say `Pluto` and you will hear a beep when Pluto is ready for your commands. If Pluto needs some other input in order to carry out a function, such as a zip code for the weather, you will hear a beep when it is ready for your input 

### Start of Day
An option you can set up is a time to run Start-of-Day, a few functions that will run at the same time every day. These functions include giving the weather for the day, going over calendar events/reminders, then play music if you would like. 

Alternatively, you can run Start-of-Day manually by saying something like `Run start of day`

### Timers/Alarms
Here you can have Pluto set a timer that runs in the background. It will ask for the duration of the alarm and then run the timer in the background. 

Say something like `Set a Timer` to set up a timer/alarm.

### Calendars
Here is where Pluto will interact with its onboard calendar. Pluto can add new events to the calendar, list off any events for the day, and deletes old events.

Say something like `Add an Event to the Calendar` to add a new event to the calendar.

Say something like `What are my Events for today?` to here what you have going on today.

#### Note
WIP - Connectivity with Proton Calendar is in the works. Eventually this will be added alongside the onboard calendar.

### Weather
Pluto can look up the local weather for the day, using your zip code. The zip code can be added as an environment variable, or can be requested manually.

Say something like `Whats the Weather like for Today` to hear the current weather

### Internet Functionality
Here you can ask Pluto to search the internet for something, including some math questions, trivia, conversions, and other small requests

Say something like `Who is Dick Freeland` as an example of who someone is

### Music
Pluto will also play music hosted onboard from wherever you tell it to look for music. Pluto will play a random song for you from that music folder

Say something like `Can you Play Some Music` to listen to a random song 

### Sleep
You can tell Pluto that you are going to bed, and it will stop listening for queries for 8 hours. Pluto will then wake up with you and wait for further commands

Simply say `Goodnight` and Pluto will stop listening until the morning

### Loose Lips Sink Ships
Need Pluto to stop listening for a little while? Or maybe you're heading out for work or errands? Whatever your reason, you can now tell Pluto to temporarily stop listening for commands

Tell Pluto to `Take a break` or to `Stop Listening` and it will ask how long to stop listening

### *DESKTOP ONLY*
Some features only make sense when Pluto is running on a desktop. These include taking a screenshot, locking the screen, and minimizing/full screen windows. Because Pluto runs in a terminal window, you can use the `clean` command to clear all the past requests from the session

`Lockdown` will lock your screen. You can still interact with Pluto, but you will need to unlock the screen to interact with the rest of the computer

`Screenshot` prepares the computer to take a screenshot. The user will have to select the area of the screenshot

`Hide window` will minimise the current window

`Fullscreen` will maximize the window

----------------------------------
