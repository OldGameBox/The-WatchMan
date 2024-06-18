import pyttsx3

def text_to_speech(input_text):
    engine = pyttsx3.init()
    engine.say(input_text)
    engine.runAndWait()