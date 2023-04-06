import requests
from bs4 import BeautifulSoup
import csv

class WebscraperBever:
    def makeConnection():
        url = 'https://www.bever.nl/c/heren/jassen/hardshell.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
            }
        response = requests.get(url, headers=headers)

    def getTags(response):
        soup = BeautifulSoup(response.content, 'html.parser')
        product_tags = soup.find_all('div', {'class': 'as-m-product-tile'})

    def loopTroughTags(product_tags):
        with open('bever_products.csv', 'w', newline='') as csvfile:
            fieldnames = ['name', 'price', 'description']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for tag in product_tags:
                name = tag.find('div', {'class': 'as-m-product-tile__title-wrapper'}).text.strip()
                price = tag.find('div', {'class': 'as-a-price__value as-a-price__value--sell'}).text.strip()
                description = tag.find('div', {'class': 'as-m-product-tile__info-wrapper'}).text.strip()
                writer.writerow({'name': name, 'price': price, 'description': description})