import werobot
import random
from werobot import WeRoBot
from werobot.replies import ArticlesReply, Article

robot = WeRoBot(token='wystech')
from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '16040536'
API_KEY = 'aCiGQ7gP7GceRREckMgy7S5K'
SECRET_KEY = 'TpUXmvH3K7rTXkjKjvTuDT6qbkOguEUp'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def music_data():
    music_list = [
        ['童话镇', '陈一发儿', 'https://e.coka.la/wlae62.mp3', 'https://e.coka.la/wlae62.mp3'],
        ['都选C', '缝纫机乐队', 'https://files.catbox.moe/duefwe.mp3', 'https://files.catbox.moe/duefwe.mp3'],
        ['精彩才刚刚开始', '易烊千玺', 'https://e.coka.la/PdqQMY.mp3', 'https://e.coka.la/PdqQMY.mp3']
    ]
    num = random.randint(0, 2)
    return music_list[num]


@robot.location
def echo(message):
    return '地图的地理位置信息：%s' % message.label


# @robot.image 修饰的 Handler 只处理图片消息
@robot.image
def img(message):
    url = message.img

    # """ 调用通用文字识别, 图片参数为远程url图片 """
    try:
        resp = client.basicGeneralUrl(url)
        list = []
        for i in resp['words_result']:
            word = i['words']
            list.append(word)
        with open('./test.txt', 'w') as f:
            for i in list:
                f.writelines(i + "\n")
        with open('./test.txt', 'r') as f:
            response = f.read()
        return '图像上传成功识别文字结果如下：%s' % response
    except Exception as e:
        return e


@robot.filter('听歌')
def sing(message):
    reply = ArticlesReply(message=message)
    article = Article(
        title="网易云音乐",
        description="即将跳转网易云",
        img='http://img1.imgtn.bdimg.com/it/u=3397394635,2323693060&fm=26&gp=0.jpg',
        url="https://music.163.com/"
    )
    reply.add_article(article)
    return reply


@robot.voice
def voice(message):
    return '语音的媒体格式：%s' % message.format


@robot.video
def video(message):
    return '视频的媒体id:%s' % message.media_id


@robot.unknown
def unknown(message):
    return message.raw


@robot.link
def link(message):
    return '链接的主题:%s' % message.title


@robot.text
def hello(message, session):
    # reply = TextReply(message=message, content='hello!')
    try:
        count = session.get("count", 0) + 1
        session["count"] = count
        return '你发送了请等待回复......:%s' % message.content
    except Exception as e:
        return e
        # return reply


@robot.scan
def scan_event(event):
    return event.ticket


# 让服务器监听在 0.0.0.0:80
@robot.filter('音乐')
def music(message):
    music1 = music_data()
    return music1


robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()
