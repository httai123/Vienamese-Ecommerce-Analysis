import requests
import pandas as pd 

class TikiComment():
    def __init__(self):

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            'X-Guest-Token': 'v1jwOArlmQNJUb6iy2BETKfdZPhnYkR8'
        }

        self.params = {
            'limit': 20,
            'include' : 'comments,contribute_info,attribute_vote_summary',
            'sort' : 'score|desc,id|desc,stars|all',
            'page' : 1,
            'spid' : 0,
            'product_id' :0,
            'seller_id' : 0

        }

        self.comment_list = []

    def parser_comment(self,response):
        review_list = {}
        review_list['comment_id'] = response.get('id')
        review_list['product_id'] = response.get('product_id')
        review_list['content'] = response.get('content')
        review_list['customer_id'] = response.get('customer_id')
        delivery_rating = response.get('delivery_rating')
        if delivery_rating and len(delivery_rating) >= 4:
            review_list['delivery_time'] = delivery_rating[0]
            review_list['packaged_quality'] = delivery_rating[3]
        else:
            review_list['delivery_time'] = None
            review_list['packaged_quality'] = None
        seller = response.get('seller')
        # Check if seller is not None before accessing its 'id' field
        if seller:
            review_list['seller_id'] = seller.get('id')
        else:
            review_list['seller_id'] = None

        review_list['new_score'] = response.get('new_score')
        product_attributes = response.get('product_attributes')
        review_list['product_attributes'] = product_attributes[0] if product_attributes else None
        review_list['is_photo'] = response.get('is_photo')
        review_list['thank_count'] = response.get('thank_count')
        review_list['rating'] = response.get('rating')
        
        timeline = response.get('timeline')
        if timeline:
            review_list['date'] = timeline.get('review_created_date')
        else:
            review_list['date'] = None

        return review_list
    
    def crawl_comment(self,id,seller_id,count,spid):
        limit = self.params['limit']
        pages = count // limit if count % limit == 0 else count//limit + 1
        for i in range(1,pages+1):
            self.params['page'] = i
            self.params['spid'] = spid
            self.params['product_id'] = id
            self.params['seller_id'] = seller_id
            url = 'https://tiki.vn/api/v2/reviews'

            response = requests.get(url,headers=self.headers, params=self.params)
            print(response)
            if response.status_code == 200:
                d = response.json()['data']
                for review in d:
                    self.comment_list.append(self.parser_comment(review))

    
    def save_csv(self,filename):
        df = pd.DataFrame(self.comment_list)
        df.to_csv(filename,mode= 'w')
        