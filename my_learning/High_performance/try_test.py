# def fuc():
#     try:
#         import requests
#         resp = requests.get('http://www.baidu.com')
#         print(resp.content)
#     except Exception as e:
#         print(e)
#     try:
#         print('111')
#     except Exception as e:
#         print('222')
# fuc()


dict = {
    "name": "zs",
    "age": "18"
}
dict2 = {
    "addr": "sh"
}
dict.update(dict2)

image = {'count': 5, 'action': 'xxxx', 'event_id': 'sjshahah'}
dict.update(image)
print(dict)
dict.pop('addr')
print(dict)
