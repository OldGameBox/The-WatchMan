import pyttsx3

def text_to_speech(text):
     speech = input(text)
     engine = pyttsx3.init()
     engine.say(speech)
     engine.runAndWait()

if __name__ == "__main__":
    print("hi")