import requests
import json
import urllib3
import re


urllib3.disable_warnings()

def save_wechattoken():
    url = 'https://t-wechat.qinghotel.com/wechat/user/decodeUserInfo/v2'
    data = {"unionId":"oo2kw1FoBs9IcJvyy3087DWmZzw4","openId":"odEYp4z2Xx5IkKOs0NUOZzvYZZgo"}
    headers = {"Host":"t-wechat.qinghotel.com", "content-type":"application/json"}
    result = requests.request('post', url, json=data, headers=headers, verify=False)
    token = json.loads(result.text)['data']['token']
    print(token)
    data = {
              "token": token,
              "Content-Type":"application/json"
            }
    # with open('./tempData/appletToken.json', 'w+') as f:  #linux
    with open('../tempData/appletToken.json', 'w+') as f:   #local 3.8
        f.write(json.dumps(data))
        print('wechattoken is update!!!')

save_wechattoken()
