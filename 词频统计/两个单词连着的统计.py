# 利用数组的方式来实现的词频统计，可能字典方式更简单

def getText():
    txt = open("words.txt", "r", encoding="utf-8").read()  # 词频统计的文件放在words.txt里
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(ch, " ")  # 将文本中特殊字符替换为空格
    return txt


# 词频展示的最小数值

# 将文本转换成一个一个的单词
hamletTxt = getText()
words = hamletTxt.split()


def countTerm():
    term = {}
    i = 0
    for word in words:
        term[i] = word
        print(term[i])
        i = i + 1
    # 统计单词数量
    count_term = i - 1
    print("-------------------\nAll terms are\n{}".format(term))
    print("-------------------\nThe number of words in this text is\n{}".format(count_term))

    # 将单词转换成两个连续单词的数组
    ad_terms = [[]]  # 不去重的数组
    dd_terms = [[]]  # 去重的数组

    for i in range(count_term):
        ad_terms.append([term[i], term[i + 1]])
    ad_terms.remove([])

    print('''-------------------
    All_double_terms are {}
    '''.format(ad_terms))

    count_all_double_terms = i - 1
    print("-------------------")
    print("count_all_double_terms is")
    print(count_all_double_terms + 2)

    j = 0

    for i in range(count_term):
        if [term[i], term[i + 1]] not in dd_terms:
            dd_terms.append([term[i], term[i + 1]])
            j = j + 1
    dd_terms.remove([])

    print("-------------------")
    print("distinct_double_terms are")
    print(dd_terms)

    count_distinct_double_terms = j

    print("-------------------")
    print("count_distinct_double_terms is")
    print(count_distinct_double_terms)

    # 统计词频
    count = []
    datatemp = [[[]]]

    for i in range(count_distinct_double_terms):
        count.append(0)
        for j in range(count_all_double_terms + 2):
            if dd_terms[i] == ad_terms[j]:
                count[i] = count[i] + 1

    for i in range(count_distinct_double_terms):
        if count[i] > gate:  # 只展示大于等于gate的
            a, b = dd_terms[i]
            c = count[i]
            datatemp.append([a, b, int(c)])

    datatemp.remove([[]])  # 去掉空格的那一项

    sorted_datas = sorted(datatemp, key=lambda x: x[2], reverse=True)  # 排序

    print("------------------------------------")
    print("关键词组合 ： 关键词频率")

    # 打印在屏幕上
    for data in sorted_datas:
        a, b, c = data
        print(a, b, ":", c)


if __name__ == "__main__":
    gate = 0
    # 将文本转换成一个一个的单词
    hamletTxt = getText()
    words = hamletTxt.split()
    countTerm()
