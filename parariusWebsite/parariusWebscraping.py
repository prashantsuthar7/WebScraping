from bs4 import BeautifulSoup
import requests
import pandas as pd

for i in range(1,3):
    url = f"https://www.pararius.com/apartments/amsterdam/page-{i+1}"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    lists = soup.find_all('section', class_="listing-search-item")

    for list in lists:
        title = list.find('a', class_="listing-search-item__link listing-search-item__link--title").text.strip()
        location = list.find('div', class_="listing-search-item__location").text.strip()
        price = list.find('div', class_="listing-search-item__price").text.strip()
        size = list.find('li', class_="illustrated-features__item illustrated-features__item--surface-area").text.strip()

        dist = {
            'Title' : title,
            'Location' : location,
            'Price' : price,
            'Size' : size
        }
        print(dist)
    print(f'Page {i}')
    # df = pd.DataFrame.from_dict(dist)
    # df.to_csv(r'pararious.csv', index= False, header=True)
