from requests_html import HTMLSession

s = HTMLSession()

def get_product_links(page):
    url = f'https://themes.woocommerce.com/storefront/product-category/clothing/page/{page}'
    links = []
    r = s.get(url)
    products = r.html.find('ul.products li')
    for item in products:
        links.append(item.find('a', first=True).attrs['href'])
    return links

# print(page1)
# page1 = get_product_links(1)

def parse_product(url):
    #tesst_link = 'https://themes.woocommerce.com/storefront/product/lowepro-slingshot-edge-250-aw/'
    r = s.get(url)
    title = r.html.find('h1.product_title.entry-title', first=True).text.strip()
    price = r.html.find('p.price', first=True).text.strip().replace('£','').replace('\n',' ')
    cat = r.html.find('span.posted_in a', first=True).text.strip()
    try:
        sku = r.html.find('span.sku', first=True).text.strip()
    except AttributeError as err:
        sku = 'None'
        print(err)
    #link = url

    product = {
        'title': title,
        'price': price,
        'sku': sku,
        'category': cat,
        #'link' : url
    }
    return product
#print(parse_product('https://themes.woocommerce.com/storefront/product/lowepro-slingshot-edge-250-aw/'))

for x in range(1, 3):
    urls = get_product_links(x)
    for url in urls:
        print(parse_product(url))
