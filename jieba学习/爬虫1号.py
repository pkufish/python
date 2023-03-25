# 导入模块
from bs4 import BeautifulSoup
from selenium import webdriver


# 定义函数
# 请求URL

url= input("请输入网址，包括https://\n")

#url = "https://lsrm.hinews.cn/xinwen/show-17283.html?"

# 设置请求头和UA
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36")
browser = webdriver.Chrome(options=chrome_options)

browser.get(url)

# 获取网页源码
html = browser.page_source

# 关闭浏览器
browser.close()

# 新建soup对象获取html信息
soup = BeautifulSoup(html, 'html.parser')

# 获取搜索结果
results = soup.find_all('p')
# print(results)

#正文内容
text = ""

for result in results:
    text = text + str(result)

#print(text)

with open('words.txt', 'w', encoding="utf-8") as f:
    f.write(text)

import jieba

# 统计单个词频

# 函数定义
def getText():
    txt = open("words.txt", "r", encoding="utf-8").read()  # 读取文件
    txt = txt.lower()  # 把所有字母都变成小写，便于统计

    # 将文本中特殊字符替换为空
    for ch in '!"#$%&()*+,-./:;<=>?@[\\\n]^_‘{|}~':
        txt = txt.replace(ch, "")

    # 将文本中英文字符替换为空
    for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789':
        txt = txt.replace(ch, "")
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
