# Webscraper for the website Decathlon.nl to get images and reviews.
# Note: this program is specificaly made for an assignment for school and is not made to be used with any other intentions.

import re
import csv
import requests
from bs4 import BeautifulSoup

# -------------------- Settings --------------------
# the URL of the products you want to scrape
url = 'https://www.decathlon.nl/browse/c0-sporten/c1-hardlopen/c2-hardloopschoenen/_/N-1lxbvp?&Ns=product.averageRating%7C1%7C%7Csku.availability%7C1'
# the amount of pages you want to scrape
product_page = 1
size = 32

# -------------------- Creating the main soup --------------------
reviews = []
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')
product_ids = soup.find_all('a', {'class': 'dpb-product-model-link'})
product_urls = []
product_id_list = []
product_afbeeldingen = []

# get the full links from the products
while product_page <= 2:
    print(f'Getting product_ids... We are at page: {product_page}')
    for product in product_ids:
        url_product_ids = f'https://www.decathlon.nl/browse/c0-sporten/c1-hardlopen/c2-hardloopschoenen/_/N-1lxbvp?&Ns=product.averageRating%7C1%7C%7Csku.availability%7C1&from={size}&size=32'
        response2 = requests.get(url_product_ids, headers=headers)
        soup = BeautifulSoup(response2.content, 'html.parser')
        product_ids_new = soup.find('a', {'class': 'dpb-product-model-link'})
        product_pictures = soup.find('img')['src']
        product_afbeeldingen.append(product_pictures)
        temp_product = product['href']
        product_urls.append(temp_product)
    size += 32
    product_page += 1

# get the ID's from the products so they can be used in the API
for i in product_urls:
    splitted_product = re.findall(r'\b8(?!00)\w+',i)
    product_id_list.append(splitted_product[0])

# -------------------- Scraping & Writing the CSV File --------------------
def get_reviews():

    with open('Output/Decathlon-product-reviews.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Review', 'Afbeelding']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        page_number = 1
        while page_number <= 2:
            print(f'Getting reviews...We are at page: {page_number}')
            for i in product_id_list:
                review_url = f'https://www.decathlon.nl/nl/ajax/nfs/reviews/{i}?page={page_number}&count=500'
                result_afbeeldingen = requests.get(review_url, headers=headers)

                if result_afbeeldingen.status_code != 200:
                    print(f'Request failed with status code {result_afbeeldingen.status_code}')
                    continue

                try:
                    reviews_data = result_afbeeldingen.json()

                    if not reviews_data['reviews']:
                        continue

                    temp_review = reviews_data['reviews'][0]['review']['body']
                    reviews.append(temp_review)
                    for i in product_afbeeldingen:
                        temp_afbeelding = i
                    writer.writerow({'Review': temp_review, 'Afbeelding': temp_afbeelding})
                except Exception as e:
                    continue

            page_number += 1

# -------------------- END --------------------
get_reviews()
print("Done Scraping!")