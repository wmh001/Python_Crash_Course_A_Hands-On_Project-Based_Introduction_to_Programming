# 15.3 随机漫步
# 每步的方向随机

# 15.3.1 创建RandomWalk()类

# 15.3.2 选择方向
# 添加fill_walk()方法

# 15.3.3 绘制随机漫步图
import matplotlib.pyplot as plt
from random_walk15_3 import Randomwalk

# 创建一个RandomWalk实例，并将其包含的点都绘制出来
rw = Randomwalk()
rw.fill_walk()
plt.scatter(rw.x_values, rw.y_values, s=15)
# plt.plot(rw.x_values, rw.y_values)
plt.show()

# 15.3.4 模拟多次随机漫步
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = Randomwalk()
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break

# 15.3.5 设置随机漫步图的样式
# 突出起点、终点和经过的路径

# 15.3.6 给点着色
# 使用颜色映射区分点的先后，删除每个点的轮廓
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = Randomwalk()
    rw.fill_walk()

    # 颜色映射
    point_numbers = list(range(rw.num_points))
    plt.scatter(
        rw.x_values,
        rw.y_values,
        c=point_numbers,
        cmap=plt.cm.Blues,
        edgecolors="none",
        s=15,
    )
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break

# 15.3.7 重新绘制起点和终点
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = Randomwalk()
    rw.fill_walk()

    # 颜色映射
    point_numbers = list(range(rw.num_points))
    plt.scatter(
        rw.x_values,
        rw.y_values,
        c=point_numbers,
        cmap=plt.cm.Blues,
        edgecolors="none",
        s=15,
    )
    plt.scatter(0, 0, c="green", edgecolors="none", s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break

# 15.3.8 隐藏刻度
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = Randomwalk()
    rw.fill_walk()

    # 隐藏刻度
    # 法一：
    # matplotlib.pyplot.axes()
    # 返回在当前图表实例上新创建的空白轴域实例
    ax = plt.axes()
    # matplotlib.axes._axes.Axes实例.get_xaxis()
    # 返回轴域实例的用于管理x轴及其轴标签、刻度、刻度标签的xaxis属性，为一个matplotlib.axis.XAxis（x轴）实例

    # 在模块matplotlib.axis中定义了类Axis及其子类XAxis和YAxis，分别用于管理坐标轴、x轴、y轴

    # matplotlib.axis.XAxis实例.set_visible(
    #     b=是否显示坐标轴刻度及其标签<布尔>)
    # 显示或隐藏x轴实例对应坐标轴的刻度及其标签
    ax.get_xaxis().set_visible(False)
    # matplotlib.axes._axes.Axes实例.get_yaxis()
    # 返回轴域实例的用于管理y轴及其轴标签、刻度、刻度标签的yaxis属性，为一个matplotlib.axis.YAxis（y轴）实例
    # matplotlib.axis.YAxis实例.set_visible(
    #     b=是否显示坐标轴刻度及其标签<布尔>)
    # 显示或隐藏y轴实例对应坐标轴的刻度及其标签
    ax.get_yaxis().set_visible(False)
    # 由于matplotlib.pyplot.axes()函数创建空白轴域会覆盖在原图上，与旧轴域叠加在一起，因此该函数需要在绘图前运行
    # 其余三个函数既可在创建轴域后到绘图前之间运行，又可以在绘图后到显示图像前运行，但需要作用于同一轴域实例

    # 法二：
    # matplotlib.pyplot.gca()
    # 返回当前轴域实例
    # plt.gca().get_xaxis().set_visible(False)
    # plt.gca().get_yaxis().set_visible(False)
    # 既可在创建轴域后到绘图前之间运行，又可以在绘图后到显示图像前运行

    # 法三：
    # matplotlib.pyplot.xticks(
    #     ticks=x轴刻度坐标列表<列表>: 列表元素为数字时，设定显示刻度的坐标; 列表为空时，不显示刻度 | 自动确定如何显示,
    #     labels=x轴刻度标签文本列表<列表>: 在x轴刻度位置列表不空时才能传入 | 文本化x轴刻度坐标列表元素组成的列表,
    #     **kwargs: 接收数个关键字实参)
    # 在当前轴域实例中设置x轴上显示几个刻度、在哪儿显示刻度、刻度标签
    # plt.xticks([])
    # matplotlib.pyplot.yticks(
    #     ticks=y轴刻度坐标列表<列表>: 列表元素为数字时，设定显示刻度的坐标; 列表为空时，不显示刻度 | 自动确定如何显示,
    #     labels=y轴刻度标签文本列表<列表>: 在y轴刻度位置列表不空时才能传入 | 文本化y轴刻度坐标列表元素组成的列表,
    #     **kwargs: 接收数个关键字实参)
    # 在当前轴域实例中设置y轴上显示几个刻度、在哪儿显示刻度、刻度标签
    # plt.yticks([])
    # 既可在创建轴域后到绘图前之间运行，又可以在绘图后到显示图像前运行

    # 颜色映射
    point_numbers = list(range(rw.num_points))
    plt.scatter(
        rw.x_values,
        rw.y_values,
        c=point_numbers,
        cmap=plt.cm.Blues,
        edgecolors="none",
        s=15,
    )
    plt.scatter(0, 0, c="green", edgecolors="none", s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break

# 15.3.9 增加点数
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = Randomwalk(50000)
    rw.fill_walk()

    # 隐藏刻度
    ax = plt.axes()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # 颜色映射
    point_numbers = list(range(rw.num_points))
    plt.scatter(
        rw.x_values,
        rw.y_values,
        c=point_numbers,
        cmap=plt.cm.Blues,
        edgecolors="none",
        s=1,
    )
    plt.scatter(0, 0, c="green", edgecolors="none", s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break

# 15.3.10 调整尺寸以适合屏幕
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = Randomwalk(50000)
    rw.fill_walk()

    # 设置绘图窗口的尺寸
    # matplotlib.pyplot.figure(
    #     num=图表的窗口标题<字符串/整型数/浮点数>: 接收字符串时将其作为标题; 接收数字时标题为Figure str(int(num))
    #         | None: 标题为Figure str(该窗口在同时显示的窗口中的打开序数),
    #     figsize=图表尺寸<二元组>: (宽（英寸）, 高（英寸）)，转换为以像素为单位时，假定屏幕分辨率为80像素/英寸 | None,
    #     dpi=分辨率（像素/英寸）<整型数/浮点数> | None,
    #     facecolor=背景颜色<字符串>: 可选参数为matplotlib模块通用字符符号 | None,
    #     edgecolor=边框颜色<字符串>: 可选参数为matplotlib模块通用字符符号 | None,
    #     frameon=是否显示边框<布尔> | True)
    # 返回依参数新创建的图表实例，并将其设置为当前图表实例
    plt.figure(dpi=128, figsize=(10, 6))

    # 隐藏刻度
    ax = plt.axes()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # 颜色映射
    point_numbers = list(range(rw.num_points))
    plt.scatter(
        rw.x_values,
        rw.y_values,
        c=point_numbers,
        cmap=plt.cm.Blues,
        edgecolors="none",
        s=1,
    )
    plt.scatter(0, 0, c="green", edgecolors="none", s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break
