import random
import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  # Import the Options class

# Initialize the Chrome WebDriver with the options
driver = webdriver.Chrome()

# Proceed with the rest of your code
driver.get('https://www.lazada.vn/products/gia-chi-4710k-khi-thanh-toan-dien-thoai-realme-c55-8gb256gb-hang-chinh-hang-tra-gop-0-mien-phi-van-chuyen-i2201252987-s10486338182.html?c=&channelLpJumpArgs=&clickTrackInfo=query%253A%253Bnid%253A2201252987%253Bsrc%253ALazadaMainSrp%253Brn%253A22df02c2dda594e227e7036201aa5910%253Bregion%253Avn%253Bsku%253A2201252987_VNAMZ%253Bprice%253A4299000%253Bclient%253Adesktop%253Bsupplier_id%253A200199195712%253Bpromotion_biz%253A%253Basc_category_id%253A4518%253Bitem_id%253A2201252987%253Bsku_id%253A10486338182%253Bshop_id%253A2918144&fastshipping=0&freeshipping=0&fs_ab=2&fuse_fs=0&lang=en&location=H%E1%BB%93%20Ch%C3%AD%20Minh&price=4.299E%206&priceCompare=&ratingscore=4.915492957746479&request_id=22df02c2dda594e227e7036201aa5910&review=71&sale=218&search=1&source=search&spm=a2o4n.searchlistcategory.list.i40.44a424eaojRXGe&stock=1')

elems_name = driver.find_elements(By.XPATH, '//*[@id="module_product_review"]/div/div/div[3]/div[1]/div[1]/div[2]/span[1]')
name_comment = [elem.text for elem in elems_name]

elems_content = driver.find_elements(By.XPATH, '//*[@id="module_product_review"]/div/div/div[3]/div[1]/div[1]/div[3]/div[1]')
content_comment = [elem.text for elem in elems_content]

elems_likeCount = driver.find_elements(By.XPATH, '//*[@id="module_product_review"]/div/div/div[3]/div[1]/div[1]/div[3]/div[4]/span[1]/span/span')
like_count = [elem.text for elem in elems_likeCount]

print
df = pd.DataFrame(list(zip(name_comment,content_comment,like_count)), columns=['name', 'comment', 'like'])

df.to_csv('Lazada/test.csv')

driver.quit()
