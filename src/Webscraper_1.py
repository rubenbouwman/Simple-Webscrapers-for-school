import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.bever.nl/c/heren/jassen/hardshell.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

product_tags = soup.find_all('div', {'class': 'as-m-product-tile'})

