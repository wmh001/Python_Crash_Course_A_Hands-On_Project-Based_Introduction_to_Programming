# 16.2 制作交易收盘价走势图：JSON格式

# 16.2.1 下载收盘价数据
# 访问https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json
# 该文件的内容为一个长列表，其元素为字典，每个字典有5个相同的键：日期、月序数、周序数、星期、收盘价
# from __future__ import (absolute_import, division, print_function,
#                         unicode_literals)
# try:
#     # Python 2.x版本
#     from urllib2 import urlopen
# except ImportError:
#     # Python 3.x版本
#     from urllib.request import urlopen
# import json
# import requests

# json_url = "https://raw.githubusercontent.com/muxuezi/btc/master/
#     btc_close_2017.json"
# response = urlopen(json_url)
# # 读取数据
# req = response.read()
# print(req)
# # 将数据写入文件
# with open("btc_close_2017_urllib.json", "wb") as f:
#     f.write(req)
# # 加载json格式
# file_urllib = json.loads(req)
# print(file_urllib)

# json_url = "https://raw.githubusercontent.com/muxuezi/btc/master/
#     btc_close_2017.json"
# req = requests.get(json_url, timeout=(3, 7))
# # 将数据写入文件
# with open("btc_close_2017_request.json", "w") as f:
#     f.write(req.text)
# file_requests = req.json()
# print(file_requests)

# 16.2.2 提取相关的数据
import json
import math
from itertools import groupby

import pygal

# 将数据加载到一个列表中
filename = r"data_visualization\btc_close_2017_16_2.json"
with open(filename) as f:
    btc_data = json.load(f)
# 打印每一天的信息
for btc_dict in btc_data:
    date = btc_dict["date"]
    month = btc_dict["month"]
    week = btc_dict["week"]
    weekday = btc_dict["weekday"]
    close = btc_dict["close"]
    print(
        "{} is month {} week {}, {}, the close price is {} RMB".format(
            date, month, week, weekday, close
        )
    )

# 16.2.3 将字符串转换为数字值
# 将月序数、周序数、收盘价转换为整型数
# 打印每一天的信息
for btc_dict in btc_data:
    date = btc_dict["date"]
    month = int(btc_dict["month"])
    week = int(btc_dict["week"])
    weekday = btc_dict["weekday"]
    # int()不能将包含小数点的字符串数字直接转换为整型数
    close = int(float(btc_dict["close"]))
    print(
        "{} is month {} week {}, {}, the close price is {} RMB".format(
            date, month, week, weekday, close
        )
    )

# 16.2.4 绘制收盘价折线图
# 存储数据
dates, months, weeks, weekdays, close = [], [], [], [], []
for btc_dict in btc_data:
    dates.append(btc_dict["date"])
    months.append(int(btc_dict["month"]))
    weeks.append(int(btc_dict["week"]))
    weekdays.append(btc_dict["weekday"])
    close.append(int(float(btc_dict["close"])))

# 绘制折线图
# pygal.Line(
#     *args,
#     **kwargs: 接收数个关键字实参，均有默认值:
#         x_label_rotation=x轴标签旋转角度<浮点数>: 标签与x轴夹角，顺时针为正,
#         show_minor_x_labels=是否显示次要刻度<布尔>,
#         其他参数)
# 返回已参数新创建的折线图Line实例

# pygal.graph.line.Line实例常用属性：
# title<字符串>：折线图的总标题
# x_labels<一维列表>：待绘制数据横坐标
# x_labels_major<一维列表>：x轴刻度的坐标也即刻度标签，其元素中同时属于属性x_labels的元素对应的坐标显示刻度及刻度标签
line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = "收盘价（￥）"
line_chart.x_labels = dates
# x轴显示的刻度每隔20天一个
N = 20
line_chart.x_labels_major = dates[::N]
# pygal.graph.line.Line实例.add(
#     title=图例标签<字符串> | 无默认值,
#     values=待绘制数据点纵坐标<一维列表> | 无默认值,
#     **接收数个关键字实参，均有默认值)
# 在折线图实例上依数据绘制一条折线
line_chart.add("收盘价", close)
# pygal.graph.line.Line实例.render_to_file(
#     filename=文件路径<字符串> | 无默认值
#     *kwargs: 接收数个关键字实参，均有默认值)
# 依文件路径将折线图保存为矢量图文件
line_chart.render_to_file(r"data_visualization\收盘价折线图（￥）16_2.svg")

# 16.2.5 时间序列特征初探
# 时间序列分析目标：发现趋势、周期性、噪声，描述事实、预测未来、做出决策

# 对数变换消除非线性趋势
line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = "收盘价对数变换（￥）"
line_chart.x_labels = dates
# x轴显示的刻度每隔20天一个
N = 20
line_chart.x_labels_major = dates[::N]
close_log = [math.log10(_) for _ in close]
line_chart.add("log收盘价", close_log)
line_chart.render_to_file(r"data_visualization\收盘价对数变换折线图（￥）16_2.svg")
# 剔除非线性趋势后，可以发现，收盘价在3月、6月、9月都出现剧烈波动

# 16.2.6 收盘价均值
# 绘制前11个月的日均值（一月内收盘价总和/一月总天数）、前49周日均值（一周内收盘价总和/一周总天数）、每周中各天日均值


