#  _*_ coding:utf-8 _*_
import requests
import re
import os

# 导入json文件（里面有所有英雄的名字及数字）

url = "http://pvp.qq.com/web201605/js/herolist.json"  # 英雄的名字json

head = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
html = requests.get(url, headers=head)
# html = requests.get(url)
html_json = html.json()
print(html_json)

# 提取英雄名字和数字

hero_name = list(map(lambda x: x["cname"], html_json))  # 名字
print(hero_name)
for index, i in enumerate(hero_name):
    # 根据不同名字创建不同的文件夹
    os.mkdir('/home/wy/Desktop/sleflearn/picture' + '/' + hero_name[index])
print(hero_name)
hero_number = list(map(lambda x: x["ename"], html_json))  # 数字
print(hero_number)
