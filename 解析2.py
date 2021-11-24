from lxml import etree
# xpath解析  1.实例化etree对象 2.通过调用etree对象中的方法结合xpath标签进行内容捕获

# 本地加载 etree.parse(filepath)
# 互联网 etree.HTML(page.text)
# xpath(xpath表达式)

if __name__=='__main__':
    # parser = etree.HTMLParser(encoding="utf-8")
    # tree = etree.parse("test.html", parser=parser)
    ps = etree.HTMLParser(encoding='utf-8')
    tree = etree.parse('demo.html',parser=ps)
    r= tree.xpath('/html//text')
    # = tree.xpath('/html/body/text')
    # //多个层级 /根节点开始 // 任意位置开始
    r1 = tree.xpath('//text[@class = "a"]')
    print(r1)
    r2 = tree.xpath('//text[2]')
    print(r2)
    r3 = tree.xpath('//div[@class = "d1"]/li[1]/text()')[0]
    print(r3)



