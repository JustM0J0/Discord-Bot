import requests
import json
def compliment_me():
    compliment1 = requests.get("https://complimentr.com/api")
    compliment1 = compliment1.json()
    return compliment1['compliment']

