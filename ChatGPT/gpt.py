import cv2
import base64
import requests
import pyttsx3

camera = cv2.VideoCapture(0)

api_key = open('../openai.api', 'r').read()

# ret, image = camera.read()
# cv2.imwrite('captured_image.jpg', image)

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


payload = {
    "model": "gpt-4o",
    "messages": [
        {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    "text": "You will receive images of different objects. You must identify and describe ONLY THE MAIN OBJECT in the middle of image in details. If you cannot identify an object, you MUST ONLY SAY: 'IDENT_ERROR'. Start by saying: 'I see...'"
                }
            ]
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encode_image('captured_image.jpg')}"
                    }
                }
            ]
        }
    ],
    "max_tokens": 300
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

text_to_speech(response.json()['choices'][0]['message']['content'])
