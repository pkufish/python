import jieba
from wordcloud import WordCloud, ImageColorGenerator
from matplotlib import pyplot
from matplotlib import font_manager

# 首先定义一段文本在变量article中
article = "数据分析可以发现行业内经济变化趋势，挖掘用户需求特点，预测行业发展趋势，识别服务中出现的问题和潜在风险，确保业务稳定可控运营，支持企业战略决策提供科学依据。数据分析包括数据采集、数据清洗、数据可视化、模型开发和实现，涉及统计、算法、计算机科学等多种领域的知识。"

txt = open("words.txt", "r", encoding="utf-8").read()

# 使用jieba对article进行分词
seg_list = jieba.lcut(txt, cut_all=False)

print(seg_list)
# 分词后的结果做成字符串，方便后续处理
words = " ".join(seg_list)

# 定义字体文件路径

# 设置字体
#pyplot.figure(font_path=font_path2)

font = r'C:\Windows\Fonts\simfang.ttf'

pyplot.rcParams['font.sans-serif'] = 'SimHei'
#设置正常显示字符
pyplot.rcParams['axes.unicode_minus'] = True
#设置线条样式
pyplot.rcParams['lines.linestyle'] = '-.'
#设置线条宽度
pyplot.rcParams['lines.linewidth'] = 3

# 生成词云
# 生成一个wordcoud对象
wordcloud = WordCloud(collocations=False, font_path=font, width=1400, height=1400, margin=2).generate(words)

print(wordcloud)

# 显示图
pyplot.imshow(wordcloud)
pyplot.axis("off")
pyplot.show()
