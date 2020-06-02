# -*- coding: utf-8 -*-
"""
Spyder 编辑器

这是一个临时脚本文件。
"""
import requests,time

headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1"
}
url = "http://test.yamatosicecream.com:678/action/qq_kj/2019.php"

import random,string

u = 0
p = "a"

params={'u': {u} ,
        'p': {p} ,
        'bianhao': '1'
}
def genRandomString(slen=10):
    return ''.join(random.sample(string.ascii_letters + string.digits, slen))
def randomnumber(slen = 9):
    return "".join(map(lambda x:random.choice(string.digits), range(slen)))
def urlrequests():
    u = randomnumber()
    p = genRandomString()
    params['u'] = u
    params['p'] = p
    res = requests.get(url, params=params, headers=headers)
    print(res,u,p)
    time.sleep(2)
        
if __name__ == '__main__':
    while(1):
        urlrequests()
