import requests
from bs4 import BeautifulSoup

# create session object
my_session = requests.session()

url = 'http://www.webscrapingfordatascience.com/complexjavascript/'

# get the main page first, to obtain the PHPSESSID

r = my_session.get(url)

# manually set the nonce cookie

my_session.cookies.update(
    {
        'nonce': '1278',
    }
)

r = my_session.get(
    url + 'quotes.php',
    params={
        'p': '0',
    },
)

print(r.text)
