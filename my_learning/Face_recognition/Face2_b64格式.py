# https://aip.baidubce.com/rest/2.0/face/v3/detect
import requests


# import matplotlib.pyplot as plt
# from matplotlib.image import imread
class Face():
    def __init__(self):
        # client_id 为官网获取的AK， client_secret 为官网获取的SK
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=EQ1xbon78DH5drso7Gulmepp&client_secret=h6gr3EL1hWgNLseA31xdEhxGl5t7QSe9'
        self.headers = {
            'Content-Type': 'application/json',
        }
        resp = requests.post(url=host, headers=self.headers)

        self.access_token = resp.json()['access_token']

    def face_detect(self):
        '''人脸检测'''
        url = 'https://aip.baidubce.com/rest/2.0/face/v3/detect'
        import base64
        with open("/home/wy/Desktop/wuyanzu.jpg", "rb") as f:
            # b64encode是编码，b64decode是解码
            base64_data = base64.b64encode(f.read())
            # base64.b64decode(base64data)

        params = {
            "image": base64_data,
            "image_type": "BASE64",
            # face_field 可以添加各个参数返回不同的响应
            "face_field": "faceshape,facetype,beauty,gender,emotion"
        }
        # params = {"image":"027d8308a2ec665acb1bdf63e513bcb9","image_type":"FACE_TOKEN","face_field":"faceshape,facetype"}
        # img = imread('/home/wy/Desktop/wechat/Face_recognition/ID_card.jpg')
        # plt.imshow(img)
        # plt.show()
        access_token =  self.access_token
        request_url = url + "?access_token=" + access_token
        headers = self.headers
        try:
            resp = requests.post(url=request_url, headers=self.headers, data=params)
            print(resp.json()['result'])
        except Exception as e:
            print(e)


face001 = Face()
face001.face_detect()