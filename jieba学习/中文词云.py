import jieba

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
words = jieba.lcut(getText(), cut_all=False)  # 将阅读文本用空格分隔
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
font = r'C:\Windows\Fonts\simfang.ttf'

# 生成对象
wordcloud = WordCloud(collocations=False, font_path=font, width=1600, height=1000, margin=2).generate(longtext)

# 显示词云图片
plt.figure(dpi=300,figsize=(16,9))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()