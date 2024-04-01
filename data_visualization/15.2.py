# 15.2 绘制简单的折线图
import matplotlib.pyplot as plt

# matplotlib模块绘制图像过程：
# 创建matplotlib.figure.Figure（图表）实例，用于管理图表
# 在图表实例的不同位置创建若干matplotlib.axes._axes.Axes（轴域/子图）实例，用于管理一个轴域，
# 轴域是一个属于同一坐标系的坐标轴及其标签、坐标刻度及其标签、坐标系内的图像等元素组成的集体
# 一个图表实例默认创建一个覆盖整个图表的轴域实例

squares = [1, 4, 9, 16, 25]
# matplotlib.pyplot.plot(
#     *args: 接收数个坐标序列<元组/列表/np数组/pd数组/pd表格>及一个可选的格式控制字符串<字符串>:
#         坐标序列:
#             接收一个一维坐标序列时，以索引转换为整型数作横坐标，以对应的序列元素作纵坐标;
#             接收两个一维坐标序列，且第一个一维序列元素为数字时，以第一个序列为横坐标序列，第二个序列为纵坐标序列，索引相等的配对为一个点;
#             接收两个一维坐标序列，且第一个一维序列元素不为数字时，以第一个序列的索引转换为数字作横坐标，以横坐标序列的元素作为横坐标刻度标签
#                 （会自动周期性隐藏部分标签，防止标签重叠，使刻度标签等距且清晰），第二个序列为纵坐标序列，索引相等的配对为一个点;
#             有多个一维坐标序列时，一二配对绘制一条折线，三四配对绘制另一条折线，依次类推，每对按上文有两个坐标序列时处理;
#             使用多维np数组和pd表格时，有更加复杂的配对方式;
#             配对的两个一维序列的元素数量必须相等 | 无默认值,
#         格式控制字符串:
#             有3个部分字符串拼接组成：颜色、标记样式、线条样式，不同部分的可选字符串为matplotlib模块通用字符符号，如下，
#                 注意此处颜色部分仅支持单字符符号 | "b-": 蓝色无点型实线,
#     scalex,
#     scaley,
#     data,
#     **kwargs: 接收数个关键字实参，均有默认值:
#         color=线颜色<字符串/三元组/四元组>: 可选字符串参数为matplotlib模块通用字符符号; 可选元组参数为元组表示的
#             [0,1]浮点数RGB和RGBA颜色 | "b",
#         linewidth=线宽<浮点数>,
#         linestyle=线条的样式<字符串>: 除了支持matplotlib模块通用字符符号，还支持""无线条只显示标记、
#             "None"无线条不显示标记、" "无线条不显示标记 | "-",
#         marker=标记样式<字符串>: 可选参数为matplotlib模块通用字符符号 | "",
#         markersize=标记尺寸<浮点数>,
#         markerfacecolor=标记填充色<字符串>: 可选参数为matplotlib模块通用字符符号 | 与参数color相同,
#         markeredgewidth=标记边缘宽度<浮点数>,
#         markeredgecolor=标记边缘颜色<字符串>: 可选参数为matplotlib模块通用字符符号 | 与参数color相同,
#         label=线条的图例标签<字符串>,
#         alpha=线条和标记的透明度<浮点数>: 用0~1浮点数表示 | 1,
#         zorder=绘图的图层编号<整形数>: 数值越大越靠上,
#         solid_capstyle=实线端点样式<字符串>: butt普通平直样式、round圆角样式、projecting斜角样式等
#             | "butt",
#         dash_capstyle=虚线端点样式<字符串>: butt普通平直样式、round圆角样式、projecting斜角样式等
#             | "butt",
#         dash_joinstyle=虚线连接处样式<字符串>: round圆弧连接、bevel斜接连接、miter锐角连接等,
#         solid_joinstyle=实线连接处的样式<字符串>: round圆弧连接、bevel斜接连接、miter锐角连接等,
#         markevery=标记显示的间隔<整型数/二元组/函数>: 接收整型数n，表示每隔n-1个数据点标记一个点;
#             接收二元组(n<整型数>, m<整型数>)，表示从索引为n的数据点开始，每隔m个数据点标记一个点;
#             接收函数，表示根据某个函数的返回值来控制标记的位置 | 1: 每个点都标记,
#         其他参数)
# 在当前轴域实例中依据参数绘制折线图

