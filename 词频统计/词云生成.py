# 统计单个词频
# 函数定义
def getText():
    txt = open("words.txt", "r", encoding="utf-8").read()  # 读取文件
    txt = txt.lower()  # 把所有字母都变成小写，便于统计

    # 将文本中特殊字符替换为空格
    for ch in '!"#$%&()*+,-./:;<=>?@[\\\n]^_‘{|}~':
        txt = txt.replace(ch, " ")
    return txt  # 返回值


def getStopwords():
    txt = open("stopwords.txt", "r", encoding="utf-8").read()  # 读取文件
    txt = txt.lower()  # 把所有字母都变成小写，便于统计

    # 将文本中特殊字符替换为空格
    for ch in '!"#$%&()*+,-./:;<=>?@[\\\n]^_‘{|}~':
        txt = txt.replace(ch, " ")
    return txt  # 返回值


longtext = ""

stopwords = getStopwords().split()  # 将stopwords读取到停止词数组中
words = getText().split()  # 将阅读文本用空格分隔
counts = {}  # 大括号是字典元素

# 统计单词出现的次数

for word in words:  # 字典中的每个元素
    if word in stopwords:
        x = 1  # print('{} is stopword'.format(word))
    else:  # print('{} is not stopword'.format(word))
        longtext = longtext + " " + word  # 把词汇添加到文件中


import matplotlib.pyplot as plt
# 导入词云制作库wordcloud
from wordcloud import WordCloud

# 生成对象
wordcloud = WordCloud(background_color="white", width=1000, max_words=500).generate(longtext)
print(wordcloud)

# 显示词云图片
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()