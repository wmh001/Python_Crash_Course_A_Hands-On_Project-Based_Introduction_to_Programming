# 19.1 让用户能够输入数据
# 创建用户添加新主题的网页、添加新条目的网页以及编辑条目的网页
# 使用Django表单工具

# 19.1.1 添加新主题
# 让用户输入并提交信息的页面称为表单
# 用户输入信息时，需要进行验证，确认信息正确且无恶意，然后创建存储输入信息的模型并将其保存到数据库
# Django中创建表单最简单的方法是使用ModelForm，根据模型信息自动创建表单
# 定义django.forms.ModelForm（表单）子类用于管理表单
# 在应用程序目录(learning_logs)创建文件forms.py，定义类TopicForm

# 在 应用程序目录(learning_logs)\urls.py添加URL new_topic/
# 在 应用程序目录(learning_logs)\views.py添加视图函数new_topic()
# 两个作用：准备添加主题网页和提交数据后跳转到显示所有主题网页

# GET请求：用于从服务器读取数据的网页
# POST请求：用于用户通过表单提交信息的网页

# 在 应用程序目录(learning_logs)\templates\应用程序名(learning_logs)创建新模板new_topic.html

# 在html文件中
# form标签表示表单
#     <form action=接收数据的URL(字符串): 空字符串默认提交至当前页面URL
#         method=提交表单数据的方式(字符串): "get"和"post"
#         class=样式类名(字符串): 导入样式表中的类用于设置样式; 如需为一个元素规定多个类，用空格分隔类名;
#             form表单样式>
#     表单内容</form>
# 显示一个表单

# button标签表示按钮
#     <button name=按钮的名称(字符串)
#         type=按钮的类型(字符串): button普通、submit提交、reset重置 | IE默认button; 其他浏览器（包括W3C规范）默认submit
#         class=样式类名(字符串): 导入样式表中的类用于设置样式; 如需为一个元素规定多个类，用空格分隔类名;
#             navbar-toggle collapsed窗口宽度不足时折叠包含某些元素的容器，在触发按钮时出现下拉菜单，
#             从上到下显示被折叠元素，本控件在窗口宽度不足时的初始状态是出现; btn基础按钮样式; btn-primary未被操作的原始按钮样式
#         data-toggle=触发类型(字符串): collapse触发时显示被折叠元素
#         data-target=被折叠元素容器(字符串): #容器的id;
#         aria-expanded=初始控件是否展开(字符串)
#         aria-controls=被折叠元素容器(字符串): 容器的id>
#     按钮标签</button>
# 显示一个按钮
# 表单内的按钮单击时的默认行为是提交表单

# 模板标签：
# {% csrf_token %}
# 防止攻击者利用表单来获取对服务器未经授权的访问（跨站请求伪造）

# 在显示所有主题网页添加到提交数据网页的超链接
# 修改  应用程序目录(learning_logs)\templates\应用程序名(learning_logs)\topics.html

# 19.1.2 添加新条目
# 在应用程序目录(learning_logs)\forms.py，添加类EntryForm

# 在 应用程序目录(learning_logs)\urls.py添加URL new_entry/topic_id/
# 在 应用程序目录(learning_logs)\views.py添加视图函数new_entry()
# 两个作用：准备添加条目网页和提交数据后跳转到显示所有条目网页

# 在 应用程序目录(learning_logs)\templates\应用程序名(learning_logs)创建新模板new_entry.html

# 修改 应用程序目录(learning_logs)\templates\应用程序名(learning_logs)\topic.html
# 添加段落超链接到添加条目网页

# 19.1.3 编辑条目
# 在 应用程序目录(learning_logs)\urls.py添加URL edit_entry/entry_id/
# 在 应用程序目录(learning_logs)\views.py添加视图函数edit_entry()
# 两个作用：准备编辑条目网页和提交数据后跳转到显示所有条目网页

# 在 应用程序目录(learning_logs)\templates\应用程序名(learning_logs)创建新模板edit_entry.html
# 与new_entry.html相似

# 19.1.4 编辑主题、删除主题、删除条目
# 使用之前的知识添加编辑主题、删除主题、删除条目的功能
