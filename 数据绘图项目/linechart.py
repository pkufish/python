import matplotlib.pyplot as plt

# 准备数据
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

# 绘制线性图
plt.plot(x_values, y_values, linewidth=2)

# 设置图表标题和横纵坐标标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

# 显示图形
plt.show()
