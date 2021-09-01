from dotenv import load_dotenv
import os

# TODO: Check for OWM_CITY and/or OWM_ZIPCODE environment variable
def init_env():
    print('\nInitializing Environment...')

    load_dotenv()

    if os.getenv('OWM_KEY'):
        print('\nsetup_env function ran, but Open Weather Map key is already set!')
        print('OWM_KEY is: ' + os.getenv('OWM_KEY'))
        return

    # If there is no .env file, create it
    if not os.path.exists('./.env'):
        env_file = open('.env', 'w')
        env_file.close()

    set_new_weather_key()


def set_new_weather_key():
    weather_key = input('\nEnter or paste Open Weather Map API key here: ')

    # Recursion here, in case the user doesn't enter any value
    if not weather_key:
        set_new_weather_key()

    print('Setting Open Weather Map API key...')

    # If the file exists and is not empty, append onto a new line
    if os.stat('./.env').st_size == 0:
        print('.env is empty!')
        env_file = open('.env', 'w')
        env_file.write(f'OWM_KEY={weather_key}')
    else:
        print('.env is not empty!')
        env_file = open('.env', 'a')
        env_file.write(f'\nOWM_KEY={weather_key}')

    env_file.close()

    if os.getenv('OWM_KEY'):
        print('Key has been set to environment!')
    else:
        print('Something went wrong setting OWM key to the environment.')
