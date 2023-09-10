from product_crawl import Tiki
from comment_crawl import TikiComment

if __name__ == "__main__":
    product_crawler = Tiki()
    product_crawler.crawn_tiki(50)
    product_detail = product_crawler.product_detail_list

    comment_crawler = TikiComment()
    dict = product_crawler.item_shop_dict

    i = 0
    for item_id, item_info in dict.items():
        seller_id = item_info['seller_id']
        spid = item_info['spid']
        cmt_count = item_info['cmtcount']
        comment_crawler.crawl_comment(item_id,seller_id,cmt_count,spid)
        print(f'Phase {i}')
        i += 1

    product_crawler.save_csv('Tiki/dataset/products_1815.csv')
    comment_crawler.save_csv('Tiki/dataset/reviews_1815.csv')