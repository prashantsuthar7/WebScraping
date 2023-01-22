import requests
from bs4 import BeautifulSoup

url = 'https://distilling.com/distilleries/page/2/?_employer_name&_product_types&_employer_location&_employer_city&_proof_gallons_per_year'

r = requests.get(url)
soup = BeautifulSoup(r.text,'lxml')
links = soup.select('div.facetwp-template li a')

link_ls = []

for link in links:
    link_list = link.attrs['href']
    link_ls.append(link_list)

distory_url = 'https://distilling.com/distillery/3-badge-beverage-corporation-65468358/'

r = requests.get(distory_url)
soup = BeautifulSoup(r.text,'lxml')

title = soup.select_one('h1.entry-title')
#address = soup.select_one('div.distillery-info span')

print(title)