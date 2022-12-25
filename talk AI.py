import requests
import json
import os


while True:
    msg = input('Eric：')
    sess = requests.get(
        ('http://route.showapi.com/60-27?&showapi_appid=102421&userid=userid&showapi_sign=77760de9bbc640f68433718f807b3e42&info=' + msg))
    js = sess.text
    js = json.loads(js)
    print('Eric A.I.：', js['showapi_res_body']['text'])
    talk = js['showapi_res_body']['text']
    os.system("say {}".format(talk))