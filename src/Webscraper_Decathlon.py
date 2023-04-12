# Webscraper for the website Decathlon.nl to get images and reviews.
# Note: this program is specificaly made for an assignment for school and is not made to be used with any other intentions.
# This scraper is meant to be used with only one specific product instead of a product.

import requests
from bs4 import BeautifulSoup
import csv

# Setup the URL of the review section from the Product you want to scrape
url = 'https://www.decathlon.nl/r/halfhoge-waterdichte-bergwandelschoenen-voor-heren-mh500-grijs/_/R-p-X8493840?mc=8493840&c=GRIJS'

# Header to fake the browser
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Generate tags for all the elements within the 'review section'
response = response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
review_tags = soup.find_all('section', {'class': 'review-list svelte-1peidim'})

with open('Output/Decathlon-product-reviews.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['title', 'desc']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    answer_body_tags = soup.find_all('div', {'class': 'answer-body svelte-1v1nczs'})
    for answer_body in answer_body_tags:
        print(answer_body.get_text())
