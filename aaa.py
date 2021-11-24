import binascii
import hashlib
import json

import requests
from Crypto.Cipher import AES
import base64


def add_to_16(text):  # 补足为16倍数
    if len(text.encode('utf‐8')) % 16:
        add = 16 - (len(text.encode('utf‐8')) % 16)
    else:
        add = 0
    text = text + ('\0' * add)
    return text.encode('utf‐8')


def md5value(key):
    input_name = hashlib.md5()  # md5摘要算法
    input_name.update(key.encode("utf‐8"))
    return input_name.hexdigest().lower()  # hexdigest()返回摘要作为十六进制数据字符串值


# 加密函数
def encrypt(text, key, iv):
    # """
    # text: 内容 str
    # key : 项目resource_id str
    # iv : 项目秘钥 str
    # return ： 加密字符串 str
    # """
    key = md5value(key).encode('utf‐8')
    mode = AES.MODE_CBC
    iv = md5value(iv)
    iv = binascii.a2b_hex(iv)
    text = add_to_16(text)
    cryptos = AES.new(key, mode, iv)
    cipher_text = cryptos.encrypt(text)
    return binascii.b2a_hex(cipher_text)

def yzc():
    # 5bfefaaf-6cb6-4bee-a3a9-e7863e8920d1	W2qt9A836OGi5IcD
    p_id = "5bfefaaf-6cb6-4bee-a3a9-e7863e8920d1"
    key = "W2qt9A836OGi5IcD"
    yzcdata = {
        "projectID": "5bfefaaf-6cb6-4bee-a3a9-e7863e8920d1",  # 项目id
        "deviceCode": "TESTCAR-01",  # 设备编号
        "time": 1628770919,  # UTC+8 时间戳,拿到的心跳时间是两分钟之前或者在当前时间一分钟之后，则认为时间有误
        "online": 1  # 0.离线，1.在线
    }
    print(encrypt(json.dumps(yzcdata),p_id,key))

    url = 'http://47.108.75.78/open-api/car/heart'
    hds = {
        'Content-Type': 'application/json'
    }
    data = {
        "data": "22ec644c5588d6c56e0a3d6cc60f97201cc6d8d6c227a816671e00fdfdc5ca784eb26fd63df1af56f5f78a63e61ac387adc6a9bd3c7f8dbadaf1136e563b161d7e3527dbca2885426e6293efda2d20b751fbdedea09d317e760ac5a59f6029cbe787151211a777e64332057f787b0f5b1ccbbae08a01d70171e7140c6f0600cc",
        "projectID": "5bfefaaf-6cb6-4bee-a3a9-e7863e8920d1"
}
    resp = requests.post(url=url,data=data,headers=hds)
    print(resp.text)





if __name__ == '__main__':
    yzc()


