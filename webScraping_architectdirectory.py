import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

base_url = 'https://architectdirectory.co.uk'

for i in range(0,3,1):

    page_url = f'https://architectdirectory.co.uk/firms/?p={i+1}'
    headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36", "X-Amzn-Trace-Id": "Root=1-62cc4e82-3e17734461ed9f8237c684d1"}
    print(page_url)

    r = requests.get(page_url, headers=headers)
    soup =  BeautifulSoup(r.content, 'lxml')
    links = soup.findAll('div', class_ = 'firm__title')

    links_list = []
    for link in links:
        links_list.append(base_url+link.a['href'])
#     #print(links_list)

    website_details = []
    for page_link in links_list:

        #test_page_url = 'https://architectdirectory.co.uk/firm/panter-hudspith-architects/'
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
            "X-Amzn-Trace-Id": "Root=1-62cc4e82-3e17734461ed9f8237c684d1"}

        r = requests.get(page_link, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')

        print(page_link)
        title = soup.find('h2', class_ = 'description__title header-2').text
        try:
            email = soup.find('div', class_ = 'description__links').findAll('a')[1]['href']
        except:
            email = None
        #add = soup.find('span', class_ = 'description__contact-content').text
        try:
            add = soup.findAll('div', class_ = 'description__contact')[0].text
        except:
            add = None
        try:
            name = soup.findAll('div', class_ = 'description__contact')[1].text.replace("Contact","")
        except:
            name = None
        try:
            twi = soup.findAll('div', class_ = 'description__contact')[2].text.replace("Twitter","")
        except:
            twi = None
        try:
            ist = soup.findAll('div', class_ = 'description__contact')[3].text.replace("Instagram","")
        except:
           ist = None

        dis_Details = {

            'Name' : title,
            'Page URL' : page_link,
            'Email Address' : email,
            'Contact Person' : name,
            'Address' : add,
            'Twitter User Name' : twi,
            'Instagram User Name' : ist
        }
        website_details.append(dis_Details)
        #print(page_link)
    df = pd.DataFrame(website_details)
    output_path = 'architectdirectory.csv'
    df.to_csv(output_path, mode='a', header=not
    os.path.exists(output_path)
              )