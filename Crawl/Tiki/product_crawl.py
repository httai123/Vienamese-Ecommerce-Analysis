import pandas as pd
items1 = 
items2 = 
items3 = 
items4 = 
items5 = 
items6 = 
items7 = 
items8 = 
items9 = 
items10 = 
items11 = 
items12 = 
items13 = 
items14 = 
items15 = 
items = [items1,items2,items3,items4,items5,items6,items7,items8,items9,items10,items11,items12,items13,items14,items15]
def parser_item(item):
        product_details = {}
        
        product_details['itemid'] = item.get('item_basic').get('itemid')
        product_details['shopid'] = item.get('item_basic').get('shopid')
        product_details['name'] = item.get('item_basic').get('name')
        product_details['subcatid'] = item.get('item_basic').get('catid')
        product_details['cb_option'] = item.get('item_basic').get('cb_option')
        product_details['cmt_count'] = item.get('item_basic').get('cmt_count')
        product_details['rating'] = item.get('item_basic').get('item_rating').get('rating_star')
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
        product_details['catid'] = 1005
        return product_details

product_detail_list = []
for item in items:
    for i in item:
        product_detail_list.append(parser_item(i))

df = pd.DataFrame(product_detail_list)
df.to_csv('micro.csv')