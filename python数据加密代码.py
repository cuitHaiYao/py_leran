import binascii
import hashlib
import json

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
    """
    text: 内容 str
    key : 项目resource_id str
    iv : 项目秘钥 str
    return ： 加密字符串 str
    """
    key = md5value(key).encode('utf‐8')
    mode = AES.MODE_CBC
    iv = md5value(iv)
    iv = binascii.a2b_hex(iv)
    text = add_to_16(text)
    cryptos = AES.new(key, mode, iv)
    cipher_text = cryptos.encrypt(text)
    return binascii.b2a_hex(cipher_text)


if __name__ == '__main__':
    # key = "50c152c4c7f74a16b3743906f86c895e"
    # lv = "7MPKnD8WV1ZOr9k3"
    # data1 = encrypt('测试text', key, lv)
    # print(data1)
    reallsourceid = '5bfefaaf6cb64beea3a9e7863e8920d1'
    reallkey = 'W2qt9A836OGi5IcD'
    ycdata = {
        "projectID": "5bfefaaf-6cb6-4bee-a3a9-e7863e8920d1",  # 项目ID
        "IMEI": "TESTDUST-01",  # 设备监控号
        "time": "2021-11-23 15:10:00",  # 时间格式:yyyy-MM-dd HH:mm:ss
        "humidity": 20,  # 湿度
        "noise": 50,  # 噪音
        "PM10": 125.4,  # pm10
        "PM25": 80.5,  # pm25
        "temperature": 80,  # 温度
        "windDirection": 137.1,  # 风向
        "windSpeed": 50,  # 风速
        "sprayStatus": 0,  # 喷淋状态 0:关闭 1:开启
    }


    print(encrypt(json.dumps(ycdata), reallsourceid, reallkey))


    print(json.dumps({
        "data": "c52153fce0b6c24494fc555981aab2c79d02c559b897a43e95f99c22604996703a530b5d2431c331663958875f36bc3bb13296b94a00ddad459b3f75390258840a9979ba138569a0c18cdec8ffd5e1858ddee1325e2e6ba2ec246421a8e57b13c578f87b6486d423beaa1658c31efe10d68ac240214ce744a02a1e7632dd2f26328ef4b565bb1d581b89b498687dfb5bdf976d81c487fe4c0fa603cf813fa87636163cbcc8b6427e82d480140e2540c6ec3787b1e4f1f16dee6b91460548be62f907a97724a1b1a1f0e3447ab31955c21c0be1a4a75fe0a08ca8091d37841621af6314b79f99cf7bff4ea2f00e25ce1fb5ce8218cd9844c91a4f8dbc1912e429",
        "projectID": "5bfefaaf-6cb6-4bee-a3a9-e7863e8920d1"
    }
    ))
