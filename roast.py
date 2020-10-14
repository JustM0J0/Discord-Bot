import requests
import json
def roast_me():
    roast = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
    roast = roast.json()
    return roast["insult"]
