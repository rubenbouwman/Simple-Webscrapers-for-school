# Webscraper for the website Decathlon.nl to get images and reviews.
# Note: this program is specificaly made for an assignment for school and is not made to be used with any other intentions.
# This scraper is meant to be used with only one specific product instead of a product.

import requests
from bs4 import BeautifulSoup
import csv
import json
from urllib.request import urlopen

# -------------------- Settings --------------------
# the URL of the product you want to scrape
url = 'https://www.decathlon.nl/r/halfhoge-waterdichte-bergwandelschoenen-voor-heren-mh500-grijs/_/R-p-X8493840?mc=8493840&c=GRIJS'
product_code = 'X8493840' #----------------------------------------------------------------------------^^^^^^^^ this code
# the amount of review pages you want to scrape
pageStart = 1
pageEnd = 10

# -------------------- Functionalities --------------------
# Header to fake the browser
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

with open('Output/Decathlon-product-reviews.csv', 'w', newline='') as csvfile:
    fieldnames = ['title', 'desc']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for page in range(pageStart, pageEnd+1):
        response = requests.get(f'https://www.decathlon.nl/nl/ajax/nfs/reviews/{product_code}?page={page}&count=500')
        json_data = response.json()
        print(json_data)
   
# -------------------- End --------------------
print('Done scraping!')