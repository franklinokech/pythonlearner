import requests
from bs4 import BeautifulSoup


url = 'http://www.webscrapingfordatascience.com/complexjavascript/'

my_cookies = {
    'nonce': '1278',
    'PHPSESSID': '4qm02bt6jn4qmh4220i1pko2jt',
}

r = requests.get(
    url + 'quotes.php',
    params={
        'p': '0',
    },
    cookies=my_cookies,
)

print(r.text)
