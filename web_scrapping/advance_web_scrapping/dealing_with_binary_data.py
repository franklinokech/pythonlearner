import requests

url = 'http://www.webscrapingfordatascience.com/files/kitten.jpg'

r = requests.get(
    url,
)

with open('my_cat.jpg','wb') as my_file:
    my_file.write(r.content)