# 1.定位到2020必看片
# 2.从2020必看片中提取到子页面的链接地址
# 3.请求子页面的链接地址  拿到我们想要的下载地址

import requests
import re
import csv

url = "https://dytt89.com/"
resp = requests.get(url)
resp.encoding = "gb2312"  #指定字符集
# print(resp.text)

obj1 = re.compile(r"2022必看热片.*?<ul>(?P<ul>.*?)</ul>", re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'", re.S)
obj3 = re.compile(r'◎译　　名(?P<movie_name>.*?)<br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf">'
                  r'<a href="(?P<download>.*?)">', re.S)

result1 = obj1.finditer(resp.text)
target_href_list = []
f = open("movie_data.csv", mode="w")
csvwriter = csv.writer(f)

for it in result1:
    ul = it.group("ul")
    # 提取子页面的链接
    result2 = obj2.finditer(ul)
    for item in result2:
        # 拼接子页面的链接： 域名+子页面地址
        target_href = url + item.group("href").strip('/')
        target_href_list.append(target_href) # 将子页面链接保存起来

# 提取子页面内容
for href in target_href_list:
    resp2 = requests.get(href)
    resp2.encoding = "gbk"
    result3 = obj3.finditer(resp2.text)
    for itt in result3:
        dic = itt.groupdict()
        csvwriter.writerow(dic.values())
f.close()
print("over!")
# 总结：先锁定url：https://dytt89.com/，其次，在该网站路径下，通过网站源代码找到爬取目标对象，因为是链接地址的关系
# 我们需要额外的使用预加载compile语句查询该网站代码进行爬取，然后提取子页面的链接，将内容存储在空列表中
# 最后，对列表中的内容进行循环预处理加载，将内容格式改为字典，并存放在文件中