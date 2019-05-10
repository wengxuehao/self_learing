from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# 建立一個 ChatBot 物件
chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)
trainer = ChatterBotCorpusTrainer(chatbot)
# 第二步，训练语料

# trainer.train("chatterbot.corpus.english")

# 基於英文的自動學習套件

# # 載入(簡體)中文的基本語言庫
trainer.train("chatterbot.corpus.chinese")
#
# # 載入(簡體)中文的問候語言庫
trainer.train("chatterbot.corpus.chinese.greetings")
#
# # 載入(簡體)中文的對話語言庫
trainer.train("chatterbot.corpus.chinese.conversations")

# 與 ChatBot 對話，並且取得回應
while True:
    q = input()
    print(chatbot.get_response(q))
