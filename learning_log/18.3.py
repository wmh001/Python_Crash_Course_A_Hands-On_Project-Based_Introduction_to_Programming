# 18.3 创建网页：学习笔记主页
# 使用Django创建网页的过程分为三个阶段：定义URL模式、编写视图和编写模板
# URL模式描述了URL是如何设计的，让Django知道如何将浏览器请求与网站URL匹配
# 每个URL都映射到特定的视图，即视图函数获取并处理生成网页所需的数据
# 视图函数必有的参数是浏览器请求，还可能有的参数是URL提供的参数和其他参数，它调用一个生成网页的模板，准备好生成网页所需的数据
# 本节目标：创建学习笔记的主页、定义该主页的URL、编写其视图函数并创建一个简单的模板

# 18.3.1 映射URL
# 文件项目名(learning_log)\urls.py的列表urlpatterns包含项目中应用程序的URL模式及与URL模式有映射关系的视图函数
# URL模式表示为正则表达式字符串格式的
# Django在列表urlpatterns中查找与请求的URL字符串匹配的正则表达式字符串，请求的URL不与任何正则表达式字符串表达的URL匹配时返回错误页面

# 在其内添加应用程序（learning_logs）的URL

# 在应用程序目录(learning_logs)创建urls.py文件
# 创建列表urlpatterns，包含本应用程序所有网页的URL模式及视图函数

# 在其内添加应用程序主页URL

# 18.3.2 编写视图
# 在 应用程序目录(learning_logs)\view.py编写视图函数

# 18.3.3 编写模板
# 模板定义了网页结构
# 当网页被请求时，Django将根据请求在模板内填入数据

# 在应用程序目录(learning_logs)创建不提供数据的简单模板：
# 在应用程序目录(learning_logs)新建文件夹templates
# 在文件夹templates中新建文件夹，以应用程序名(learning_logs)命名
# 在 应用程序目录(learning_logs)\templates\应用程序名(learning_logs)新建模板(index.html)

# html文件中
# p标签表示段落
#     <P>段落内容</p>
# 显示一个段落

#  将定义并处理模型、处理URL、编写视图函数、编写模板的工作分离有利于团队分工
