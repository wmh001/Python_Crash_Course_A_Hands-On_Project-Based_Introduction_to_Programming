# 20.1 设置项目“学习笔记”的样式
# 使用Bootstrap库

# 20.1.1 应用程序django-bootstrap3
# 使用django-bootstrap3来继承到项目中

# 激活环境后，执行pip install django-bootstrap3
# 在 项目名(learning_log)\settings.py列表INSTALLED_APPS中添加应用程序bootstrap3

# django-bootstrap3的JavaScript库的jQuery可以让开发者使用Bootstrap模板提供的一些交互元素
# 在 项目名(learning_log)\settings.py末尾添加字典BOOTSTRAP3，开启jQuery

# 20.1.2 使用Bootstrap来设置项目“学习笔记”的样式
# Bootstrap提供了大量的模板
# 访问http://getbootstrap.com/ ，单击Getting Started，向下滚动到Examples，找到Navbars in action
# 本项目使用模板Static top navbar，提供了简单的顶部导航条、页面标题和用于放置页面内容的容器

# 20.1.3 修改base.html
# 修改 learning_logs\templates\learning_logs\base.html
# 因显示错误，修改模块django-bootstrap3中bootstrap.py文件的链接字符串
# 其他两种解决方案：下载本地文件；在base.html中修改链接

# 在html文件中
# <!DOCTYPE html>
# HTML5 的文档类型声明，它告诉浏览器当前页面是使用 HTML5 规范编写的，

# html标签表示该页面是html语言
#     <html lang=标识语言(字符串): en英文、en-US美式英文、zh-CN/zh中文、ja日文;
#             标识该网页使用什么语言，对网页渲染没有影响，对第三方功能可能有作用，如翻译插件检测到这个字段就会提示是否翻译>
#     文件内容</html>
# 整个html文件的根标签

# head标签表示头部
#     <head>头部标签元素</head>
# 包含所有的头部标签元素，包括<title>标题、<style>、<meta>、<link>、<script>脚本、<noscript>和<base>

# base标签表示基本的超链接
#     <base href=超链接URL(字符串)>
# 该文件中所有的链接标签的默认链接

# link标签表示外部资源
#     <link rel=外部资源在当前文档中发挥的作用(字符串): stylesheet外部CSS样式表、icon网站图标
#         href=网络资源的URL或本地资源的路径(字符串)
#         integrity=基于资源内容的哈希值(字符串): 用于确保外部资源的完整性; 与crossorigin属性一起使用
#         crossorigin=资源的CORS（跨源资源共享）设置(字符串): anonymous跨域请求不发送cookie、HTTP认证信息等凭证信息;
#             use-credentials跨域请求发送凭证信息; null不返回跨域资源并报错，适用于跨域资源加载失败时的处理 | "anonymous">
# 导入来自网络或其他本地文件夹的外部资源

# script标签表示脚本
#     <style src=外部脚本的URL或本地路径(字符串)
#         integrity=于资源内容的哈希值(字符串): 用于确保外部资源的完整性; 与crossorigin属性一起使用
#         crossorigin=资源的CORS（跨源资源共享）设置(字符串): anonymous跨域请求不发送cookie、HTTP认证信息等凭证信息;
#             use-credentials跨域请求发送凭证信息; null不返回跨域资源并报错，适用于跨域资源加载失败时的处理 | "anonymous">
# 导入来自网络或其他本地文件夹的JavaScript脚本代码

# meta标签表示元数据，用来描述一个html文件的属性，不显示在页面上，但可用于浏览器设置更新频度、搜索关键词或其他web服务

#     <meta charset=html文件的字符编码(字符串): gb2312中文简体字符编码; big5中文繁体字符编码;
#             utf-8国际通用字符编码; ISO-8859-1英文字符/拉丁字母表的字符>
#     设置文件的字符编码

