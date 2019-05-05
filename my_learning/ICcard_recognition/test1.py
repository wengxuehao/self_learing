from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '16131914'
API_KEY = '0UgpVnwEPHjoyTATytsjO86N'
SECRET_KEY = '6VMhro31R5tRG7zGwW0yGh9ZWrudK371'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


image = get_file_content('/home/wy/Desktop/iccard.jpg')

resp = client.bankcard(image)

print('识别到的卡号是:%s'%resp['result']['bank_card_number'])
print('识别卡所属银行是:%s'%resp['result']['bank_name'])
