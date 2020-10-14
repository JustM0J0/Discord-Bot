import requests
import json
def quote_content():
    quote = requests.get("https://api.quotable.io/random")
    quote = quote.json()
    return f"{quote['content']} \n~{quote['author']}"

