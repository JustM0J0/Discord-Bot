import requests
import json


def defined(word1):
    word = requests.get(f"https://owlbot.info/api/v4/dictionary/{word1}", headers = {"Authorization": "Token ********************************"})
    word = word.json()
    return word["definitions"]

