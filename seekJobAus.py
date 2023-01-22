from bs4 import BeautifulSoup
import requests

base_url = 'https://www.seek.com.au'
url = 'https://www.seek.com.au/Power-Bi-jobs-in-healthcare-medical?daterange=999'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-62cc4e82-3e17734461ed9f8237c684d1"}

r = requests.get(url, headers= headers)

links_list = []
soup = BeautifulSoup(r.content , 'lxml')
links = soup.findAll('a', class_= '_1tmgvw5 _1tmgvw8 _1tmgvwb _1tmgvwc _1tmgvwf yvsb870 yvsb87f _14uh994h')

for link in links:
    links_list.append(link['href'])
#print(links_list)

page_url = 'https://www.seek.com.au/job/58062372?type=standard'
r = requests.get(page_url, headers= headers)
soup = BeautifulSoup(r.content, 'lxml')

title = soup.find('h1', class_ = 'yvsb870 _1qw3t4i0 _1qw3t4ih _1d0g9qk4 _1qw3t4im _1qw3t4i1x').text
cmp_name = soup.find('span', class_ = 'yvsb870 _14uh9944u _1qw3t4i0 _1qw3t4i1x _1qw3t4i2 _1d0g9qk4 _1qw3t4ie').text
city_name = soup.findAll('div', class_ = 'yvsb870 _14uh9944y o76g430')[0].text
domain_name = soup.findAll('div', class_ = 'yvsb870 _14uh9944y o76g430')[1].text
salary = soup.findAll('div', class_ = 'yvsb870 _14uh9944y o76g430')[2].text.replace('$', '')
type = soup.findAll('div', class_ = 'yvsb870 _14uh9944y o76g430')[3].text
employment_details = soup.findAll('div', class_ = 'yvsb870 _1v38w810').findall('p')

for p in employment_details:
    print(p)