# 16.1 CSV文件格式
# CSV文件格式：以,作为数据分隔符的用于存储数据的文本文件
# 处理阿拉斯加锡特卡2014年1月5日的天气数据文件sitka_weather_07-2014.csv

# 16.1.1 分析CSV文件头
# 文件头表明了文件具体存储了哪些信息
import csv
from datetime import datetime

import matplotlib.dates as mdates
import matplotlib.pyplot as plt

filename = r"data_visualization\sitka_weather_07-2014_16_1.csv"
with open(filename) as f:
    # csv.reader(
    #     csvfile=待阅读文件路径<字符串> | 无默认值,
    #     其他参数: 均有默认值)
    # 返回新创建的待阅读文件的阅读器实例（可迭代对象）
    # 其元素为存储一行数据的列表，列表的每个元素为字符串类型的用逗号分隔的一项数据
    # 其元素顺序为行序
    reader = csv.reader(f)
    # next(
    #     可迭代实例<迭代器>: 仅限位置实参 | 无默认值)
    # 返回迭代器实例的下一个元素，第一次对某个可迭代实例调用时返回第一个元素
    header_row = next(reader)
    print(header_row)

# 16.1.2 打印文件头及位置
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # enumerate(
    #     iterable=可迭代实例<迭代器> | 无默认值,
    #     其他参数: 均有默认值)
    # 返回一个新创建的可迭代对象，
    # 其元素为存储可迭代实例的索引和元素的元组，该元组第一个元素为索引，第二个元素为对应该索引的可迭代器实例的元素
    # 其元素顺序为可迭代实例的元素顺序
    print(next(enumerate(header_row)))
    for index, column_header in enumerate(header_row):
        print(index, column_header)

# 日期为第一列（索引0），最高温度为第二列（索引1）

# 16.1.3 提取并读取数据
# 读取最高温度
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = []
    # 遍历每行
    for row in reader:
        # 存储每行第2个数据
        highs.append(row[1])
    print(highs)

# 将字符串转换为数字
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = []
    # 遍历每行
    for row in reader:
        # 存储每行第2个数据
        high = int(row[1])
        highs.append(high)
    print(highs)

# 16.1.4 绘制气温图表
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(highs, c="red")
plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel("", fontsize=16)
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()

# 16.1.5 模块datetime
# 模块datetime用于处理时间
# datetime.datetime.strptime(
#     字符串时间<字符串>: 仅限位置实参 | 无默认值,
#     转换格式<字符串>: 仅限位置实参 | 无默认值)
# 返回将传进来的字符串时间按照指定格式转换成的datetime实例，
#     字符串时间中与转换格式字符串中指令位置相同的字符串将为指令对应的datetime实例属性赋值
# 转换格式可以不完整，没有指定的取默认值

# datatime指令：
# %y不带世纪的年份（公元年份后两位）默认00，%Y带世纪的年份默认1900，%m月序数默认01，%B月份名，%A星期名，
# %d日默认01，%H24小时制小时默认00，%I12小时制小时，%p上下午（am，pm），%M分默认00，%S秒默认00
first_date = datetime.strptime("2014-7-1", "%Y-%m-%d")
print(first_date)

# 16.1.6 在图表中添加日期
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs = [], []
    # 遍历每行
    for row in reader:
        # 存储每行第2个数据
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c="red")
plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel("", fontsize=16)
# matplotlib.pyplot.figure实例.autofmt_xdate(
#     bottom=x轴与图像底部的距离占比<浮点数>: 小于1的浮点数;
#         表示x轴与图像底部的距离与图像高度的比值，注意x轴不能高过y轴上限，故不能取1 | 0.2,
#     rotation=x轴刻度标签旋转角度<浮点数>: 浮点数为角度制，角度为与x轴夹角，逆时针为正 | 30,
#     ha=x轴标签水平对齐方式<字符串>: left靠左，center居中，right靠右 | "right",
#     which=作用于哪个刻度线标签<字符串>: major主要刻度线，minor次要刻度线，both主要刻度线和次要刻度线 | "mojor")
# 在图表实例内的轴域实例中调整x轴的位置和x轴刻度标签的角度
# 旋转x轴刻度标签，防止重叠
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()

# 16.1.7 涵盖更长的时间
# 锡特卡全年天气数据
filename = r"data_visualization\sitka_weather_2014_16_1.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, dates_str = [], [], []
    # 遍历每行
    for row in reader:
        # 存储每行第2个数据
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        dates_str.append(current_date.strftime("%Y-%m-%d"))
        high = int(row[1])
        highs.append(high)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c="red")
plt.title("Daily high temperatures - 2014", fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

# matplotlib.axis.XAxis实例.set_major_formatter(
#     formatter=x轴主要刻度标签的格式<matplotlib.ticker.Formatter类> | 无默认值
#     其他参数，均有默认值)
# 设置x轴实例对应坐标轴的主要刻度标签格式
# matplotlib.dates.DateFormatter(
#     fmt=格式<字符串>: datatime指令及其他字符拼接成的字符串，与datetime.datetime.strptime的格式字符串相同 | 无默认值,
#     tz=有关时区的信息<> | 忽略时区信息)
# 返回以一定格式新创建的matplotlib.dates.DateFormatter实例，其类型为matplotlib.ticker.Formatter类的子类
plt.gca().get_xaxis().set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))

plt.show()

# 16.1.8 再绘制一个数据系列
# 绘制最低气温
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    # 遍历每行
    for row in reader:
        # 存储每行第2个数据
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)
        low = int(row[3])
        lows.append(low)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")
plt.title("Daily high and low temperatures - 2014", fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)
plt.gca().get_xaxis().set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))

plt.show()

# 16.1.9 给图表区域着色
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    # 遍历每行
    for row in reader:
        # 存储每行第2个数据
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)
        low = int(row[3])
        lows.append(low)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c="red", alpha=0.5)
plt.plot(dates, lows, c="blue", alpha=0.5)
# matplotlib.pyplot.fill_between(
#     x=横坐标<列表> | 无默认值,
#     y1=曲线1纵坐标<列表/浮点数>: 接收浮点数表示曲线平行于x轴，纵坐标相同 | 无默认值,
#     y2=曲线2纵坐标<列表/浮点数>: 接收浮点数表示曲线平行于x轴，纵坐标相同 | 0,
#     其他参数: 均有默认值
#     **kwargs: 接收数个关键字实参，均有默认值:
#         facecolor=填充颜色<字符串>: 可选参数为matplotlib模块通用字符符号 | "b",
#         alpha=透明度<浮点数>: 用0~1浮点数表示 | 1,
#         其他参数)
# 在当前轴域实例中用颜色填充两条曲线之间的区域
plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)
plt.title("Daily high and low temperatures - 2014", fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)
plt.gca().get_xaxis().set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))

plt.show()

# 16.1.10 错误检查
# 数据缺失时妥善处理
# 加利福尼亚死亡谷气温
filename = r"data_visualization\death_valley_2014_16_1.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    # 遍历每行
    for row in reader:
        # 绕过缺失数据
        try:
            # 存储每行第2个数据
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, "missing data")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c="red", alpha=0.5)
plt.plot(dates, lows, c="blue", alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)
title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)
plt.gca().get_xaxis().set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))

plt.show()
