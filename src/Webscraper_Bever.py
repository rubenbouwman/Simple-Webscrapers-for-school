# Webscraper for the website bever.nl to get images and reviews
# Note: this program is specificaly made for an assignment for school and is not made to be used with any other intentions

import requests
from bs4 import BeautifulSoup
import csv
import json
from urllib.request import urlopen

# De URL van de product categorie wat je wilt bezoeken
url_category = 'https://www.bever.nl/c/heren/broeken/wandelbroeken.html'

# Headers instellen voor de request
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# lijsten maken om de links en codes van de producten op te slaan
product_links = []
product_codes = []

# CSV-bestand maken/openen om de productinformatie en beoordelingen op te slaan
with open('bever_products.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'score', 'pluspunt', 'minpunt']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

# De links van de producten in de categorie schrapen en opslaan in de lijst
response = requests.get(url_category, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
product_tags = soup.find_all('div', {'class': 'as-m-product-tile'})
for tag in product_tags:
    link = 'https://www.bever.nl' + tag.find('a')['href']
    code = link.split('-')[-1].split('.')[0]
    product_links.append(link)
    product_codes.append(code)

# loop met behulp van de product code door alle reviews van alle producten
for product_code in product_codes:
    response = requests.get(f'https://widgets.reevoo.com/api/product_reviews?per_page=3&trkref=BEV&sku={product_code}&locale=nl-NL&display_mode=embedded&page=1')
    if response.status_code == 200:
        json_data = response.json()

        print(json_data)
    else:
        print('The request failed with status code', response.status_code)


    # writer.writerow({'name': name, 'score': score, 'pluspunt': pluspunt, 'minpunt': minpunt})
