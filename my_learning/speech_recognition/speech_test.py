# 从pcm–>mp3–>amr格式：
# /usr/local/ffmpeg3/bin/ffmpeg -f s16le -ar 16.0k -ac 1 -i test.txt.pcm test03.mp3
# /usr/local/ffmpeg3/bin/ffmpeg -ac 1 -ar 8000 -ab 5.15k -i test03.mp3 test05.amr
#
# 从amr–>mp3–>pcm格式
# /usr/local/ffmpeg3/bin/ffmpeg -i file.amr -ac 1 -ar 16.0k file.mp3
# /usr/local/ffmpeg3/bin/ffmpeg -i file.mp3 -f s16le -acodec pcm_s16le file.pcm
# ---------------------
# 作者：xianglingchuan
# 来源：CSDN
# 原文：https://blog.csdn.net/xianglingchuan/article/details/54092584
# 版权声明：本文为博主原创文章，转载请附上博文链接！
import time
from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '16037805'
API_KEY = 'blMPEwR70GvrPXZLTQCFc9jC'
SECRET_KEY = '0xGPAlkmsGLitMC9PoxzbRUFeQarfk5F'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


resp = client.asr(get_file_content('./pcm16k.pcm'), 'pcm', 16000, {
    'dev_pid': 1536,
})

print(resp)
