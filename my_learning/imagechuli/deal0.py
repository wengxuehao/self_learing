from aip import AipImageProcess

""" 你的 APPID AK SK """
APP_ID = '16167907'
API_KEY = '9RoMHV3w4b9DCSWrSjD97ke1'
SECRET_KEY = '22M2Qk0KqrDIkGI8havcUfVoAVUsR6CM'

client = AipImageProcess(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


image = get_file_content('./hashiqi.jpeg')

""" 调用图像无损放大 """
resp = client.imageQualityEnhance(image)
print(resp)
