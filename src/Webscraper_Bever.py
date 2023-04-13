# Webscraper for the website bever.nl to get images and reviews
# Note: this program is specificaly made for an assignment for school and is not made to be used with any other intentions

import requests
from bs4 import BeautifulSoup
import csv
import json
from urllib.request import urlopen

# De URL van de product categorie wat je wilt bezoeken
url_category = 'https://www.bever.nl/c/heren/schoenen/wandelschoenen.html'

# Headers instellen voor de request
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# lijsten maken om de links en codes van de producten op te slaan
product_links = []
product_codes = []

# De links van de producten in de categorie schrapen en opslaan in de lijst
response = requests.get(url_category, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
product_tags = soup.find_all('div', {'class': 'as-m-product-tile'})
for tag in product_tags:
    link = 'https://www.bever.nl' + tag.find('a')['href']
    code = link.split('-')[-1].split('.')[0]
    product_links.append(link)
    product_codes.append(code)


# CSV-bestand openen om de productinformatie en beoordelingen op te slaan
with open('Output/Bever-product-reviews.csv', 'w', newline='') as csvfile:
        fieldnames = ['product','img', 'score', 'punten']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Loop door alle reviews van alle producten om vervolgens alle aangegeven data scrapen
        for code in product_codes:
                url = code
                response = requests.get(f'https://widgets.reevoo.com/api/product_reviews?per_page=3&trkref=BEV&sku={url}&locale=nl-NL&display_mode=embedded&page=1')


                json_data = response.json()

                name_data = json_data["header"]["title"]
                name = name_data[:len(name_data)-79] + name_data[len(name_data):]
                afbeelding = json_data['header']["product_image"]

                if 'reviews' in json_data["body"]:
                        vorigepunten = 'begin'
                        for review in json_data["body"]['reviews']:
                                score = json_data['body']['reviews'][0]['overall_score']
                                punten = json_data["body"]['reviews'][0]["text"] 
                                if punten != vorigepunten:
                                        writer.writerow({'product': name, 'img': afbeelding, 'score': score, 'punten': punten})
                                        vorigepunten = punten
                                else:
                                        continue
                else:
                        continue
print('Done scraping!')