def draw_line(x_data, y_data, title, y_legend):
    xy_map = []
    # zip(
    #     待打包的可迭代对象1<迭代器>: 不接收关键字实参 | 无默认值,
    #     待打包的可迭代对象2<迭代器>: 不接收关键字实参 | 有无限个空元素的可迭代对象)
    # 返回一个可迭代对象，可迭代对象第i个的元素是由两个待打包可迭代对象中的第i个构成的一个二元组，
    #     二元组的第一个元素为待打包的可迭代对象1的元素，二元组的第二个元素为待打包的可迭代对象2的元素，
    #         两个元素在原序列中的索引相同且等于在返回值中的索引
    # 两个可迭代对象不等长时，舍弃长可迭代对象多余元素
    # grouby(
    #     iterable=待分组序列<列表/元组/字符串/其他多种可迭代元素> | 无默认值,
    #     key=分组依据<函数>: 返回作为分组标准的特征 | None: 返回元素本身，即值相等的分为一组)
    # 把可迭代对象中相邻的拥有相同指定特征的几个元素，分为一组
    # 返回一个可迭代对象，其元素索引为原序列从前到后分组的顺序（从0开始）
    # 其元素有两个元素，第一个元素为相同的特征，第二个元素为相邻的、特征相同的数据组成的次级序列，数据索引依在原序列中的前后顺序而定的
    # 该可迭代对象经一次遍历（如传入list()、在for循环中充当迭代器）后就清空
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):
        # 分组依据为作为元素的元组的第一个元素
        # x为月份序数/周序数/周几，y为二元组，元组第一个元素为月份序数/周序数/周几，第二个元素为收盘价
        # 将单月/周/天的收盘价组成列表
        y_list = [v for _, v in y]
        # 计算日均值并和月份序数/周序数/周几打包加入列表
        xy_map.append([x, sum(y_list) / len(y_list)])
    # *多维可迭代对象
    # 返回多个值，每个值为一个可迭代对象的元素
    # zip(
    #     *待解包的二维可迭代对象<列表/元素/其他可迭代对象> | 无默认值)
    # 返回一个可迭代对象，其元素为元组，第i个元组包含来自二维可迭代对象的每个子可迭代对象的第i个元素
    x_unique, y_mean = [*zip(*xy_map)]
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file("data_visualization\\" + title + "16_2.svg")
    return line_chart


# 绘制前11个月的日均值（一月内收盘价总和/一月总天数）
# 列表实例.index(
#     待求索引的元素<>: 仅限位置实参 | 无默认值,
#     求索引范围开头<整型数>: 仅限位置实参; 求索引范围的第一个值的索引;
#         索引超出列表最大索引时必定找不到元素报错 | 0,
#     求索引范围结尾<整型数>: 仅限位置实参; 求索引范围的最后一个值的索引加1; 范围不包括该索引对应的值; 可以超出列表最大索引;
#         结尾索引小于等于开头索引时必定找不到元素报错 | 列表最后一个元素的索引加1)
# 返回列表实例在指定范围内第一次出现的某个元素在原列表的索引
# 范围中没有该元素时报错
idx_month = dates.index("2017-12-01")
line_chart_month = draw_line(
    months[:idx_month], close[:idx_month], "收盘价月日均值（￥）", "月日均值"
)
# 收盘价7月下降，其他月上升，10到11月的增幅最大

# 绘制前49周（2017-01-02~2017-12-10）的日均值（一周内收盘价总和/一周总天数）
idx_week = dates.index("2017-12-11")
line_chart_week = draw_line(
    weeks[1:idx_week], close[1:idx_week], "收盘价周日均值（￥）", "周日均值"
)
# 收盘价与节假日无关

# 绘制2017-01-02~2017-12-10每周各天日均值
idx_week = dates.index("2017-12-11")
wd = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
weekdays_int = [wd.index(w) + 1 for w in weekdays[1:idx_week]]
line_chart_weekday = draw_line(
    weekdays_int, close[1:idx_week], "收盘价星期均值（￥）", "星期均值"
)
line_chart_weekday.x_labels = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
line_chart_weekday.render_to_file(r"data_visualization\收盘价星期均值（￥）16_2.svg")
# 收盘价在周一最低，周一到周四快速拉升，周四周五基本持平，之后增速放缓

# 16.2.7 收盘价数据仪表盘
# 将图表整合在一起，做一个收盘价数据仪表盘
with open(
    r"data_visualization\收盘价Dashboard16_2.html", "w", encoding="utf8"
) as html_file:
    first_row = "<html><head><title>收盘价Dashboard"
    html_file.write(first_row + "</title><metacharset='utf-8'></head><body>\n")
    for svg in [
        "收盘价折线图（￥）16_2.svg",
        "收盘价对数变换折线图（￥）16_2.svg",
        "收盘价月日均值（￥）16_2.svg",
        "收盘价周日均值（￥）16_2.svg",
        "收盘价星期均值（￥）16_2.svg",
    ]:
        # 图像默认高度为500像素，SVG为矢量图，可以任意缩放且不失真
        html_file.write(
            "    <object type='image/svg+xml' data='{0}'\
                height=500></object>\n".format(svg)
        )
    html_file.write("</body></html>")
