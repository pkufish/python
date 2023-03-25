import matplotlib.pyplot as plt

# 准备数据
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

# 绘制折线图
plt.plot(x_values, y_values)

# 显示图形
plt.show()

----

import matplotlib.pyplot as plt

# 准备数据
x_values = ["A", "B", "C", "D", "E"]
y_values = [10, 24, 36, 48, 62]

# 绘制柱状图
plt.bar(x_values, y_values)

# 显示图形
plt.show()

---
import matplotlib.pyplot as plt

# 准备数据
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

# 绘制散点图
plt.scatter(x_values, y_values)

# 显示图形
plt.show()


matplotlib 支持多种类型的绘图，常见的绘图类型包括：

折线图（line plot）
散点图（scatter plot）
条形图（bar plot）
直方图（histogram）
饼图（pie chart）
箱线图（box plot）
热力图（heatmap）
3D 绘图（3D plot）
下面是这些绘图类型对应的函数名：

折线图：plt.plot()
散点图：plt.scatter()
条形图：plt.bar()、plt.barh()
直方图：plt.hist()
饼图：plt.pie()
箱线图：plt.boxplot()
热力图：plt.imshow()
3D 绘图：mpl_toolkits.mplot3d 中的函数
当然，这些只是 matplotlib 支持的部分绘图类型，实际上还有很多其他类型的绘图可以使用 matplotlib 实现。不同类型的绘图还会有不同的参数和用法，需要根据具体情况进行调整。




