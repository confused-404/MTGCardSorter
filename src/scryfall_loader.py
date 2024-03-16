import requests
import json
from PIL import Image
import identifier

scryfall_api_endpoint = "https://api.scryfall.com"

def get_set_info(set_code):
    response = requests.get(scryfall_api_endpoint + "/sets/" + set_code)

    if (response.status_code != 200):
        # print(response.status_code)
        return -1

    return json.loads(response.content)

def get_card(name):
    # print(scryfall_api_endpoint + "/cards/named?fuzzy=" + name.replace(" ", "+"))
    response = requests.get(scryfall_api_endpoint + "/cards/named?fuzzy=" + name.replace(" ", "+") + "&pretty=true")

    if (response.status_code != 200):
        # print(response.status_code)
        return -1

    return json.loads(response.content)

def get_image(card_name, size):
    data = get_card(card_name)
    response = requests.get(data["image_uris"][size], stream=True)

    if (response.status_code != 200):
        # print(response.status_code)
        return -1

    return Image.open(response.raw)

def save_image(card_name, size):
    get_image(card_name, size).save("imgs/raw/" + card_name + ".jpg")
