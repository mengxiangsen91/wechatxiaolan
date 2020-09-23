import json

from PyWeChatSpy import WeChatSpy
import random
import re
# from wxpy import *
from api import *
from skill import get_content_cyjl


def my_parser(data):
    if data["type"] == 5:  # 判断是微信消息数据
        for msg in data["data"]:  # 遍历微信消息
            # if msg["msg_type"] == 10000:  # 判断是微信拍一拍系统提示
            #     # 因为微信系统消息很多 因此需要用正则匹配消息内容进一步过滤拍一拍提示
            #     # {'self': 0, 'msg_type': 10000, 'wxid1': '179xxxxxx72@chatroom', 'content': '"Mandy的小脑袋" 拍了拍你'}
            #     m = re.search('".*" 拍了拍', msg["content"])
            #     if m:  # 搜索到了匹配的字符串 判断为拍一拍
            #         image_path = f"F:\\PyWeChatSpy-1.0.7.x\\images\\{random.randint(1, 7)}.jpg"  # 随机选一张回复用的图片
            #         spy.send_file(msg["wxid1"], image_path)  # 发送图片
            # if msg["wxid2"] in data["data"]:
            #     continue
            # if 1 == 1:
            if '@小岚' in msg["content"]:
                if msg["msg_type"] == 1 and msg["self"] == 0:
                    b = msg["content"]
                    a = b.replace("@小岚\u2005", "")
                    answer = get_content(a)
                    time.sleep(1)
                    if answer == '':  # 防止返回内容为空
                        for i in range(2):
                            time.sleep(2)
                            answer = get_content(a)
                            if answer != '' and answer != "emmmm，我不是很懂你的意思":
                                break
                            else:
                                answer = "emmmm，我不是很懂你的意思"
                    spy.send_text(msg["wxid1"], answer)
            elif "#" in msg["content"]:
                if msg["msg_type"] == 1 and msg["self"] == 0:
                    b = msg["content"]
                    a = b.replace("#", "")
                    answer = get_content_cyjl(a)
                    time.sleep(1)
                    spy.send_text(msg["wxid1"], answer)
            else:
                break


spy = WeChatSpy(parser=my_parser)  # 实例化WeChatSpy类


if __name__ == '__main__':
    spy.run()  # 运行代码
