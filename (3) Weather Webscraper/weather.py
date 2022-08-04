import requests
from bs4 import BeautifulSoup as soup

print("This is a webscraper to check the weather of a specific place.")
place = input("Please enter a location: ").replace(" ", "+").title()
modification = place + "+weather"
url = "https://www.google.com/search?q=" + modification

req = requests.get(url)
save = soup(req.text, "html.parser")
update = save.find("div", {"class": "BNeawe"})
print("")
print("The current weather in " + place.replace("+", " ") + " is " + update.string + ".")
