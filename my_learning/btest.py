import werobot
from werobot import WeRoBot
from werobot.replies import TextReply

robot = WeRoBot(token='wystech')
@robot.location
def echo(message):
    return'地图的地理位置信息：%s'% message.label
# @robot.image 修饰的 Handler 只处理图片消息
@robot.image
def img(message):
    return message.img
@robot.voice
def voice(message):
    try:
        return '语音的媒体格式：%s'% message.format
    except Exception as e:
        return e

@robot.video
def video(message):
    return '视频的媒体id:%s'% message.media_id
@robot.unknown
def unknown(message):
    return message.raw
@robot.link
def link(message):
    return '链接的主题:%s'%message.title
@robot.text
def hello(message, session):
    # count = session.get("count", 0) + 1
    # session["count"] = count
    # return "Hello!你刚才发送了:%s " % message.content
    reply = TextReply(message=message, content='Hello!')


# 让服务器监听在 0.0.0.0:80
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.config['DEBUG'] = True
robot.run()
