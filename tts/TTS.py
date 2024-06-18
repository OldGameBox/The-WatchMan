import pyttsx3


while 0 == 0:
    def text_to_speech(text):
         speech = input(text)
         engine = pyttsx3.init()
         engine.say(speech)
         engine.runAndWait()

    text_to_speech()