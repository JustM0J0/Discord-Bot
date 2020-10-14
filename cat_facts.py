import requests
import json


def cat_fact():
    fact = requests.get("https://meowfacts.herokuapp.com/")

    fact = fact.json()


    return fact["data"][0]

cat_fact()
