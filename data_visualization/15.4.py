# 15.4 使用Pygal模拟掷骰子
# Pygal是可视化包，可以生成可缩放可交互的矢量图，以适应尺寸不同的屏幕

# 15.4.1 安装Pygal
# Linux/OS x：pip install --user pygal
# Windows：python -m pip install pygal

# 15.4.2 Pygal画廊
# 访问http://www.pygal.org

# 15.4.3 创建Die类

# 15.4.4 掷骰子
import pygal
from die15_4 import Die

# 创建一个六面骰子
die = Die()

# 掷几次骰子，并保存结果
results = []
for _ in range(100):
    result = die.roll()
    results.append(result)

print(results)

# 15.4.5 分析结果
results = []
for _ in range(1000):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []
for value in range(1, die.num_sides + 1):
    # 列表.count(
    #     被统计的元素<>: 仅限位置实参 | 无默认值)
    # 返回被统计的元素在列表中出现的次数
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# 15.4.6 绘制直方图
# 对结果进行可视化
# pygal.Bar(
#     config=配置参数<pygal.config.Config类> | None: 默认配置,
#     **kwargs: 接收数个关键字实参，均有默认值:
#         style=图像样式<pygal.style.Style类>,
#         x_label_rotation=x轴标签旋转角度<浮点数>: 与x轴夹角，顺时针为正 | 0,
#         show_legend=是否显示左上角图例<布尔> | True,
#         其他参数)
# 返回依参数新创建的条形图Bar实例
# 注意在同时传递参数config和参数style时，参数config属性style的属性与参数style的属性冲突时以参数style的属性为准，
#     即使参数config的属性为指定的而参数style的属性为默认的也如此
# 在只传递参数config时，以参数config的属性为准
# pygal 2.0.0发生了变动，Config类的属性title_font_size、label_font_size、
#     major_label_font_size迁移到Style类中，因此在参数config的属性中指定字体大小属性而在参数style中使用默认字体大小属性则指定无效
# 条形图在浏览器中打开后有交互性，如鼠标指向条形时会显示其数据

# pygal.graph.bar.Bar实例的常用属性：
# title<字符串>：条形图的总标题
# x_labels<一维列表>：数据横坐标也即x轴的次要刻度标签
# x_title<字符串>：x轴标签
# y_title<字符串>：y轴标签
# config<pygal.config.Config（配置）类>：条形图的配置参数

# pygal.config.Config实例的常用属性：
# x_label_rotation<浮点数>：x轴标签与x轴夹角，顺时针为正
# show_legend<布尔>：是否显示左上角图例
# truncate_label<整型数>；显示主要刻度标签的字数上限，超过上限的字以···代替，光标指向时显示全名
# show_y_guides<布尔>：是否显示图像中的水平虚线和x轴
# width<浮点数>：图像宽度
# style<pygal.style.Style（样式）类及其子类>：样式，如颜色、字体大小等

# pygal.style.Style实例的常用属性：
# title_font_size<浮点数>：图表标题字体大小
# label_font_size<浮点数>：次要刻度标签字体大小
# major_label_font_size<浮点数>：主要刻度标签字体大小
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ["1", "2", "3", "4", "5", "6"]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

# pygal.Bar实例.add(
#     title=图例标签<字符串> | 无默认值,
#     values=数据<整型数列表/浮点数列表/字典列表>: 字典列表的元素格式为{"value": 纵坐标<浮点数/整型数>,
#         "label": 默认工具提示外的工具提示, "xlink": 单击条形时跳转的链接, 其他键值对} | 无默认值,
#     **kwargs: 接收数个关键字实参，均有默认值)
# 依数据绘制条形图
# 条形图的工具提示为光标移动到条形上时出现的方框上显示的信息
hist.add("D6", frequencies)
# pygal.Bar实例.render_to_file(
#     filename=文件路径<字符串> | 无默认值
#     *kwargs: 接收数个关键字实参，均有默认值)
# 依文件路径保存条形图
hist.render_to_file(r"data_visualization\die_visual15_4_1.svg")

# 15.4.7 同时掷两个骰子
die_1 = Die()
die_2 = Die()

# 掷多次两骰子，并保存结果之和
results = []
for _ in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times."
hist.x_labels = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6 + D6", frequencies)
hist.render_to_file(r"data_visualization\die_visual15_4_2.svg")

# 15.4.8 同时掷两个面数不同的骰子
die_1 = Die()
die_2 = Die(10)

# 掷多次两骰子，并保存结果之和
results = []
for _ in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "Results of rolling a D6 and a D10 50000 times."
hist.x_labels = [
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6 + D10", frequencies)
hist.render_to_file(r"data_visualization\die_visual15_4_3.svg")
