import pyttsx3 as speech


def speak(text):
    speech_engine = speech.init()
    speech_engine.say(text)
    speech_engine.runAndWait()
