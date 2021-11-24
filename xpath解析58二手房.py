import  requests
import lxml

def ershou58():
    url = 'https://cd.58.com/ershoufang/'
    hds = {
        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 95.0.4638.69Safari / 537.36Edg / 95.0.1020.53'
    }
    page_text = requests.get(url=url,headers=hds)
    page_text.encoding = 'utf-8'
    page_text = page_text.text
    # print(page_text)




if __name__  == '__main__':
    ershou58()