# matplotlib模块通用字符符号：
# 颜色：c青、r/red红、g/green绿、b/blue蓝、w/white白、k/black黑、y黄、m洋红等
# 标记样式：空字符串无标记、o实心圆、.小点、,像素点、v朝下三角形、^朝上三角形、<朝左三角形、>朝右三角形、
#     1朝下Y形、2朝上Y形、3朝左Y形、4朝右Y形、s正方形、p五边形、*五角星、8八边形、h纵向六角形、H横向六角形、
#     +细加号、P粗加号、x细叉号、X粗叉号、D宽菱形、d窄菱形、|垂直线、_水平线等
# 线条样式：:点线、-.点划线、--虚线、-实线等

plt.plot(squares, linewidth=5)

# 15.2.1 修改标签文字和线条粗细
# 设置轴域的标题，并给坐标轴加上标签
# matplotlib.pyplot.title(
#     label=标题<字符串> | 无默认值,
#     fontdict=标题的字体属性<字典>: 可选键值对：family:字体族<字符串/列表>、
#         fontsize/size:字体大小<浮点数>、color:字体颜色<字符串>: 可选参数为matplotlib模块通用字符符号、
#         fontweight/weight:字体粗细<字符串/整型数>: 可选字符串参数：normal普通字体，bold粗体等;
#             可选整型数参数：400普通字体，700粗体等、其他键值对 |,
#     loc=标题的位置<字符串>: left左、center中、right右 | "center",
#     pad=标题与图形边界的距离<浮点数> |,
#     y: 仅限关键字实参
#     **kwargs: 接收数个关键字实参，均有默认值:
#         fontsize=字体大小<整型数/字符串>: 可选字符串参数：xx-small、
#             x-small、small、medium、large、x-large、xx-large等 | 12,
#         fontweight=字体粗细<整型数/字符串>: 可选字符串参数：light、normal、
#             medium、semibold、bold、heavy、black等 | "normal",
#         fontstyle=字体类型<字符串>: normal、italic斜体、oblique倾斜等 | "normal",
#         verticalalignment=水平对齐方式<字符串>: center、top、bottom、baseline等,
#         horizontalalignment=垂直对齐方式<字符串>: left、right、center等,
#         rotation=旋转角度<浮点数/字符串>: 浮点数为角度制，角度为与x轴夹角，逆时针为正;
#             可选字符串参数：vertical、horizontal等 | 0,
#         alpha=透明度<浮点数>: 用0~1浮点数表示 | 1,
#         backgroundcolor=标题背景颜色<字符串>: 可选参数为matplotlib模块通用字符符号,
#         bbox=标题外框形式<字典>: 可选键值对：boxstyle:方框外形<字符串>、facecolor/fc:背景颜色<字符串>: 可选参数为matplotlib模块通用字符符号、
#             edgecolor/ec:边框线条颜色<字符串>: 可选参数为matplotlib模块通用字符符号、其他键值对 | 无标题外框,
#         其他参数)
# 在当前轴域实例中依据参数添加标题
plt.title("Square Numbers", fontsize=24)
# matplotlib.pyplot.xlabel(
#     xlabel=x轴标签<字符串> | 无默认值,
#     fontdict=标签的字体属性<字典>: 常用键值对：family:字体族<字符串/列表>、size:字体大小<浮点数>、
#         color:字体颜色<字符串>: 可选参数为matplotlib模块通用字符符号、weight:字体粗细<字符串/整型数>:
#             可选字符串参数：normal普通字体，bold粗体等; 可选整型数参数：400普通字体，700粗体等、其他键值对 |,
#     labelpad=标签与坐标轴距离<浮点数> |,
#     loc=标签的位置<字符串>: 仅限关键字实参; 可选参数：left左、center中、right右 |,
#     **kwargs: 接收数个关键字实参，均有默认值:
#         fontsize=字体大小<整型数/字符串>: 可选字符串参数：xx-small、
#             x-small、small、medium、large、x-large、xx-large等 | 12,
#         fontweight=字体粗细<整型数/字符串>: light、normal、medium、
#             semibold、bold、heavy、black等 | "normal",
#         fontstyle<字符串>字体类型: normal、italic斜体、oblique倾斜等 | "normal",
#         verticalalignment=水平对齐方式<字符串>: center、top、bottom、baseline等,
#         horizontalalignment=垂直对齐方式<字符串>: left、right、center等,
#         rotation=旋转角度<浮点数/字符串>: 浮点数为角度制，角度为与x轴夹角，逆时针为正;
#             可选字符串参数：vertical、horizontal等 | 0,
#         alpha=透明度<浮点数>: 用0~1浮点数表示 | 1,
#         backgroundcolor=标签背景颜色<字符串>: 可选参数为matplotlib模块通用字符符号,
#         bbox=标签外框形式<字典>: 可选键值对：boxstyle:方框外形<字符串>、facecolor/fc:背景颜色<字符串>: 可选参数为matplotlib模块通用字符符号、
#             edgecolor/ec:边框线条颜色<字符串>: 可选参数为matplotlib模块通用字符符号、其他键值对 | 无标签外框,
#         其他参数)
# 在当前轴域实例中依据参数添加x坐标轴标签
plt.xlabel("Value", fontsize=14)
# matplotlib.pyplot.ylabel(
#     ylabel=y轴标签<字符串> | 无默认值,
#     fontdict=标签的字体属性<字典>: 常用键值对：family:字体族<字符串/列表>、size:字体大小<浮点数>、
#         color:字体颜色<字符串>: 可选参数为matplotlib模块通用字符符号、weight:字体粗细<字符串/整型数>:
#             可选字符串参数：normal普通字体，bold粗体等; 可选整型数参数：400普通字体，700粗体等、其他键值对 |,
#     labelpad=标签与坐标轴距离<浮点数> |,
#     loc=标签的位置<字符串>: 仅限关键字实参; 可选参数：top顶、center中、bottom底 |,
#     **kwargs: 接收数个关键字实参，均有默认值:
#         fontsize=字体大小<整型数/字符串>: 可选字符串参数：xx-small、
#             x-small、small、medium、large、x-large、xx-large等 | 12,
#         fontweight=字体粗细<整型数/字符串>: light、normal、medium、
#             semibold、bold、heavy、black等 | "normal",
#         fontstyle<字符串>字体类型: normal、italic斜体、oblique倾斜等 | "normal",
#         verticalalignment=水平对齐方式<字符串>: center、top、bottom、baseline等,
#         horizontalalignment=垂直对齐方式<字符串>: left、right、center等,
#         rotation=旋转角度<浮点数/字符串>: 浮点数为角度制，角度为与x轴夹角，逆时针为正;
#             可选字符串参数：vertical、horizontal等 | 90,
#         alpha=透明度<浮点数>: 用0~1浮点数表示 | 1,
#         backgroundcolor=标签背景颜色<字符串>: 可选参数为matplotlib模块通用字符符号,
#         bbox=标签外框形式<字典>: 可选键值对：boxstyle:方框外形<字符串>、facecolor/fc:背景颜色<字符串>: 可选参数为matplotlib模块通用字符符号、
#             edgecolor/ec:边框线条颜色<字符串>: 可选参数为matplotlib模块通用字符符号、其他键值对 | 无标签外框,
#         其他参数)
# 在当前轴域实例中依据参数添加y坐标轴标签
plt.ylabel("Square of Value", fontsize=14)
# matplotlib.pyplot.tick_params(
#     axis=作用与哪个轴<字符串>: x（x轴）、y（y轴）、both（x轴和y轴） | "both",
#     **kwargs: 接收数个关键字实参，均有默认值:
#         which=作用于哪个刻度线<字符串>: major主要刻度线、minor次要刻度线、both主要和次要刻度线 | "major",
#         reset=更新设置之前是否将刻度重置为默认情况<布尔> | False,
#         direction=刻度相对于坐标系的位置<字符串>: in里侧、out外侧、inout里侧和外侧 | "out",
#         length=刻度线的长度<整型数>,
#         width=刻度线的宽度<整型数>,
#         color=刻度线的颜色<字符串>: 可选参数为matplotlib模块通用字符符号,
#         pad=刻度与对应标签的距离<整型数>,
#         labelsize=刻度标签的字体大小<整型数>,
#         labelcolor=刻度标签的字体颜色<字符串>: 可选参数为matplotlib模块通用字符符号,
#         labelrotation=刻度标签的旋转角度<浮点数>: 角度制，角度为与x轴夹角，逆时针为正 | 0,
#         其他参数)
# 在当前轴域实例中依据参数改变刻度、刻度标签、网格线的外观
# matplotlib.pyplot.plot()会创建默认刻度和刻度标签
plt.tick_params(axis="both", labelsize=14)
# matplotlib.pyplot.show()
# 还没有窗口将新建窗口，将当前绘制的图表实例显示在该窗口中；已有窗口会用当前绘制的图表实例覆盖窗口内的图表实例
# 执行后更新当前图表实例为新建的空白图表实例
plt.show()

