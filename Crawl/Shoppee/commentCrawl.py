import time 
import requests
import datetime
import pandas as pd 
import random

class Comment_Shopee:
    def __init__(self):

        self.comment_list = []


    def parser_comment(self, response):
        review_list = {}

        review_list['orderId'] = response.get('orderid')
        review_list['itemId'] = response.get('itemid')
        review_list['shopId'] = response.get('shopid')
        review_list['cmtId'] = response.get('cmtid')
        review_list['rating'] = response.get('rating_star')

        review_list['comment'] = response.get('comment')
        review_list['ship_oversea'] = response.get('sip_info')['is_oversea']
        review_list['region'] = response.get('sip_info')['origin_region']
        review_list['userId'] = response.get('userid')
        review_list['likes'] = response.get('like_count')

        return review_list

    def crawl_comment(self, itemId, shopId, count):
        pages = count // 59 if count % 59 == 0 else count//59+1
        for i in range(0,pages,4):
            offset = i*59
            url = 'https://shopee.vn/api/v2/item/get_ratings?exclude_filter=0&filter=0&filter_size=0&flag=1&fold_filter=0&itemid={}&limit={}&offset={}&relevant_reviews=false&request_source=1&shopid={}&tag_filter=&type=0&variation_filters='.format(itemId,59,offset,shopId)

            response = requests.get(url)
            if response.status_code == 200:
                
                d = response.json().get('data')
                if d is None:
                    continue
                for rating_key, rating_value in d.items():
                    if rating_key == 'ratings':
                        ratings = rating_value
                        if ratings == None:
                            continue
                        else:
                            for rating in ratings[:15]:
                            
                                self.comment_list.append(self.parser_comment(rating))



    def save_csv(self, filename):
        df = pd.DataFrame(self.comment_list)
        df.to_csv(filename,mode= 'w')




