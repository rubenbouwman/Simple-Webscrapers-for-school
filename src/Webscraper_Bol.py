# Webscraper for the website bol.com to get images and reviews
# Note: this program is specificaly made for an assignment for school and is not made to be used with any other intentions

import requests
from bs4 import BeautifulSoup
import csv

# URL with the prefered product catagory and filter
url_category = 'https://www.bol.com/nl/nl/l/outdoorschoenen/39510/?page=1'
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

            review_tags = productSoup.find_all('li', {'class': 'review js-review'})

            for tag in review_tags:
                # extract rating
                score = tag.select_one('.star-rating')['aria-label']
                
                # extract review title
                title = tag.select_one('.review__title').text.strip()
                
                # extract review body
                body = tag.select_one('[data-test="review-body"]').text.strip()
                body = body.encode('utf-8', 'ignore').decode('utf-8')
                
                # extract pros and cons
                pros_list = tag.select('.review-pros-and-cons__list--pros li')
                pros = [li.text.strip() for li in pros_list]
                
                cons_list = tag.select('.review-pros-and-cons__list--cons li')
                cons = [li.text.strip() for li in cons_list]
                
                # write everything into the CSV file
                writer.writerow({'product': productName, 'img': productImage, 'score': score, 'title': title, 'pros': pros, 'cons': cons, 'body': body})



