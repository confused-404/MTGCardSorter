import requests
import json

scryfall_api_endpoint = "https://api.scryfall.com"

def get_set_info(set_code):
    response = requests.get(scryfall_api_endpoint + "/sets/" + set_code)

    if (response.status_code != 200):
        # print(response.status_code)
        return -1

    return json.loads(response.content)

def get_card(name):
    # print(scryfall_api_endpoint + "/cards/named?fuzzy=" + name.replace(" ", "+"))
    response = requests.get(scryfall_api_endpoint + "/cards/named?fuzzy=" + name.replace(" ", "+"))

    if (response.status_code != 200):
        print(response.status_code)
        return -1

    return json.loads(response.content)