# 15.2.2 校正图形
# 横坐标修正为从1开始
input_values = [1, 2, 3, 4, 5]
plt.plot(input_values, squares, linewidth=5)
# 设置标题、坐标轴和标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# 设置刻度标记的大小
plt.tick_params(axis="both", labelsize=14)
plt.show()

# 15.2.3 使用scatter()绘制散点图并设置其样式
# matplotlib.pyplot.scatter(
#     x=横坐标序列<整型数/浮点数/列表/元组/np数组>: 整型数和浮点数表示只绘制一个点 | 无默认值,
#     y=纵坐标序列<整型数/浮点数/列表/元组/np数组>: 整型数和浮点数表示只绘制一个点;
#         横坐标序列和纵坐标序列的元素数应相等，索引相同的元素配对 | 无默认值,
#     s=点的直径<整型数> | 20,
#     c=点颜色<字符串/二维行列表/浮点数列表>: 可选字符串参数为matplotlib模块通用字符符号; 二维行列表参数格式为[0,1]浮点数RGB或RGBA;
#         浮点数列表为进行颜色映射的数据 | "b",
#     marker=点样式<字符串>: 可选参数为matplotlib模块通用字符符号 | "o",
#     cmap=调色板<标量/matplotlib.pyplot.cm定义的colormap量>: 仅当c是一个浮点数列表的时候才使用 |,
#     norm=亮度1<浮点数>: 仅当c是一个浮点数列表的时候才使用，在0~1之间 |,
#     vmin=亮度21<浮点数>: 亮度21与亮度22一起用来进行亮度数据的归一化，当亮度1存在的时候忽略 |,
#     vmax=亮度22<浮点数>: 亮度22与亮度21一起用来进行亮度数据的归一化，当亮度1存在的时候忽略 |,
#     alpha=透明度<浮点数>: 用0~1浮点数表示 | 1,
#     linewidths=标记点的长度<整型数> |,
#     edgecolors=边缘颜色<字符串>: 仅限关键字实参; 可选参数为matplotlib模块通用字符符号 | 与参数c相同,
#     plotnonfinite=是否使用非限定的绘制点<布尔>: 仅限关键字实参; 非限定的绘制点包括inf、-inf和nan | False,
#     data: 仅限关键字实参 |,
#     **kwargs: 接收数个关键字实参，均有默认值:
#         edgecolor=边缘颜色<字符串>: 除了支持matplotlib模块通用字符符号，还支持"none"无边缘)
# 在当前轴域实例中依参数绘制散点图
plt.scatter(2, 4, s=200)
# 设置标题、坐标轴和标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# 设置刻度标记的大小
plt.tick_params(axis="both", labelsize=14)

