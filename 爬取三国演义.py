import requests
from bs4 import BeautifulSoup
import lxml

def getsg():
    headrs = {
        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 95.0.4638.69Safari / 537.36Edg / 95.0.1020.53'
    }
    url = 'https://www.shicimingju.com/book/hongloumeng.html'
    page_text = requests.get(url=url,headers=headrs)
    page_text.encoding = 'utf-8'
    page_text1 = page_text.text
    # print(page_text1)
    sp = BeautifulSoup(page_text1,'lxml')
    list_all = sp.select('.book-mulu>ul>li')
    fp = open('./get/红楼梦.txt','w',encoding='utf-8')
    for list in list_all:
        title = list.a.string
        list_url = 'https://www.shicimingju.com'+list.a['href']
        list_page_url = requests.get(url=list_url,headers=headrs)
        list_page_url.encoding = 'utf-8'
        list_page_url1 = list_page_url.text
        # print(list_page_url1)
        dsp = BeautifulSoup(list_page_url1,'lxml')
        div_tag = dsp.find('div',class_='chapter_content')
        content = div_tag.text
        fp.write(title+'\n'+content+'\n')
    
    # li_list = sp.find('div',class_="aside_title").string
    # print(li_list)
if __name__ == "__main__":
    getsg()
