import requests
from bs4 import BeautifulSoup

base_url = 'https://www.amazon.in'
url = 'https://www.amazon.in/s?k=ssd+m2+nvme+512&i=computers&rh=n%3A1375379031&page=2&qid=1657561514&ref=is_pn_1'

headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36", "X-Amzn-Trace-Id": "Root=1-62cc4e82-3e17734461ed9f8237c684d1"}


product_links = []

for i in range(0,2):
    r = requests.get(f'https://www.amazon.in/s?k=ssd+m2+nvme+512&i=computers&rh=n%3A1375379031&page={i+1}&qid=1657561514&ref=is_pn_1', headers = headers)
    soup = BeautifulSoup(r.content, 'lxml')
    links = soup.find_all('h2', class_='a-size-mini a-spacing-none a-color-base s-line-clamp-2')

    for item in links:
        for link in item.find_all('a', href=True):
            #print(base_url+''+link['href'])
            product_links.append(base_url+''+link['href'])
#print(len(product_links))

test_url = 'https://www.amazon.in/Crucial-Plus-500GB-PCIe-6600MB/dp/B098W1NDV2/ref=sr_1_1_sspa?keywords=ssd%2Bm2%2Bnvme%2B512&qid=1657556882&s=computers&sr=1-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFWNVNEMzREWU5OOEwmZW5jcnlwdGVkSWQ9QTAwNDQ4NTlIMFZFSk9QWDdRWE8mZW5jcnlwdGVkQWRJZD1BMDk2NTcwNTFPOVUxOVJCU0NaVDgmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl&th=1'

r = requests.get(test_url, headers=headers)

soup = BeautifulSoup(r.content, 'lxml')

#title = soup.find('span', id='productTitle').text.strip()
price = soup.find('span', class_ = 'a-price-whole').text.strip()
review = soup.find('span', id = 'acrCustomerReviewText').text.strip().split(' ')[0]
ranking = soup.find('span', class_='a-icon-alt').text.split(' ')[0]
size = soup.find('p', class_='a-text-left a-size-base').text
size_price = soup.find('p', class_='a-spacing-none a-text-left a-size-mini twisterSwatchPrice').text



print(size_price)