import requests
from bs4 import BeautifulSoup

import json


URLS = ["https://foursouls.com/card-search/?card_type=character", "https://foursouls.com/card-search/page/2/?card_type=character"]
character_urls = []

for URL in URLS:
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find(id="cardGrid")

    characters = results.find_all("div", class_="cardGridCell")


    for character in characters:
        character_url = character.find("a")["href"]
        character_urls.append(character_url)


characters = []

for idx, character_url in enumerate(character_urls):
    page = requests.get(character_url)

    soup = BeautifulSoup(page.content, "html.parser")

    cardpage = soup.find("main")
    character_name = cardpage.find("h1").text
    character_image = cardpage.find("div", id="CardLeft").find("a")["href"]
    stats = cardpage.find_all("td", class_="value")
    character_health = stats[0].text.split(":")[-1].strip()
    character_attack = stats[1].text.split(":")[-1].strip()
    character_set = cardpage.find("div", id="OriginSet").find("p").text
    print(f"{idx+1}/{len(character_urls)} - {character_name}")

    characters.append({
        "name": character_name,
        "image_url": character_image,
        "health": character_health,
        "attack": character_attack,
        "set_group": character_set,
        "eternal_item": None
    })
    

with open("../characters.json", "+w") as file:
    json.dump(characters, file)