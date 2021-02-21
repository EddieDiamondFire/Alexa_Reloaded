import speech_recognition as sr

microphone = sr.Microphone()
recogniser = sr.Recognizer()


def check_version():
    return sr.__version__


def start_alexa_program():
    print("")


def end_alexa_program():
    print("")


def run_alexa():

def voice_command():
    try:
        with microphone as origin:
            r = recogniser
            audio = r.listen(origin)
            translate = r.recognize_google(audio)

            print("You said " + str(translate))
            translate = translate.lower()

            if 'alexa' in translate:
                translate = translate.replace('alexa', '')
                return translate
    except sr.UnknownValueError:
        print("Sorry I could not recognise your voice")
        run_alexa()



