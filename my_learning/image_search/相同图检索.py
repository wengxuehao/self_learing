from aip import AipImageSearch

""" 你的 APPID AK SK """
APP_ID = '16210913'
API_KEY = '5wwaTUz3RHiqojeCLvRcEt9n'
SECRET_KEY = 'yyKlQqX5gyavNKfxR1HwrDSRxSqNc7uY'

client = AipImageSearch(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


image = get_file_content('/home/wy/pic/jumao.jpg')

""" 调用相同图检索—入库, 图片参数为本地图片 """
# resp = client.sameHqAdd(image)
# print(resp)

""" 如果有可选参数 """
options = {}
options["brief"] = "{\"name\":\"周杰伦\", \"id\":\"666\"}"
options["tags"] = "100,11"

# """ 带参数调用相同图检索—入库, 图片参数为本地图片 """
resp = client.sameHqAdd(image, options)
print(resp)
#
resp1 = client.sameHqSearch(image)
""" 调用相同图检索—检索, 图片参数为本地图片 """
print(resp1)
# url = "http//www.x.com/sample.jpg"
#
# """ 调用相同图检索—入库, 图片参数为远程url图片 """
# client.sameHqAddUrl(url)
#
# """ 如果有可选参数 """
# options = {}
# options["brief"] = "{\"name\":\"周杰伦\", \"id\":\"666\"}"
# options["tags"] = "100,11"
#
# """ 带参数调用相同图检索—入库, 图片参数为远程url图片 """
# client.sameHqAddUrl(url, options)
