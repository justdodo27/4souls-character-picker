import requests
from bs4 import BeautifulSoup


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

for character_url in character_urls:
    page = requests.get(character_url)

    soup = BeautifulSoup(page.content, "html.parser")

    cardpage = results.find_all("div", class_="cardpage")

    character_name = cardpage.find("h1").text
    print(character_name)
    