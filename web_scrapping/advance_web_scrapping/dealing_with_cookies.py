import requests

url = 'http://www.webscrapingfordatascience.com/cookielogin/'

# do a post request to the url
r = requests.post(
    url,
    data={
        'username': 'dummy',
        'password': '1234',
    }
)

# get cookie values
my_cookies = r.cookies

# perform a post request
r = requests.post(
    url + 'secret.php',
    cookies=my_cookies,
)

print(r.text)
