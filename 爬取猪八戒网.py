# 拿到页面源代码
# 提取和解析数据

import requests
from lxml import etree

url = "https://s.taobao.com/search?spm=a21bo.jianhua.201867-main.17.5af911d9JrT44M&q=%E7%94%B5%E5%99%A8"
resp = requests.get(url)
# print(resp.text)

# 解析
html = etree.HTML(resp.text)

# 拿到每一个服务商的div
divs = html.xpath('/html/body/div[@id="mainsrp-itemlist"]/div/div/div[1]/div')

# /html/body/div/div[2]/div[3]/div[1]/div[21]/div/div/div[1]/div/text()
print(divs)
# '//*[@id="mainsrp-itemlist"]/div/div/div[1]/div[1]'
# for div in divs:  # 每一个服务商信息
#    title = div.xpath('./a/div[2]/div/text()')
#    a = div.xpath('./a/div[2]/div[2]/div[1]/text()')
#    print(a)