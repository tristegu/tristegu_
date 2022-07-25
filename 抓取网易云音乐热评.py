# 1.找到未加密的参数                     #  window.asrsea()
# 2.想办法把参数进行加密(必须参考网易的逻辑)，params  =>encText，encSecKey  =>encSecKey
# 3.请求到网易，拿到评论信息

import requests
# 需要暗转Crypto pip install pycryptodome
from Crypto.Cipher import AES
from base64 import b64encode
import json

url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token=a060fbeabc4ff280da6fa06e6d23e9f0"

# 请求方式是POST
data = {
    "csrf_token": "a060fbeabc4ff280da6fa06e6d23e9f0",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_1325905146",
    "threadId": "R_SO_4_1325905146"
}

# 服务于d函数的参数
e = "010001"
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud"
i = "NF0bQ3UpH5bWy7Va"   # 手动固定的，人家函数中时随机的

def get_encSecKey():     # 由于i是固定搞的，那么encSecText也是固定的，c()函数的结果就是固定的
    return "7520c1e4a7a5b9e4e0d14d6b9e76922be0e757ad9e4eca17685f28e137e082faa85d04e171f08e26084c9f51b5de8f17a92f077208d3d4a72c9b6e0575dd7ed2c5d3473f70f343874c070caf230269ec2cc1911187e182bcd306d1e934a61a7e2b16d613c83c4ac9097e680e38a9c9647d325c92e3cd5295fd9197ffd9e07761"

# 把参数进行加密
def get_params(data):    # 默认这里接收到的是字符串
    first = enc_params(data, g)
    second = enc_params(first, i)
    return second   # 返回的就是params

# 将data的长度转化成16的倍数，为下方的加密算法服务
def to_16(data):
    pad = 16 - len(data) % 16
    data += chr(pad) * pad
    return data

# 加密过程
def enc_params(data, key):
    iv ='0102030405060708'
    data = to_16(data)
    aes = AES.new(key=key.encode("utf-8"), IV=iv.encode("utf-8"), mode=AES.MODE_CBC)  # 创造加密器
    bs = aes.encrypt(data.encode("utf-8"))   # 加密,加密的内容的长度必须是16的倍数
    return str(b64encode(bs), "utf-8")  # 转换成字符串返回

# 处理加密过程
"""
     function a(a = 16) {   # 随机的16位字符串
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)  # 循环16次
            e = Math.random() * b.length,   # 随机数
            e = Math.floor(e),    # 取整
            c += b.charAt(e);     # 取字符串中的xxx位置
        return c
    }
    function b(a, b) {  # a是要加密的内容,
        var c = CryptoJS.enc.Utf8.parse(b)    # b是秘钥
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)    # e是数据
          , f = CryptoJS.AES.encrypt(e, c, {   # c加密的秘钥
            iv: d,  # 偏移量
            mode: CryptoJS.mode.CBC  # 模式：CBC
        });
        return f.toString()
    }
    function c(a, b, c) {    # c里面不产生随机数
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {   d:数据  , e:010001   , f:很长   ,  g:0CoJUm6Qyw8W8jud
        var h = {}             # 空对象
          , i = a(16);         # i就是一个16位的随机值，把i设置成定值
        h.encText = b(d, g)    # g是秘钥
        h.encText = b(h.encText, i)    # 返回的就是params, i也是秘钥
        h.encSecKey = c(i, e, f)       # 得到的就是encSecKey,e和f是定死的，如果此时我把i固定,得到的key一定也是固定的
        return h
    }
    两次加密:
    数据+g => b => 第一次加密+i => b =params
"""

# 发送请求，得到评论结果
resp = requests.post(url, data={
    "params": get_params(json.dumps(data)),
    "encSecKey": get_encSecKey()

})
print(resp.text)