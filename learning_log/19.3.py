# 19.3 让用户拥有自己的数据
# 确定数据所属的用户
# 修改模型Topic

# 19.3.1 使用@login_required限制访问
# 装饰器是放在函数定义前面的指令@装饰器或@装饰器(参数列表)
# 装饰器本质上是一个函数，它接受另一个函数或类作为参数，并返回一个新的函数或类
# 通常用于在不修改原始代码的情况下添加额外的功能、修改函数的行为

# django.contrib.auth.decorators中定义了许多可作为装饰器的函数：
# login_required()
# 只允许已登录用户访问被装饰函数，用户未登录将被重新定向到 项目名(learning_log)\setting.py设定的LOGIN_URL对应的网页

# 使用@login_required限制对views.topics的访问
# 修改settings.py指明登录网页URL

# 使用@login_required限制对views.py除主页、注册网页、注销网页外所有视图的访问

# 19.3.2 将数据关联到用户
# 只需要将最高层数据主题关联到用户
# 修改 learning_logs\models.py的Topic定义，添加一个关联到用户的外键

# 利用Django shell查询已有项目
# django.contrib.auth.models.objects.all()
# 返回已创建的用户的集合

# 执行makemigrations命令创建迁移数据库文件
# Django对于模型的没有默认值的新添加属性提供两种处理方法：
# 在终端提供默认值；退出并在模型文件中添加默认值
# 选择第一种

# 输入用户id 1，将所有既有主题关联到超级用户

# 执行migrate命令，迁移数据库，激活模型

# python manage.py flush
# 用于重置数据库，丢弃所有既有数据和已创建超级账户

# 19.3.3 只允许用户访问自己的主题
# 修改 learning_logs\views.py的topics()定义

# 19.3.4 保护用户的主题
# 限制对单个主题的访问
# 修改 learning_logs\views.py的topic()定义

# 19.3.5 保护页面edit_entry
# 修改 learning_logs\views.py的edit_entry()定义

# 19.3.6 将新主题关联到当前用户
# 修改 learning_logs\views.py的new_topic()定义
# 保存用户

# 19.3.7
# 保护new_entry、edit_topic、delete_topic、delete_topic_yes、delete_entry、delete_entry_yes网页