plt.show()

# 15.2.4 使用scatter()绘制一系列点
# 向scatter()传递列表
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.scatter(x_values, y_values, s=100)
# 设置标题、坐标轴和标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# 设置刻度标记的大小
plt.tick_params(axis="both", labelsize=14)

plt.show()

# 15.2.5 自动计算数据
# 使用循环
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, s=40)
# 设置标题、坐标轴和标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# 设置刻度标记的大小
plt.tick_params(axis="both", labelsize=14)

# matplotlib.pyplot.axis(
#     *args: 接收坐标轴的取值范围<字符串/列表/布尔>):
#         可选字符串参数：on显示四边坐标轴、坐标刻度及其标签、坐标轴标签，off不显示四边坐标轴、坐标刻度及其标签、坐标轴标签，
#             equal通过调整两轴范围保证两轴单位长度相等，scaled通过固定两轴长度比保证两轴的单位长度相等，square两轴长度、
#             跨度和单位长度相同，tight两轴范围仅在有数据的区域，auto自动确定坐标轴范围、单位长度和长度;
#         列表格式：[x轴最小值<浮点数>, x轴最大值<浮点数>, y轴最小值<浮点数>, y轴最大值<浮点数>] | "auto",
#     emit=是否通知观察者轴范围更改<布尔> | True,
#     **kwargs: 接收数个关键字实参，均有默认值:
#         xmin=x轴最小值<浮点数>,
#         xmax=x轴最大值<浮点数>,
#         ymin=y轴最小值<浮点数>,
#         ymax=y轴最大值<浮点数>,
#         其他参数)
# 设置当前轴域实例的每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

