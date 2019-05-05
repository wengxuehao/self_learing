from aip import AipImageClassify

""" 你的 APPID AK SK """
APP_ID = '16042058'
API_KEY = 'AyuLyqu4FNB4klZvGAHSjVaQ'
SECRET_KEY = 'MI53Tuf71Xt4KoQiqT7G3lUH96DC3mZ8'

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)


""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('yueji.jpeg')
#
# """ 调用通用物体识别 """
# resp = client.animalDetect(image)
# print(resp)

""" 如果有可选参数 """
options = {}
options["top_num"] = 3
options["baike_num"] = 5
""" 带参数调用通用植物识别 """
resp = client.plantDetect(image, options)
print(resp)
print(resp['result'][0]['name'])
print(resp['result'][0]['baike_info']['description'])

