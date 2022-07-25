# 登录 -> 得到cookie
# 带着cookie去请求书架url -> 书架上的内容

# 必须把上面两个操作连起来
# 我们可以使用session进行请求 -> session你可以认为是一连串的请求. 在这个过程中cookie不会丢失

import requests
data = {
    "loginName": "13818925348",
    "password": "Ghr20020118"
}
# 会话
session = requests.session()

# 1.登录
url = "https://passport.17k.com/ck/user/login"
resp = session.post(url, data=data)
# print(resp.text)
# print(resp.cookies)   # 看cookie

# 2.拿书架上的数据
# 刚才的那个session中是有cookie的
shujia_url = "https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919"
result = session.get(shujia_url)
print(result.json())