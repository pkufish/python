import string

# 给定一段英文：

text = 'In computer science, a linked list is a linear collection of data elements, called nodes, each pointing to the next node by means of a pointer. It is a data structure consisting of a collection of nodes which together represent a sequence. Under the simplest form, each node is composed of data and a reference to the next node in the sequence; more complex variants add additional links.inked lists are a very common and simple data structure used in computer science. The principal benefit of a linked list over a conventional array is that the list elements can be easily inserted or removed without reallocation or reorganization of the entire structure because the data items need not be stored contiguously in memory or on disk, while restructuring an array at run-time is a much more expensive operation.'

# 词频统计程序
def words_frequency(text):
    # 移除段落中标点符号
    punctuation_set = set(string.punctuation)
    modified_text = "".join([char for char in text if char not in punctuation_set])

    # 按空格分割单词
    words_list = modified_text.split()
    # 统计单词的词频
    words_frequency = {}

    for word in words_list:
         if word not in words_frequency:
                words_frequency[word] = 1
         else:
                words_frequency[word] += 1
    print(words_frequency)


    # 调用函数

if __name__ == '__main__':
    words_frequency(text)