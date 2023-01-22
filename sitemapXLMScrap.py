#UC Health web site scraping using robot.txt and sitemap.xml
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

url = 'https://www.uchealth.org/provider/uch_provider-sitemap.xml'

r = requests.get(url)
# print(r)

soup = BeautifulSoup(r.text, 'lxml')
links = soup.find_all('loc')

doc_links = []

for link in links:
     doc_links.append(link.text)
# print(doc_links)

main_url = 'https://www.uchealth.org'
#test_link = ['https://www.uchealth.org/provider/mona-abaza-md-ms-otolaryngology/','https://www.uchealth.org/provider/rick-albert-md-internal-medicine/']

uc_health_provider = []

ct = 0
for doc_link in doc_links:

    ct += 1
    r = requests.get(doc_link)
    soup = BeautifulSoup(r.text, 'lxml')

    no = ct
    doc_name = soup.find('div', class_='hero-overlay').text.strip().replace("\t", "").replace("\n", "").split(",")[0]
    link =  doc_link
    f_name = soup.find('h3', class_='title').text.replace("\n", "")
    f_name_link = soup.find(class_='gtm_location_profile' , href=True)['href']
    f_phone = soup.find('div', class_='phone').text.strip().replace("\n", ",")
    try:
        f_fax = soup.find('div', class_='fax').text.strip().replace("\n", ",")
    except:
        f_fax = ''
    f_add_1 = soup.find('div', class_= 'address_line_1').text.strip()
    f_city_state_zip = soup.find('div', class_= 'city-state-zip').text.strip()
    try:
        f_add_2 = soup.find('div', class_= 'address_line_2').text.strip()
    except:
        f_add_2 = ''
    time.sleep(1)

    doc_details = {
        'No' : no,
        'Provider name' : doc_name,
        'Provider link' : link,
        'Facility name' : f_name,
        'Facility link' : main_url +''+ f_name_link,
        'Phone' : f_phone,
        'Fax' : f_fax,
        'Address1' : f_add_1,
        'Address2' : f_add_2,
        'City State Zip' : f_city_state_zip

    }
    uc_health_provider.append(doc_details)
    print(f'Saving {no} :', doc_details['Provider name'])
    df = pd.DataFrame(uc_health_provider)
#df.to_csv('uc_health_provider Details.csv')
df.to_csv(r'C:\Users\prash\Desktop\Project\uc_health_provider Details.csv', index=False)
#print(df.head(15))




