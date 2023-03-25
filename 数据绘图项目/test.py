import csv
import numpy as np
import matplotlib.pyplot as plt

date_list, uv_list = [], []
# 从csv文件读取数据
csv_file = csv.reader(open('data.csv', encoding='utf-8'))
print(csv_file)

for line in csv_file:
    print(line)