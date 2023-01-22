import requests
from bs4 import BeautifulSoup

base_url = 'https://www.nysenate.gov/senators-committees'

r = requests.get(base_url)
soup = BeautifulSoup(r.content, 'lxml')

containers = soup.findAll('div', class_ = 'first u-odd')

for i in range(1,136):
    if (i % 2) == 0:
        container = soup.findAll('div', class_ = 'u-even')
    else:
        container = soup.findAll('div', class_ = 'u-odd')

for containerss in container:
    print(containerss)