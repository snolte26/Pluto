# PyJARVIS
a python voice assistant

----------------------------------

This script will check for a `.env` file in the project root.
It should contain a line such as:
```
OWM_KEY = <YOUR_API_KEY_HERE>
MUSIC_PATH = <YOUR_MUSIC_PATH_HERE>
```
Replace `<YOUR_API_KEY>` with your Open Weather Map API key.

Replace `<YOUR_MUSIC_PATH_HERE>` with your Music Directory.

If you don't have one yet:
1. Go to https://openweathermap.org/
2. Create an account if you haven't yet
3. Click the [API Keys](https://home.openweathermap.org/api_keys) tab
4. Create a key by naming it and clicking "Generate"

If you don't have this environment variable set, the script will ask for one
on the command line and do all of this for you.

----------------------------------
