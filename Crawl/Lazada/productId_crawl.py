import requests
import time 
import random 
import pandas as pd


headers = {
    'Referer': 'https://www.lazada.vn/',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'X-Csrf-Token': 'e33ee858b618d',
    'X-Requested-With': 'XMLHttpRequest'
}

params = {
    'ajax': True,
    'isFirstRequest': True,
    'page': 1,
    'spm': 'a2o4n.home.cate_1.1.19053bdccFrL2j'
}
response = requests.get('https://www.lazada.vn/dien-thoai-di-dong/?ajax=true&isFirstRequest=true&page=1&spm=a2o4n.home.cate_1.1.19053bdccFrL2j', headers= headers, params=params)

def parser_item(item):
    product_details = {}
    
    product_details['itemId'] = item.get('itemId')
    product_details['name'] = item.get('name')
    product_details['brandId'] = item.get('brandId')
    product_details['brand_name'] = item.get('brandName')
    product_details['category'] = item.get('categories')
    product_details['inStock'] = item.get('inStock')
    product_details['sold'] = item.get('itemSoldCntShow')
    product_details['location'] = item.get('location')
    product_details['discount'] = item.get('discount')
    product_details['price'] = item.get('originalPrice')
    product_details['priceShow'] = item.get('price')
    product_details['rating'] = item.get('ratingScore')
    product_details['sku'] = item.get('sku')
    product_details['reviews'] = item.get('reviews')
    product_details['sellerId'] = item.get('sellerId')
    product_details['sellerName'] = item.get('sellerName')

    return product_details


product_details_list = []
for i in range (1,103):
    params["page"] = i
    response = requests.get('https://www.lazada.vn/dien-thoai-di-dong/?ajax=true&isFirstRequest=true&page=1&spm=a2o4n.home.cate_1.1.19053bdccFrL2j', headers= headers, params=params)
    if response.status_code == 200:
        print(f'Done{i}')
        mods = response.json()['mods']
        for record_key, record_value in mods.items():
            if record_key == 'listItems':
                list_items = record_value
                for item in list_items:
                    product_details = parser_item(item)
                    product_details_list.append(product_details)
    time.sleep(random.randrange(3,10))
            
df = pd.DataFrame(product_details_list)
df.to_csv(' product.csv', index = False)