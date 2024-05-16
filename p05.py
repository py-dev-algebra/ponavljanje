import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup


if load_dotenv():
    url = os.getenv('URL')

print(url)