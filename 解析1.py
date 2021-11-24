from bs4 import BeautifulSoup
import lxml
import requests

if __name__ == "__main__":
    # 将本地文件加载到soup中
    fp = open('./get/demo.html',encoding='utf-8')
    soup = BeautifulSoup(fp,'lxml')
    # 从互联网加载到soup中
    # fp = response.text
    # soup = BeautifulSoup(fp,'lxml')
    # print(soup)

    # 返回第一次出现的变迁 sou.tagName
    # print(soup.li)

    # find('tagName')等同于soup.tagName
    print(soup.find('li'))

    # 根据属性
    print(soup.find('li',class_ = 't2'))


    # findall
    print(soup.find_all('text',class_='a'))

    # 根据选择器 返回集合 层级选择器
    # soup.select('.a>url>li text>a')[0] 定位
    # 空格表示多个层级，大于表示的是一个层级
    print(soup.select('.b'))

    # 获取标签文本数据，属性值
    # sour.a.text/string/get_text text与gettext可以获取某一个标签中所有的文本内容 string只能获取该标签直系文本内容
    print(soup.find('div').text)
    print(soup.find('li').string)
    print(soup.find('li').get_text)
