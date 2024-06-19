from tts import TTS
from ChatGPT import gpt
import cv2 as cv

if __name__ == "__main__":
    camera = cv.VideoCapture(0)
    while True:
        _, image = camera.read()
        cv.imshow("The WatchMan [Prototype]", image)
        if cv.waitKey(1) == 32:
            TTS.text_to_speech(gpt.scan(camera, True))
        if cv.waitKey(1) == ord('q'):
            break
    camera.release()
    cv.destroyAllWindows()
