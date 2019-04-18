import requests
import ssl

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=EQ1xbon78DH5drso7Gulmepp&client_secret=h6gr3EL1hWgNLseA31xdEhxGl5t7QSe9'
headers = {
'Content-Type':'application/json',
}
resp = requests.post(url=host,headers=headers)

access_token = resp.json()['access_token']


