# just validate all link scrap or not is pending - is validated and working fine
# some of linkIn link not capture so we need to apply 'if' condition and check this string 'Find me on Linkedin
# if found than take link else None

#https://www.houzz.com/professionals/interior-designer/florida-city-fl-us-highlight-best-of-houzz-winner-probr1-bo~t_11785~r_4155669~ps_1000?fi=15

from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
for i in range(20, 80 , 20):
    url = f'https://www.houzz.com/photos/query/design-build-firms/nqrwns/p/{i}?oq=design%20build%20firms&redirectoq=design%20build%20firms'

    #hozuzz_room_Details = []
    #print(i)
    #print(url)
    headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36", "X-Amzn-Trace-Id": "Root=1-62cc4e82-3e17734461ed9f8237c684d1"}

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    all_link = soup.findAll('a', class_='hz-photo-card__pro')
    c= 0
    room_links = []
    for link in all_link:
        c +=1
        room_links.append(link['href'])
        #print(c,link['href'])
    #print(room_links)

# test = 'https://www.houzz.com/professionals/design-build-firms/landis-architects-builders-pfvwus-pf~2046843566'

    hozuzz_room_Details = []
    for room_link in room_links:
        r = requests.get(room_link,headers= headers)
        soup = BeautifulSoup(r.content, 'lxml')
        #print(room_link)
        try:
            name = soup.find('h1', class_='sc-mwxddt-0 hOZgYi').text.strip()
        except:
            name = 'None'
        try:
            website = soup.find('a', class_='sc-62xgu6-0 dokyUu sc-mwxddt-0 kCqoeY hui-link trackMe')['href']
        except:
            website = 'None'
        try:
            add = soup.findAll('span', class_='sc-mwxddt-0 IconRow___StyledText-sc-1yd0o47-0 kalHqY heMrgw')[2].text
        except:
            add = 'None'
        try:
            cost =soup.findAll('span', class_='sc-mwxddt-0 IconRow___StyledText-sc-1yd0o47-0 kalHqY heMrgw')[3].text
            if 'Typical Job Cost' not in cost:
                cost = 'None'
            else:
                cost
                    #=re.sub("[^0-9]","|",cost)
        except:
            cost = 'None'
        try:
            linkedIn = soup.findAll('a', class_='sc-62xgu6-0 dSguXm sc-mwxddt-0 dOJEup hui-link hz-track-me')[2]['href']
        except:
            linkedIn = 'None'
        try:
            phone = soup.findAll('p', class_='sc-mwxddt-0 cZJFpr').text
        except:
            phone = 'None'
        room_details ={
            'Company name' : name,
            'Room Url'  : room_link,
            'Company URL'   : website,
            'Linkedin link' : linkedIn,
            'Typical Job Cost' : cost,
            'Address': add,
            'Phone' : phone

        }
        hozuzz_room_Details.append (room_details)
        print(room_details['Company name'])
    # df = pd.DataFrame(hozuzz_room_Details)
    # output_path = 'hozuzz_room_Details1.csv'
    # df.to_csv(output_path,mode='a',header=not
    #         os.path.exists(output_path))