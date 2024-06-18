import pyttsx3


while 0 == 0:
    def text_to_speech():
         speech = input("What do you want to be said?: ")
         engine = pyttsx3.init()
         engine.say(speech)
         engine.runAndWait()

    text_to_speech()