import requests

url = 'http://www.webscrapingfordatascience.com/trickylogin/'

my_session = requests.session()

# set global headers
my_session.headers.update(
    {
        'User-Agent': 'Chrome!',
    }
)

# all requests will now use this user-agent
r = my_session.post(
    url
)

print(r.request.headers)

r = my_session.post(
    url,
    params={
        'p': 'login',
    },
    data={
        'username': 'dummy',
        'password': '1234',
    }
)

print(r.request.headers)

r = my_session.get(
    url,
    params={
        'p': 'protected',
    }
)

print(r.request.headers)