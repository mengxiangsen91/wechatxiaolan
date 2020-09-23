# @Author:孟祥森
# @Time:2020/9/18 16:57

import hashlib
import time
import requests
import random
import string
from urllib.parse import quote


def curlmd5(src):
    m = hashlib.md5(src.encode('UTF-8'))
    return m.hexdigest().upper()  # 将得到的MD5值所有字符转换成大写


def get_params(plus_item):  # 用于返回request需要的data内容
    global params
    t = time.time()  # 请求时间戳（秒级）,（保证签名5分钟有效）
    time_stamp = str(int(t))
    nonce_str = ''.join(random.sample(string.ascii_letters + string.digits, 10))  # 请求随机字符串，用于保证签名不可预测
    app_id = '2156854947'  # 修改成自己的id
    app_key = 'mw9EgBDh407Y4P3g'  # 修改成自己的key
    params = {'app_id': app_id,
              'question': plus_item,
              'time_stamp': time_stamp,
              'nonce_str': nonce_str,
              'session': '10000'
              }
    sign_before = ''
    for key in sorted(params):  # 要对key排序再拼接
        sign_before += '{}={}&'.format(key, quote(params[key], safe=''))  # 拼接过程需要使用quote函数形成URL编码
    sign_before += 'app_key={}'.format(app_key)  # 将app_key拼接到sign_before后
    sign = curlmd5(sign_before)
    params['sign'] = sign  # 对sign_before进行MD5运算
    return params  # 得到request需要的data内容


def get_content(plus_item):
    global payload, r
    url = "https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat"  # 聊天的API地址
    plus_item = plus_item.encode('utf-8')
    payload = get_params(plus_item)
    r = requests.post(url, data=payload)  # 带参请求api地址
    result = r.json()["data"]["answer"]
    print(result)
    return result  # 获得返回内容
