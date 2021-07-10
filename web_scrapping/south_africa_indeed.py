import pandas as pd
import requests
from bs4 import BeautifulSoup


def extract(page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 OPR/77.0.4054.203'
    }
    url = f'https://za.indeed.com/jobs?q=South+Africa&start={page}'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    return soup


def transform(soup):
    divs = soup.find_all('div', class_='slider_item')

    for item in divs:
        try:
            title = item.find('h2', class_='jobTitle').find_all('span')[1].text.strip()
        except:
            title = ''
        company = item.find('span', class_='companyName').text.strip()

        salary_element = item.find('span', class_='salary-snippet')

        if salary_element:
            salary = salary_element.text.strip()
        else:
            salary = ''

        summary = item.find('div', class_='job-snippet').text.strip().replace('\n', '')

        job = {
            'title': title,
            'company': company,
            'salary': salary,
            'summary': summary,
        }

        joblist.append(job)

    return


joblist = []

for i in range(0, 41, 10):
    print(f'Getting page {i} ')
    c = extract(i)
    transform(c)

df = pd.DataFrame(joblist)
print(df.head)
df.to_csv('jobs.csv', index=False)
