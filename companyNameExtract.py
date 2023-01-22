import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

base_url = 'https://finder.startupnationcentral.org'

for i in range(0, 1):
    url = f'https://finder.startupnationcentral.org/company/search?&page={i+1}'
    print(url)
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36", "X-Amzn-Trace-Id": "Root=1-62cc4e82-3e17734461ed9f8237c684d1"}

    r = requests.get(url, headers= header)
    soup = BeautifulSoup(r.content,'lxml')
    link_tb = soup.findAll("div", { "id" : "main-table-content" })[0]
    links = link_tb.findAll('a', href=True)
    tb_link_list = []
    #print(links['href'])
    for link in links:
        tb_link_list.append(base_url + link['href'])
        #page_url.append(tb_link_list[:50])
    #print(tb_link_list[:50])

    # unwanted_str = '/company/search'
    # new_list = [item for item in tb_link_list if unwanted_str not in item] #remove unwant string from list
    # #print(tb_link_list.append(new_list[:-2]))

    #page_url = 'https://finder.startupnationcentral.org/company_page/abracadabra-implants-ltd'
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36", "X-Amzn-Trace-Id": "Root=1-62cc4e82-3e17734461ed9f8237c684d1"}
    finder_cmp_details = []

    for cmp_dt in tb_link_list[:50]:
        r = requests.get(cmp_dt, headers= header)
        soup = BeautifulSoup(r.content, 'lxml')
        print(cmp_dt)
        try:
            c_name = soup.find('h1', class_= 'company-profile-name').text.strip()
        except:
            c_name = 'None'
        try:
            linkedIn = soup.find('div', {"id" : "social-links-icons-container"})
            linked_links = linkedIn.find('a', href=True)
        except:
            linked_links = 'None'
        cmp_details = {
            'link': cmp_dt,
            'Company Name' : c_name,
            'LinkedIn Url' : linked_links['href']
        }
        finder_cmp_details.append(cmp_details)
        #print(cmp_details['Company Name'])
        #print(cmp_details['LinkedIn Url'])
    df = pd.DataFrame(finder_cmp_details)
    output_path = 'finder_startupnationcentral.csv'
    df.to_csv(output_path, mode='a', header = not
                os.path.exists(output_path)
              )
