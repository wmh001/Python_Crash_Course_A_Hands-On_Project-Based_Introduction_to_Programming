# 19.2 创建用户账户
# 建立用户注册和身份验证系统，让用户注册和登录账户
# 创建新应用程序，包含处理用户账户的功能
# 修改Topic，让每个主题归属于特定用户

# 19.2.1 应用程序users
# 激活环境后，在项目目录执行命令startapp，添加应用程序users
# 在 项目名(learning_log)\settings.py列表INSTALLED_APPS中添加应用程序users
# 在 项目名(learning_log)\urls.py列表urlpatterns中users账户的URL
# 在 应用程序目录(users)\urls.py列表urlpatterns中登录账户的URL
# 在 应用程序目录(users)\templates\应用程序名(users)创建新模板login.html

# html文件中，
# input标签表示收集用户输入信息的控件
#     <input type=控件类型(字符串): text单行文本框; password密码文本框;
#             radio单选框; checkbox复选框; button、submit按钮; reset重置
#             file文件上传; number数字框; range音量条; hidden隐形
#         name=控件的名称(字符串)
#         value=默认收集的信息也即该区域默认的显示文字(字符串)/>
# 显示收集用户输入信息的控件
# 表单内的输入控件在表单提交时将收集的信息作为用户请求

# 模板标签：
# {% if 布尔表达式 %}
#     语句体
# {% endif %}
# 布尔表达式为真时，执行语句体，执行完毕后结束语句块

# 修改父模板 learning_logs\templates\learning_logs\base.html
# 显示用户名或登录链接

# 在html文件中，请求的属性可以不通过实例.，直接访问

# 模板标签
# {% if 布尔表达式 %}
#     语句体1
# {% else %}
#     语句体2
# {% endif %}
# 布尔表达式为真时，执行语句体1；否则执行语句体2；执行完毕后结束语句块

# 19.2.3 注销
# 在 应用程序目录(users)\urls.py列表urlpatterns中添加注销账户的URL
# 在 应用程序目录(users)\views.py定义视图函数logout_view()
# 注销视图函数重新定向到主页

# 修改父模板 learning_logs\templates\learning_logs\base.html
# 已登录后显示注销链接

# 19.2.4 注册页面
# 在 应用程序目录(users)\urls.py列表urlpatterns中添加注册账户的URL
# 在 应用程序目录(users)\views.py定义视图函数register()，创建Django提供的表单UserCreationFrom
# 在 应用程序目录(users)\templates\应用程序名(users)创建新模板register.html
# 修改父模板 learning_logs\templates\learning_logs\base.html链接到注册页面
