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
