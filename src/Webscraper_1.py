# Webscraper for the website bever.nl to get images and reviews
# Note: this program is specificaly made for an assignment for school and is not made to be used with any other intentions

import requests
from bs4 import BeautifulSoup
import selenium
import csv

# Setup the url you want to visit
url = 'https://www.bever.nl/c/heren/jassen/hardshell.html'

# Setup the header to act like a real browser
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Get the HTML contents
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# Get all the selected tags
product_tags = soup.find_all('div', {'class': 'as-m-product-tile'})

# Loop through the tags to find the content that you want
with open('bever_products.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'price', 'description']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for tag in product_tags:
        name = tag.find('div', {'class': 'as-m-product-tile__title-wrapper'}).text.strip()
        price = tag.find('div', {'class': 'as-a-price__value as-a-price__value--sell'}).text.strip()
        description = tag.find('div', {'class': 'as-m-product-tile__info-wrapper'}).text.strip()
        writer.writerow({'name': name, 'price': price, 'description': description})