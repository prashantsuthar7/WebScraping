from bs4 import BeautifulSoup
import requests

base_url = 'https://www.ibba.org/find-a-business-broker/'

r = requests.get(base_url)
soup = BeautifulSoup(r.content, 'lxml')

state = soup.findAll('div', class_ = 'statescontainer')

print(state)