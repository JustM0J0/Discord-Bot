import requests
import json
def useless_fact():
    fact = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
    fact = fact.json()
    return fact["text"]

useless_fact()
