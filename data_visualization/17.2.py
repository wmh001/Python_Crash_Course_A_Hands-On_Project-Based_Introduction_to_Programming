# 17.2 使用Pygal可视化仓库
import pygal
import requests
from pygal.style import LightColorizedStyle as LCS
from pygal.style import LightenStyle as LS

# 执行API调用并存储响应
URL = "https://api.github.com/search/repositories?q=language:python&sort=star"
r = requests.get(URL)
print("Status code:", r.status_code)

# 将API响应存储在一个变量中
response_dict = r.json()
print("Total repositories:", response_dict["total_count"])

# 研究有关仓库的信息
repo_dicts = response_dict["items"]

names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict["name"])
    stars.append(repo_dict["stargazers_count"])

# 可视化
# pygal.style.LightenStyle(
#     color=基色<字符串>: 16进制颜色代码，#开头，其余6位为16进制数，前两个字符表示红色亮度，
#         中间两个字符表示绿色亮度，后两个字符表示蓝色亮度，颜色亮度的取值范围为00~FF | 无默认值,
#     step=<整型数> | 10,
#     max_ | None,
#     base_style=除其他指定参数外所有内容的样式<>: pygal.style.LightColorizedStyle浅色风格 | None,
#     **kwargs: 接收数个关键字实参，均有默认值)
# 返回新创建的符合参数的LightenStyle（样式Style类子类）实例
my_style = LS("#333366", base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = "Most-Starred Python Projects on GitHub"
chart.x_labels = names
chart.add("", stars)
chart.render_to_file(r"data_visualization\python_repos17_2_1.svg")

# 17.2.1 改进Pygal图表

# 改进标题字体大小、刻度标签字体大小
# 法一：
# 创建条形图实例时使用默认字体大小，创建后修改条形图实例config属性的style属性
# pygal.Config()
# 返回新创建的pygal.config.Config实例
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

my_style = LS("#333366", base_style=LCS)

chart = pygal.Bar(config=my_config, style=my_style)
chart.config.style.title_font_size = 24
chart.config.style.label_font_size = 14
chart.config.style.major_label_font_size = 18
chart.title = "Most-Starred Python Projects on GitHub"
chart.x_labels = names

chart.add("", stars)
chart.render_to_file(r"data_visualization\python_repos17_2_2_1.svg")

# 法二：
# 修改config实参的style属性，在创建条形图实例时舍去style实参
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
# my_config.style = LS("#333366", base_style=LCS)
my_config.style.title_font_size = 24
my_config.style.label_font_size = 14
my_config.style.major_label_font_size = 18
# Style实例在赋值时不修改提前指定且不冲突的属性
my_config.style = LS("#333366", base_style=LCS)

chart = pygal.Bar(config=my_config)
chart.title = "Most-Starred Python Projects on GitHub"
chart.x_labels = names

chart.add("", stars)
chart.render_to_file(r"data_visualization\python_repos17_2_2_2.svg")

# 法三：
# 创建style实参后，创建并修改修改style实参的属性
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

my_style = LS("#333366", base_style=LCS)

my_style.title_font_size = 24
my_style.label_font_size = 14
my_style.major_label_font_size = 18
# my_style = LS("#333366", base_style=LCS)
chart = pygal.Bar(config=my_config, style=my_style)
chart.title = "Most-Starred Python Projects on GitHub"
chart.x_labels = names

chart.add("", stars)
chart.render_to_file(r"data_visualization\python_repos17_2_2_3.svg")

# 法四：
# 修改创建Style实例时的参数
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

my_style = LS(
    "#333366",
    base_style=LCS,
    title_font_size=24,
    label_font_size=14,
    major_label_font_size=18,
)

chart = pygal.Bar(config=my_config, style=my_style)
chart.title = "Most-Starred Python Projects on GitHub"
chart.x_labels = names

chart.add("", stars)
chart.render_to_file(r"data_visualization\python_repos17_2_2_4.svg")

# 17.2.2 添加自定义工具提示
# SVG格式图像对光标和单击的响应称为工具提示
# 条形图的默认工具提示为光标移动到条形上时出现显示横坐标标签和纵坐标的方框

my_style = LS("#333366", base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart.title = "Python Projects"
chart.x_labels = ["public-apis", "system-design-primer", "awesome-python"]

plot_dicts = [
    {"value": 284431, "label": "Description of public-apis"},
    {"value": 248251, "label": "Description of system-design-primer"},
    {"value": 200034, "label": "Description of awesome-python"},
]

chart.add("", plot_dicts)
chart.render_to_file(r"data_visualization\bar_descriptions17_2_3.svg")

# 17.2.3 根据数据绘图
# 使plt_dicts[i]["values"]的值取决于绘图时刻的情况
print("Nameber of items:", len(repo_dicts))

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict["name"])

    plot_dict = {
        "value": repo_dict["stargazers_count"],
        "label": repo_dict["description"],
    }
    plot_dicts.append(plot_dict)

my_style = LS("#333366", base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart.title = "Python Projects"
chart.x_labels = names

chart.add("", plot_dicts)
chart.render_to_file(r"data_visualization\python_repos17_2_4.svg")

# 17.2.4 在图表中添加可单击的连接
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict["name"])

    plot_dict = {
        "value": repo_dict["stargazers_count"],
        "label": repo_dict["description"],
        "xlink": repo_dict["html_url"],
    }
    plot_dicts.append(plot_dict)

my_style = LS("#333366", base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart.title = "Python Projects"
chart.x_labels = names

chart.add("", plot_dicts)
chart.render_to_file(r"data_visualization\python_repos17_2_5.svg")
