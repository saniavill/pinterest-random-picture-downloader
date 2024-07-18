import json
import os
import requests
import random

with open('pinz3.json', encoding="UTF-8") as f: #open your json file. mine contains a random board's info. namely the url pics, description etc
    data = json.load(f)

picture_links = [] #for all the links

for item in data['pictures']:
    picture_links.append(item["image/url"]) #access the links in the json file and put them inside the list

def _random_link_picker():
    randlink = random.choice(picture_links)
    return randlink


def download_image():
    filename = 'picture.jpg' #to waste less storage, every time you run this file the new image replaces the image that was downloaded before
    imageurl = _random_link_picker()
    image_response = requests.get(imageurl, stream=True)
    if image_response.status_code == 200:
        with open(filename, "wb") as image_file:
            for chunk in image_response:
                image_file.write(chunk)


download_image()
