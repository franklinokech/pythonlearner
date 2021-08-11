import requests

url = 'http://www.webscrapingfordatascience.com/jsonajax/results2.php'

r = requests.post(
    url,
    json={
        'api_code': 'C123456'
    }
)

print(r.request.headers)
print(r.json().get('results'))