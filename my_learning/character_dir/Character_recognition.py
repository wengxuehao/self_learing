from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '16040536'
API_KEY = 'aCiGQ7gP7GceRREckMgy7S5K'
SECRET_KEY = 'TpUXmvH3K7rTXkjKjvTuDT6qbkOguEUp'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
  

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('ID_card.jpg')

""" 调用通用文字识别, 图片参数为本地图片 """
client.basicGeneral(image)

""" 如果有可选参数 """
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"

""" 带参数调用通用文字识别, 图片参数为本地图片 """
resp = client.basicGeneral(image, options)
# print(resp)
list = []
for i in resp['words_result']:
    word = i['words']
    list.append(word)
with open('./test.txt','w') as f:
    for i in list:
        f.writelines(i + "\n")
with open('./test.txt','r') as f:
    print('识别到的内容是：%s'%f.read())
        # continue
        # print(i)
    # print(i)
# print(resp['words_result'])

# url = "http://119.3.42.90:8080/static/images/logo.jpg"
# #
# # """ 调用通用文字识别, 图片参数为远程url图片 """
# try:
#     resp = client.basicGeneralUrl(url)
#     print(resp)
# except Exception as e:
#     print(e)
#
# #
# # """ 如果有可选参数 """
# options = {}
# options["recognize_granularity"] = "big"
# options["language_type"] = "CHN_ENG"
# options["detect_direction"] = "true"
# options["detect_language"] = "true"
# options["vertexes_location"] = "true"
# options["probability"] = "true"
#
# """ 带参数调用通用文字识别, 图片参数为远程url图片 """
# resp = client.webImageUrl(url, options)
# print(resp)

