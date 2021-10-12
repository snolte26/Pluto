from dotenv import load_dotenv
import os


# TODO: Check for OWM_CITY and/or OWM_ZIPCODE environment variable
def initialize():
    print('\nInitializing Environment...')

    load_dotenv()

    if os.getenv('OWM_KEY') and os.getenv('MUSIC_PATH'):
        # print('\nsetup_env function ran, but Open Weather Map key is already set!')
        # print('OWM_KEY is: ' + os.getenv('OWM_KEY'))
        return

    # If there is no .env file, create it
    if not os.path.exists('./.env'):
        env_file = open('.env', 'w')
        env_file.close()

    if not os.getenv('OWM_KEY'):
        set_new_weather_key()

    if not os.getenv('MUSIC_PATH'):
        set_new_music_path()

    if not os.getenv('WOLF_ALPH_KEY'):
        set_new_wolf_alph_key()

    if not os.getenv('ZIP_CODE'):
        set_zip_code()

    if not os.getenv('SoD_TIME'):
        set_SoD_TIME()


def set_new_weather_key():
    weather_key = input('\nEnter or paste Open Weather Map API key here: ')

    # Recursion here, in case the user doesn't enter any value
    if not weather_key:
        set_new_weather_key()

    print('Setting Open Weather Map API key...')

    # If the file exists and is not empty, append onto a new line
    if os.stat('./.env').st_size == 0:
        env_file = open('.env', 'w')
        env_file.write(f'OWM_KEY={weather_key}')
    else:
        env_file = open('.env', 'a')
        env_file.write(f'\nOWM_KEY={weather_key}')

    env_file.close()

    load_dotenv()

    if os.getenv('OWM_KEY'):
        print('Key has been set to environment!')
    else:
        print('Something went wrong setting OWM key to the environment.')


def set_new_music_path():
    music_path = input('\nEnter or paste music directory here here: ')
    musicPathList = []

    # Recursion here, in case the user doesn't enter any value
    if not music_path:
        set_new_music_path()

    print('Setting Music Directory...')

    for word in music_path.split("\\"):
        musicPathList.append(word)
        musicPathList.append("\\" + "\\")
    musicPathList.pop()
    music_path = "".join(musicPathList)

    # If the file exists and is not empty, append onto a new line
    if os.stat('./.env').st_size == 0:
        print('.env is empty!')
        env_file = open('.env', 'w')
        env_file.write(f'MUSIC_PATH={music_path}')
    else:
        print('.env is not empty!')
        env_file = open('.env', 'a')
        env_file.write(f'\nMUSIC_PATH={music_path}')

    env_file.close()

    load_dotenv()

    if os.getenv('MUSIC_PATH'):
        print('Path has been set to environment!')
    else:
        print('Something went wrong setting Music Path to the environment.')


def set_new_wolf_alph_key():
    wolf_alph_key = input('\nEnter or paste Wolfram Alpha API key here: ')

    # Recursion here, in case the user doesn't enter any value
    if not wolf_alph_key:
        set_new_wolf_alph_key()

    print('Setting Wolfram Alpha API key...')

    # If the file exists and is not empty, append onto a new line
    if os.stat('./.env').st_size == 0:
        env_file = open('.env', 'w')
        env_file.write(f'WOLF_ALPH_KEY={wolf_alph_key}')
    else:
        env_file = open('.env', 'a')
        env_file.write(f'\nWOLF_ALPH_KEY={wolf_alph_key}')

    env_file.close()

    load_dotenv()

    if os.getenv('wolf_alph_key'):
        print('Key has been set to environment!')
    else:
        print('Something went wrong setting Wolfram Alpha key to the environment.')
    pass


def set_zip_code():
    zipCode = input('\nEnter or paste ZIP Code here: ')

    # Recursion here, in case the user doesn't enter any value
    if not zipCode:
        set_zip_code()

    print('Setting zip code...')

    # If the file exists and is not empty, append onto a new line
    if os.stat('./.env').st_size == 0:
        env_file = open('.env', 'w')
        env_file.write(f'ZIP_CODE={zipCode}')
    else:
        env_file = open('.env', 'a')
        env_file.write(f'\nZIP_CODE={zipCode}')

    env_file.close()

    load_dotenv()

    if os.getenv('ZIP_CODE'):
        print('Key has been set to environment!')
    else:
        print('Something went wrong setting Zip Code to the environment.')
    pass


def set_SoD_TIME():
    SoD_TIME = input('\nEnter or paste Start of Day Time here (24 hr i.e. 13:30): ')

    # Recursion here, in case the user doesn't enter any value
    if not SoD_TIME:
        set_SoD_TIME()

    print('Setting SoD_TIME...')

    # If the file exists and is not empty, append onto a new line
    if os.stat('./.env').st_size == 0:
        env_file = open('.env', 'w')
        env_file.write(f'SoD_TIME={SoD_TIME}')
    else:
        env_file = open('.env', 'a')
        env_file.write(f'\nSoD_TIME={SoD_TIME}')

    env_file.close()

    load_dotenv()

    if os.getenv('SoD_TIME'):
        print('Key has been set to environment!')
    else:
        print('Something went wrong setting SoD_TIME to the environment.')
    pass
