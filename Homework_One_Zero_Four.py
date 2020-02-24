#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
from lxml import html
import time
#找到 chromedriver
browser = webdriver.Chrome(executable_path='/Users/James/python課堂練習/Python爬蟲/chromedriver')

browser.get("http://104.com.tw/") #用selenium開啟104網頁
browser.implicitly_wait(10) #避免固定等待時間

#用SelectorGadget套件找到搜尋欄位css屬性 
keyword = browser.find_element_by_css_selector("#ikeyword") 

keyword.send_keys("數據") #########輸入搜尋 此欄位應設定變數
keyword.send_keys(Keys.ENTER) #送出輸入的關鍵字
browser.implicitly_wait(10)

### 以下為換頁方法
                                        #找到class page-select選擇頁面
#selectSite = Select(browser.find_element_by_css_selector(".page-select"))
#selectSite.select_by_value('2')#選取第二頁

soup.select('.page-select')[0].text.replace('第','').replace('頁','').split('/')[-1] #可取出總共頁數,注意是str屬性
pages = int(soup.select('.page-select')[0].text.replace('第','').replace('頁','').split('/')[-1])

#將頁數變為int屬性 , 指派給變數pages跑迴圈
############待解決問題: 1. 如何判斷總共有幾頁, done  2. 統整加入迴圈讓他從頭跑道尾 done


# In[ ]:


soup = bs(browser.page_source,'lxml') #browser.page_source指令可用selenium方式抓取當前網頁資訊
#browser.page_source #可去掉此行#號看資料長相


# In[ ]:


#抓取資料
soups = soup.select('article')

for page in range(pages+!)[1:]:
    selectSite = Select(browser.find_element_by_css_selector(".page-select"))
    selectSite.select_by_value(str(pages))
    for i in soups:
            if 'b-block--ad' in i.get('class'):
                continue #跳過有廣告標籤的公司
            if 'b-block--top-bord' in i.get('class'):
                url = "http:"+i.find("a").get("href") #職缺名稱網址
                browser = webdriver.Chrome(executable_path='/Users/James/python課堂練習/Python爬蟲/chromedriver')
                browser.get(url) #
                browser.implicitly_wait(10) #避免固定等待時間
                soup = bs(browser.page_source,'lxml')
                #soup=bs(browser.page_source,"html.parser") 
                rawdata = requests.get(url)
            if 'b-block--top-bord' not in i.get('class'):
                break
#           soup.select('.job-description__content')[0].text.strip().replace('\n','') #工作內容
#           soup.select('u')[0].text.strip() #職務類別
#           soup.select('.monthly-salary')[0].text.strip() #工作待遇   
            
#########待解決問題: 1. 加入抓取公司網址 抓取人數規模等資訊,其他資訊欄位還需補齊
#          2. 判斷重複資料
#          3. 資料儲存方式
#          4. 連接mysql語法攥寫
#          5. 資料如何導入資料庫


# In[ ]:




