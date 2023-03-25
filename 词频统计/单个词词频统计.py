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
        counts[word] = counts.get(word, 0) + 1  # 字段中每个字段增加词频

print("字典元素：{}".format(counts))  # 打印字典元素
items = list(counts.items())  # 字典转化为列表
print("列表元素：{}".format(items))  # 打印字典元素

# 排序，按单词出现的次数从大到小排好序
items.sort(key=lambda itemX: itemX[1], reverse=True)  # itemX是一个随即命名的函数，lambda是隐藏自定义函数的命令 itemX[1]是第列表元组第二个函数

# 打印出现次数前10 的单词
i = 0
print("{0:<10}{1:>5}".format("短语", "词频"))  # 采用固定宽度展示
while i < len(items):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
    i = i + 1


