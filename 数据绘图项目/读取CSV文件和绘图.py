import csv
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

date_list, uv_list = [], []
# 从csv文件读取数据
csv_file = csv.reader(open('data.csv', encoding='utf-8'))

str = ''

for line in csv_file:
    ll = line[0].split(';')
    date_list.append((datetime.isoformat(datetime.strptime(ll[0], '%Y%m%d'))))
    uv_list.append(ll[1])
    print('{}  {}'.format(datetime.isoformat(datetime.strptime(ll[0], '%Y%m%d')), ll[1]))

# 将字符串转换为浮点数
uv_list = np.array(uv_list, dtype=float)

# 绘制折线图
plt.figure(figsize=(8, 8))
plt.plot(date_list, uv_list, color='red', label='UV', linestyle='-', marker='^', markersize=4)
plt.title('Daily UV')
plt.xlabel('Date')
plt.ylabel('UV Value')
plt.legend()
plt.show()

# https://matplotlib.org/api/pyplot_summary.html
