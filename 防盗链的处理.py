# 1.拿到contID
# 2.拿到videoStatus返回的json. ->srcURL
# 3.srcURL里面的内容进行修整
# 4.拿到视频正确的src地址，下载视频
import requests

url = "https://www.pearvideo.com/video_1763997"
contID = url.split("_")[1]
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    # 防盗链：(referer)当前本次请求的上一级是谁
    "Referer": url
}

# 如果要对url地址进行修改的话，要在前面加f
videoStatusUrl = f"https://www.pearvideo.com/videoStatus.jsp?contId={contID}&mrd=0.9675444749265996"
resp = requests.get(videoStatusUrl, headers=header)
dic = resp.json()
srcUrl = dic["videoInfo"]["videos"]["srcUrl"]
systemTime = dic["systemTime"]
srcUrl = srcUrl.replace(systemTime, f"cont-{contID}")
# print(srcUrl)
# 下载视频
with open("a.mp4", mode="wb") as f:
    f.write(requests.get(srcUrl).content)
print("over!")
