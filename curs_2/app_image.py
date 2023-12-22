import streamlit as st
import base64
import os
import requests

engine_id = "stable-diffusion-v1-6"
api_host = os.getenv('API_HOST', 'https://api.stability.ai')
api_key = "sk-9LpSxVc0SR8Ks9LN4mwgOyGcNTUNZfWEVQWQCqT0XopoDEJF"

def text_to_image(text):
    if api_key is None:
      raise Exception("Missing Stability API key.")

    response = requests.post(
        f"{api_host}/v1/generation/{engine_id}/text-to-image",
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {api_key}"
        },
        json={
            "text_prompts": [
                {
                    "text": text
                }
            ],
            "cfg_scale": 7,
            "height": 320,
            "width": 320,
            "samples": 1,
            "steps": 30,
        },
    )

    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))

    data = response.json()

    for i, image in enumerate(data["artifacts"]):
        return base64.b64decode(image["base64"])

st.title("Text to Image Generator")

text = st.text_input("Enter some text:")

if st.button("Generate Image"):
    image = text_to_image(text)
    st.image(image)
