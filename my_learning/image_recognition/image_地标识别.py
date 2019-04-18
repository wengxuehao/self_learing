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

image = get_file_content('/home/wy/Desktop/tiananmen.jpg')

""" 调用地标识别 """
try:
    resp = client.landmark(image)
    print(resp['result']['landmark'])
except Exception as e:
    print(e)