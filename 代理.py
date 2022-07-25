# 原理：通过第三方的一个机器去发送请求
# 先编写正常的爬虫代码
# 代理可以避免过多请求对方服务器后被封ip

import requests

# 218.60.8.83:3129
proxies = {
    # "http":"",
    "https" : "https://218.60.8.83:3129"
}
resp = requests.get("https://www.baidu.com", proxies=proxies)  # proxies就是代理
resp.encoding = 'utf-8'
print(resp.text)