plt.show()

# 15.2.6 删除数据点的轮廓
# scatter()绘制的散点图默认为蓝色填充、同填充色轮廓
plt.scatter(x_values, y_values, edgecolor="none", s=40)
# 设置标题、坐标轴和标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# 设置刻度标记的大小
plt.tick_params(axis="both", labelsize=14)
plt.axis([0, 1100, 0, 1100000])

plt.show()

# 15.2.7 自定义颜色
plt.scatter(x_values, y_values, c="red", edgecolor="none", s=40)
# 设置标题、坐标轴和标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# 设置刻度标记的大小
plt.tick_params(axis="both", labelsize=14)
plt.axis([0, 1100, 0, 1100000])

plt.show()

# 使用[0,1]浮点数RGB颜色
plt.scatter(x_values, y_values, c=[[0, 0, 0.8]], edgecolor="none", s=40)
# 设置标题、坐标轴和标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# 设置刻度标记的大小
plt.tick_params(axis="both", labelsize=14)
plt.axis([0, 1100, 0, 1100000])

plt.show()

# 15.2.8 使用颜色映射
# 使用调色板
# 颜色映射是一系列颜色
# scatter()使用颜色映射时先将c设置为进行映射的浮点数列表
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor="none", s=40)
# 设置标题、坐标轴和标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# 设置刻度标记的大小
plt.tick_params(axis="both", labelsize=14)
plt.axis([0, 1100, 0, 1100000])

# 15.2.9 自动保存图表
# matplotlib.pyplot.savefig(
#     *args: 接收文件路径<字符串> | 无默认值,
#     **kwargs: 接收数个关键字实参，均有默认值:
#         fname=文件路径<字符串> | 与*args相同,
#         dpi=分辨率<浮点数/matplotlib.figure.Figure类>: 浮点数单位为每英寸的像素点数; 接收matplotlib.figure.Figure类时
#             将使用该图表实例的分辨率 | matplotlib.rcParams["savefig.dpi"],
#         quality=jpg/jpeg文件输出的质量<整型数>: 仅对jpg或jpeg文件生效;
#             建议取值范围为1~95，超过100将会禁用jpeg压缩算法，可能会导致文件过大 | 95,
#         facecolor=图表背景色<字符串>: 可选参数为matplotlib模块通用字符符号 | "auto": 使用当前图表实例的背景色,
#         edgecolor=图表边缘颜色<字符串>: 可选参数为matplotlib模块通用字符符号 | "auto": 当前图表实例边缘颜色,
#         orientation=图表方向<字符串>: landscape横向、portrait纵向 | "portrait",
#         papertype=纸张大小<字符串>: letter、legal、executive、ledger、a0~a10、b0~b10
#             |,
#         format=保存格式<字符串>: eps、jpeg、jpg、pdf、pgf、png、ps、raw、rgba、svg、svgz、
#             tif、tiff |,
#         backend=使用非默认后端渲染文件<字符串> |,
#         bbox_inches=图表多余白色空白区处理方式<字符串> |,
#         pad_inches=图表周围填充<浮点数> | 0.1,
#         其他参数)
# 保存当前图表实例为一个图像文件
# matplotlib.pyplot.show()后更新当前图表实例为新建的图表实例，如果此时立即保存图表实例，会保存空白图表
plt.savefig(r"data_visualization\squares_plot15_2.png", bbox_inches="tight")

plt.show()
