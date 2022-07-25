# 1.拿到主页面的源代码，然后提取到子页面的链接地址，href
# 2.通过href拿到子页面的内容，从子页面中找到图片的下载地址 img ->src

import requests
from bs4 import BeautifulSoup



url = "https://www.umei.cc/bizhitupian/weimeibizhi/"
resp = requests.get(url)
resp.encoding = "utf-8"  # 处理乱码
# print(resp.text)

# 把源代码交给bs4
main_page = BeautifulSoup(resp.text, "html.parser")
alist = main_page.find("div", class_="swiper-wrapper after").find_all("a")
# print(alist)
for a in alist:
    child_url = "https://www.umei.cc" + a.get("href")  # 直接通过get就可以拿到属性的值  #拼接url字符串
    # print(child_url)
    # 拿到子页面的源代码
    child_page_resp = requests.get(child_url)
    child_page_resp.encoding = "utf-8"
    child_page_text = child_page_resp.text
    # 从子页面中拿到图片的下载路径
    child_page = BeautifulSoup(child_page_text, "html.parser")
    p = child_page.find("div", class_="content-box")
    target_url = p.find("img")   # 使用find找到img标签
    src = target_url.get("src")   # 使用get直接提取src的属性值
    # print(target_url.get("src"))
    # 下载图片
    img = requests.get(src)
    # img.content   # 这里拿到的是字节
    img_name = src.split("/")[-1]   # 拿到url中最后一个/以后的内容，切片
    with open("image/" + img_name, mode="wb") as f:   # mode中wb属性适用于图片和声音
        f.write(img.content)  # 图片内容写入文件
    print("over!!", img_name)

print("all over!!!")