#     <meta http-equiv=参数(字符串) content=对应参数的实参(字符串)>
#     向浏览器传递一些有用的信息，以帮助正确和精确地显示网页内容
#     常用参数及其作用：
#     Expires  网页的到期时间: 网页过期后，必须到服务器上重新传输; 格式为GMT时间的字符串格式
#     Pragma  是否禁止浏览器从本地计算机的缓存中访问页面内容: no-cache禁止浏览器从本地计算机的缓存中访问页面内容
#     Refresh  间隔多少时间自动刷新并指向哪个新页面: 间隔几秒自动刷新到的URL网址; 缺省URL时指向本页面
#     X-UA-Compatible 采用何种IE版本去渲染网页: IE=版本号 使用指定版本的IE渲染; IE=edge 使用最新版本的IE渲染;
#         chrome=1 使用Chrome Frame渲染; 同时使用IE和Chrome时，用,连接

#     <meta name=参数(字符串) content=对应参数的实参(字符串)>
#     用于描述网页
#     常用参数及其作用：
#     Keywords  给搜索引擎提供关键字
#     description  网站内容描述
#     author  作者

# title标签表示标题
#     <title>标题</title>
# 定义网页在浏览器标题栏显示的标题，同时也是当网页添加到收藏夹时在收藏夹中显示的标题和在搜索引擎结果页面显示的标题

# body标签表示主体
#     <body>页面内容</body>
# 包含用户看到的页面内容

# nav标签表示导航标签区域
#     <nav class=样式类名(字符串): 导入样式表中的类用于设置样式; 如需为一个元素规定多个类，用空格分隔类名;
#             navbar-static-top导航条静止在顶部并会跟着网页滚动而滚动; navbar navbar-default默认浅灰色导航条>
#     导航标签内容</nav>
# 显示导航标签区域

# div标签表示容器
#     <div class=样式类名(字符串): 导入样式表中的类用于设置样式; 如需为一个元素规定多个类，用空格分隔类名;
#             container设置容器固定宽度并支持响应式布局; navbar-header设置容器包含宽度不足的窗口下可见元素即站点名称及按钮（站点名称是
#             navbar-brand样式的链接，在任何宽度的窗口下可见，按钮是navbar-toggle类的按钮，只在宽度不足的窗口下可见）;
#             navbar-collapse collapse设置容器为导航条组件各列表项的父元素，窗口宽度不足时可以折叠本容器，
#             在窗口宽度不足时的初始状态是折叠; page-header页面标题; jumbotron容器显示为包含某些元素的灰色背景大框;
#             panel panel-default默认面板样式; panel-heading面板标题; panel-body面板主体
#         id=控件id(字符串)>
#     容器元素</div>
# 将相关的元素组合在一起，方便对这些元素进行统一的样式设置和控制

# 模板标签：
# {% load 模板标签集名 %}
# 导入模板标签集

# {% bootstrap_css %}
# 导入模板标签集中的Bootstrap库的CSS

# {% bootstrap_javascript %}
# 导入模板标签集中的Bootstrap库的JS

# 20.1.4 使用jumbotron设置主页的样式
# Bootstrap的jumbotron元素是一个包含某些元素的大框，常用于在主页呈现项目的简要描述

# html文件中
# h1标签表示一级标题
#     <h1>一级标题</h1>
# 显示一级标题

# h2标签表示二级标题
#     <h2>二级标题</h2>
# 显示二级标题

# 20.1.5 设置登录页面坐标的样式
# 模板标签
# {% bootstrap_form 表单名 %}
# 将Bootstrap样式规则应用于各个表单元素

# {% buttons %}按钮控件{% endbuttons %}
# 将Bootstrap样式应用于按钮

# 20.1.6 设置new_topic页面的样式

# 20.1.7 设置topics页面的样式
# html文件中
# h3标签表三级标题
#     <h3>三级标题</h3>
# 显示三级标题

# h4标签表四级标题
#     <h4>四级标题</h4>
# 显示四级标题

# 20.1.8 设置topic页面中条目的样式
# 用Bootstrap面板panel来突出每个条目
# 面板是一个带预定义样式的容器，包括面板标题和面板主体

# html文件中
# small标签表示小字号
#     <small>内容</small>
# 显示比外层标签的内容字号稍小的内容，如果外层标签的内容字体已经是所支持的最小字号，那么该标签无影响

# 20.1.9 设置其他页面的样式
