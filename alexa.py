import datetime

import speech_recognition as sr
from common import speech_engine as se

microphone = sr.Microphone()
recogniser = sr.Recognizer()


def check_version():
    return sr.__version__


def start_alexa_program():
    run_alexa()


def end_alexa_program():
    print("")
    print("Stopping session")
    exit()


def run_alexa():
    while True:
        command = voice_command()

        if command is not None:
            time_possibilities = ['is the time', 'time', 'what is the time']

            for x in time_possibilities:
                if x in command:
                    time = datetime.datetime.now().strftime('%H:%M:%S')

                    text = "The current time is {}".format(time)
                    se.speak(text)
                    print(text)
                    break
        elif command is None:
            print("I cannot hear what you have said")
            se.speak("Sorry, I cannot hear what you have said")
            continue


def voice_command():
    try:
        with microphone as source:
            print("Alexa is Listening.......")
            voice = recogniser.listen(source)
            response = recogniser.recognize_google(voice)
            print("You said: " + response)

            response = response.lower()

            if 'alexa' in response:
                response = response.replace('alexa', '')

                speak = "Okay, I will {}".format(response)
                print(speak)
                se.speak(speak)
                return response

    except:
        print("Alexa cannot recognise your voice")
        se.speak("I cannot recognise your voice")
        return None
