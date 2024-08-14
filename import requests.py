import requests
from bs4 import BeautifulSoup

url = "https://www.realestate.com.au/rent/in-gold+coast,+qld/list-1"

response = requests.get(url)
print(response)