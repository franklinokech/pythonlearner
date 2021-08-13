import requests

url = 'http://www.webscrapingfordatascience.com/simplejavascript/quotes.php'

r = requests.get(url, cookies={
    'jsenabled': '1',
})

print(r.json())