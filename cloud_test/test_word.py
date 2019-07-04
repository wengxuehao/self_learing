#  _*_ coding:utf-8 _*_
# 词云
import wordcloud
import matplotlib.pyplot as plt

# 添加中文支持
w = wordcloud.WordCloud(background_color='white', height=660, width=800, margin=2,
                        font_path=r'./simhei.ttf')
with open('a.txt', 'r') as f:
    content = f.read()
    wordcloud = w.generate(content)

plt.imshow(wordcloud)
plt.axis('off')
plt.show()
wordcloud.to_file('test.png')
print('生成词云成功')
# 用wordcloud等软件生成词云，它会根据信息的频率、权重按比列显示关键字的字体大小。
