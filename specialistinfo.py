from bs4 import BeautifulSoup
import requests

base_url = 'https://www.specialistinfo.com/'

page_url = 'https://www.specialistinfo.com/gp_find.php?range=A&def=0&scope=1&type=1'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-62cc4e82-3e17734461ed9f8237c684d1"}

r = requests.get(page_url, headers= headers)
soup = BeautifulSoup(r.content, 'lxml')
table = soup.findAll('table')[2]
links = table.findAll('a')

page_links = []
for link in links:
    page_links.append(base_url+link['href'])
#print(page_links)

#test_url = 'https://www.specialistinfo.com/gpget.php?ftype=dt&town=Abbots Bromley'
for page_link in page_links:
    r = requests.get(page_link, headers= headers)
    soup = BeautifulSoup(r.content, 'lxml')
    table = soup.findAll('table')[3]
    #td = table.findAll('td', class_ = 'gp')

    tr = table.findAll('tr')

    list_name = []
    ct = 0
    for ttr in tr:
        try:
            name = ttr.find('div', class_ = 'data').text
            list_name.append(name)
            print(len(list_name))
            #print(len(name))
        except:
            name = 'Nan'