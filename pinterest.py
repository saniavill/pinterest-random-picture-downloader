import json
import os
import requests
import random

with open('pinz3.json', encoding="UTF-8") as f: #open your json file
    data = json.load(f)

picture_links = []

for item in data['pictures']:
    picture_links.append(item["image/url"])

def _random_link_picker():
    randlink = random.choice(picture_links)
    return randlink


def download_image():
    filename = 'picture.jpg'
    image_url = _random_link_picker()
    image_response = requests.get(image_url, stream=True)
    if image_response.status_code == 200:
        with open(filename, "wb") as image_file:
            for chunk in image_response:
                image_file.write(chunk)


download_image()
