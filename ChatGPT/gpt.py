import cv2
import base64
import requests

api_key = open('openai.api', 'r').read()
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}


def scan(camera: cv2.VideoCapture, debug: bool = False) -> str:
    _, image = camera.read()
    cv2.imwrite('captured_image.jpg', image)
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=generate_payload())
    if debug: print("Scan Result:" + response.json()['choices'][0]['message']['content'])
    return response.json()['choices'][0]['message']['content']


def generate_payload() -> dict:
    return {
        "model": "gpt-4o",
        "messages": [
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": "You will receive images of different objects. You must identify and describe ONLY THE MAIN OBJECT in the middle of image. Use ONLY around 2-3 sentences. If you cannot identify an object, you MUST ONLY RESPOND: 'IDENT_ERROR'. Start by saying: 'I see...'"
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


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


if __name__ == "__main__":
    api_key = open('../openai.api', 'r').read()
    camera = cv2.VideoCapture(0)
    scan(camera, True)
