from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 读取一个txt文件
text = open('words.txt', encoding="utf-8").read()

# 生成对象
wordcloud = WordCloud().generate(text)

# 显示词云图片
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
