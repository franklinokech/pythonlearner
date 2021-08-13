import requests
from bs4 import BeautifulSoup
url = 'http://www.webscrapingfordatascience.com/simplejavascript/'
r = requests.get(url)

htm_soup = BeautifulSoup(r.text,'html.parser')

# no ul tag here
ul_tag = htm_soup.find('ul')

print(ul_tag)

# show js code
script_tag = htm_soup.find('script', attrs={'src': None})

print(script_tag)

