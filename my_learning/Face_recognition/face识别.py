# import urllib, urllib2, sys
import base64
import ssl
from pprint import pprint

import requests

get_token_url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=EQ1xbon78DH5drso7Gulmepp&client_secret=h6gr3EL1hWgNLseA31xdEhxGl5t7QSe9'
url = 'https://aip.baidubce.com/rest/2.0/image-classify/v2/dish'
resp = requests.post(get_token_url)
# print(resp.json()['access_token'])
access_token = resp.json()['access_token']
# print(access_token)
face_url = 'https://aip.baidubce.com/rest/2.0/face/v3/detect' + '?access_token=' + access_token
headers = {
    'Content-Type': 'application/x-www-form-urlencode'

}

with open('./wuyanzu.jpeg', 'rb') as f:
    content = f.read()
    img = base64.b64encode(content)
    params = {
        'image': img,
        'image_type': 'BASE64',
        "face_field": "age,beauty,expression,faceshape,gender,glasses,race,quality,emotion",
        'max_face_num': 5
    }
    response = requests.post(face_url, headers=headers, data=params)
    result = response.json()['result']
    # pprint(result)
    data = {
        'color': result['face_list'][0]['race']['type'],
        'age': result['face_list'][0]['age'],
        'glasses': result['face_list'][0]['glasses']['type'],
        'gender': result['face_list'][0]['gender']['type'],
        'face_shape':result['face_list'][0]['face_shape']['type']
    }
    print(data)
    # print('图片中可能人种是：%s'%color)
