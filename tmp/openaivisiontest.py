from openai import OpenAI
import base64

import copykitten


def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')


def openai_image_reponse(API_KEY):

# Path to your image
    image_path = "./cropped_screenshot.png"

# Getting the base64 string
    base64_image = encode_image(image_path)

    client = OpenAI(api_key=API_KEY)

    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
        "role": "user",
        "content": [
            {"type": "text", "text": "Please answer question in this image."},
            {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/png;base64,{base64_image}",
            },
            },
        ],
        }
    ],
    max_tokens=300,
    )

    print(response.choices[0])
    #copykitten.copy(response.choices[0])

if __name__ == "__main__":
    openai_image_reponse("sk-1234567890abcdef1234567890abcdef")
    
