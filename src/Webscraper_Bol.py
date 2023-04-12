# Webscraper for the website bol.com to get images and reviews
# Note: this program is specificaly made for an assignment for school and is not made to be used with any other intentions

import requests
from bs4 import BeautifulSoup
import csv

url_category = 'https://www.bol.com/nl/nl/s/?page=1&searchtext=outdoor+broek+heren&view=tile'