# coding=utf-8

from chatterbot import ChatBot

# 第一步，创建chatterbot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot(

    'Ron Obvious',

    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'

)
trainer = ChatterBotCorpusTrainer(chatbot)
# 第二步，训练语料

# trainer.train("chatterbot.corpus.english")
trainer.train("chatterbot.corpus.chinese.conversations")

# 第三步，输入对话得到答案
while True:
    q = input()

    print(chatbot.get_response(q))

