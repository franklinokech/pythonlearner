import requests

url = 'http://www.webscrapingfordatascience.com/files/kitten.jpg'

r = requests.get(
    url,
    stream=True
)

with open('my_cat_stream.jpg', 'wb') as my_file:
    # Read by 4 KB chunk
    for byte_chunk in r.iter_content(chunk_size=4096):
        my_file.write(byte_chunk)
