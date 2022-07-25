# 拿到页面源代码 requests
# 使用re来提取想要的有效信息 re
# 将爬取到的数据存储到csv文件中 csv
import re
import requests
import csv

url = "https://movie.douban.com/top250"
dic = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

resp = requests.get(url, headers=dic)
page_content = resp.text

# 解析数据
# 采用预加载正则表达式 .*?为惰性匹配，换而言之就是尽可能少地匹配 其中(?P<name>.*?)就是爬取的目标对象
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>'
                 r'.*?<p class="">.*?<br>(?P<year>.*?)&nbsp'
                 r'.*?<span class="rating_num" property="v:average">(?P<rate>.*?)</span>'
                 r'.*?<span>(?P<people>.*?)</span>', re.S)

# 开始匹配
result = obj.finditer(page_content)
f = open("data.csv", mode="w")
csvwriter = csv.writer(f)
for it in result:
    # print(it.group("name"))
    # print(it.group("year").strip())
    # print(it.group("rate"))
    # print(it.group("people"))
    dic = it.groupdict()
    dic["year"] = dic["year"].strip()
    csvwriter.writerow(dic.values())
f.close()
print("over!")