import requests
import time 
import random 
import pandas as pd

class Shopee:
    def __init__(self):
        self.headers = {

            'User-Agent': 'python-requests/2.26.0',
            'Referer': 'https://shopee.vn/Thi%E1%BA%BFt-B%E1%BB%8B-%C4%90i%E1%BB%87n-T%E1%BB%AD-cat.11036132?facet=100582&page=0&sortBy=pop',
            'Sec-Ch-Ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Linux"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Sz-Token': 'rZD252Y8oif52q6gCs9abg==|IvJGGYftrwVHB9hqW6JNnh6biXmavRj5gvU430JHJf5HQPBr7+2A131RWcaHdIFQ1ANr+eyF3i2Q1A==|JciufarO4C2wjB5z|08|3',
            'X-Api-Source': 'pc',
            'X-Csrftoken': 'UzcXJ4awUrOQSvDFbdVk1CWRbEXu69Df',
            'X-Requested-With': 'XMLHttpRequest',
            'X-Sap-Access-F': '3.2.113.4.0|13|2.9.2-2_5.1.0_0_175|03d062fd35cb4e1c84518b5abce2f54c37288dd2c71f4b|10900|1100',
            'X-Sap-Access-S': 'rtLMFOpCqs5icRJymKS28CDdsACe1T3zpqsIO679HKk=',
            'X-Sap-Access-T': '1691031778',
            'X-Sap-Ri': 'e218cb64c64cb06e8bfd643162ada5a36a21a910d13c59a2',
            'X-Shopee-Language': 'vi',
            'X-Sz-Sdk-Version': '2.9.2-2&1.4.1',
            'Af-Ac-Enc-Dat': 'null',
            'Authority' : 'shopee.vn',
            "Accept": "application/json", 
            "Accept-Encoding": "gzip, deflate, br"
        }
        self.params = {
            'by': 'pop',
            'categoryids': 101100,
            'limit': 60,
            'match_id':  11036101,    
            'newest': 0,
            'order' : 'desc',
            'page_type' : 'search',
            'scenario' : 'PAGE_CATEGORY',
            'version' : 2
    
        }
        self.product_detail_list = []
        self.item_shop_dict = {}
    
    def parser_item(item):
        product_details = {}
        
        product_details['itemid'] = item.get('item_basic').get('itemid')
        product_details['shopid'] = item.get('item_basic').get('shopid')
        product_details['name'] = item.get('item_basic').get('name')
        product_details['subcatid'] = item.get('item_basic').get('catid')
        product_details['cb_option'] = item.get('item_basic').get('cb_option')
        product_details['cmt_count'] = item.get('item_basic').get('cmt_count')
        product_details['ctime'] = item.get('item_basic').get('ctime')
        product_details['flag'] = item.get('item_basic').get('flag')
        product_details['historical_sold'] = item.get('item_basic').get('historical_sold')
        product_details['is_adult'] = item.get('item_basic').get('is_adult')
        product_details['is_official_shop'] = item.get('item_basic').get('is_official_shop')
        product_details['liked_count'] = item.get('item_basic').get('likes')
        product_details['price'] = item.get('item_basic').get('price')
        product_details['discount'] = item.get('item_basic').get('discount')
        product_details['stock'] = item.get('item_basic').get('stock')
        product_details['show_free_shipping'] = item.get('item_basic').get('show_free_shipping')
        product_details['shop_location'] = item.get('item_basic').get('shop_location')
        product_details['shopee_verified'] = item.get('item_basic').get('shopee_verified')
        product_details['can_use_bundle_deal'] = item.get('item_basic').get('can_use_bundle_deal')
        product_details['can_use_cod'] = item.get('item_basic').get('can_use_cod')
        product_details['catid'] = 101100
        
        return product_details

    def crawn_shopee(self,pages):
        for i in range (0,pages):
            self.params['newest'] = i*60
            response = requests.get('https://shopee.vn/api/v4/search/search_items',params=self.params,headers=self.headers)
            if response.status_code == 200:
                print(response.json())
                print(f'Done {i}')
                list_items = response.json()['items']
                for item in list_items:
                    self.product_detail_list.append(self.parser_item(item))
                    self.item_shop_dict[item['itemid']] = {
                        'shopid' : item['shopid'],
                        'cmtcount' : item['cmt_count']
                    }
    
    def save_csv(self, filename):
        df = pd.DataFrame(self.product_detail_list)
        df.to_csv(filename)

