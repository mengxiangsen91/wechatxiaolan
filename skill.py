# @Author:孟祥森
# @Time:2020/9/22 10:49
import json

import requests


def get_url(self):
    url = 'http://api.ruyi.ai/ruyi-api/v1/message'


def get_paramas_cyjl(data):
    global params
    app_key = 'b2c6735f-40a8-4174-9e52-d1b7531ab96a'
    user_id = '001'
    params = {'app_key': app_key,
              'user_id': user_id,
              'q': data}
    return params


def get_content_cyjl(data):
    a = get_paramas_cyjl(data)
    url = 'http://api.ruyi.ai/ruyi-api/v1/message'
    r = requests.post(url, data=json.dumps(a))
    b = r.json()["result"]["intents"]
    # print(b)
    for c in b:
        # print(c)
        for d in c["outputs"]:
            # print(d)
            result = d["property"]["text"]
            # print(result)
            return result


def caimiyu(self):
    pass


def yinyuedianbo(self):
    pass


def chat(self):
    pass


if __name__ == "__main__":
    get_content_cyjl("成语接龙")
