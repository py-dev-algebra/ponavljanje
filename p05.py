import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup


if load_dotenv():
    url = os.getenv('URL')

for i in range(50):
    url = f'https://books.toscrape.com/catalogue/page-{i + 1}.html'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        book_titles = soup.section.find_all('a')
        for title in book_titles:
            if title.get('title') is not None:
                print(title.get('title'))
                # pohraniti u bazu, datoteku, rjecnik, listu i sl.

        book_prices = soup.find_all(class_='price_color')
        for price in book_prices:
            print(price.string.replace('Â', ''))
            # dodaj uz knjigu u bazu, datoteku, rjecnik, listu i sl.
