# Webscraper for the website bol.com to get images and reviews
# Note: this program is specificaly made for an assignment for school and is not made to be used with any other intentions

import requests
from bs4 import BeautifulSoup
import csv

# URL with the prefered product catagory and filter
url_category = 'https://www.bol.com/nl/nl/s/?page=1&searchtext=outdoor+broek+heren&view=tile'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# lijst maken om de links de producten op te slaan
product_pages = []

# De links van de producten in de categorie schrapen en opslaan in de lijst
response = requests.get(url_category, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
product_tags = soup.find_all('div', {'class': 'product-item__image'})

for tag in product_tags:
    page = tag.find('a')['href']
    product_pages.append('https://www.bol.com/' + page)

# CSV-bestand openen om de productinformatie en beoordelingen op te slaan
with open('Output/Bol-product-reviews.csv', 'w', newline='') as csvfile:
        fieldnames = ['product','img', 'title', 'pro', 'cons', 'body']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for page in product_pages:
            url = page
            response = requests.get(url)
            productSoup = BeautifulSoup(response.text, "html.parser")

            productName = productSoup.find("h1", { "class" : "page-heading" })
            productImage = productSoup.find("tagName", { "img" : "data-zoom-image-url" })



