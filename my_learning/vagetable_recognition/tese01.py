import base64
from pprint import pprint

import requests
from IPython.core.display import display

get_token_url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=AyuLyqu4FNB4klZvGAHSjVaQ&client_secret=MI53Tuf71Xt4KoQiqT7G3lUH96DC3mZ8&'
url = 'https://aip.baidubce.com/rest/2.0/image-classify/v2/dish'
resp = requests.post(get_token_url)
# print(resp.json()['access_token'])
access_token = resp.json()['access_token']
request_url = url + "?access_token=" + access_token
headers = {
    'Content-Type': 'application/x-www-form-urlencode'

}
f = open('/home/wy/Desktop/shucai.jpg', 'rb')

content = f.read()
img = base64.b64encode(content)
f.close()
# print(img)
params = {
    'image': img,
    'top_num': 5,
    'baike_num': 0
}
response = requests.post(request_url, headers=headers, data=params)
pprint(response.json())
