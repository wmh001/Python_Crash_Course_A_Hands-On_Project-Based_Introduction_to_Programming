# 18.2 创建应用程序
# 在项目中暂时创建一个应用程序，用于完成大部分工作

# 创建应用程序所需的基础设施
# 激活环境后，在项目目录执行 python manage.py startapp 应用程序名(learning_logs)
# 在项目目录新增与应用程序同名目录
# 其中重要的文件有：
# models.py：定义在应用程序中管理数据的模型，通常为django.db.models.Model的子类
#     django.db.models.Model类定义了模型基本功能
# admin.py：处理管理网站，注册模型
# views.py：创建视图，编写视图函数

# 18.2.1 定义模型
# 用户可以在学习笔记中创建多个主题，输入与特定主题关联的条目，每个条目有时间戳
# 可在模型中使用的各种字段可在网址https://docs.djangoproject.com/en/1.8/ref/models/fields 参阅
# 在models.py中定义存储主题的模型Topic类，为django.db.models.Model（模型）子类

# 18.2.2 激活模型
# 让应用程序包含到项目中
# 项目名(learning_log)\settings.py文件定义的列表INSTALLED_APPS保存所有安装的应用程序
# 在列表INSTALLED_APPS中添加应用程序learning_logs

# 创建迁移文件
# 在激活环境后，在项目目录执行 python manage.py makemigrations 应用程序名(learning_logs)
# 系统创建迁移文件 应用程序名(learning_logs)\migrations\0001_initial.py，该文件在数据库中为模型Topic创建一个表

# 应用迁移，修改数据库
# 在激活环境后，在项目目录执行 python manage.py migrate
# 再次执行命令migrate时，输出与首次基本相同，仅增加了添加应用程序及是否成功

# 总结：管理数据流程：
# 执行startapp命令，在项目目录创建应用程序所需的基础设施
# 应用程序目录\models.py中定义管理数据的新模型
# 项目名\settings.py文件定义的列表INSTALLED_APPS中添加应用程序名
# 执行makemigrations命令，在项目目录创建迁移文件
# 执行migrate命令，应用迁移

# 18.2.3 Django管理网站
# 建立管理网站（admin site）方便处理模型，仅有网站管理员可以使用管理网站

# 创建超级用户
# 在激活环境后，在项目目录执行 python manage.py createsuperuser
# 设定超级用户名（ll_admin），输入邮箱（可选），设定密码（两次）

# 超级用户具备所有权限，可以访问网站的几乎所有信息，可能对其隐藏有些敏感信息，
#     如用户密码转换散列值，无法依据散列值反推原始密码
# 注册了的用户通常可阅读自己的私有数据和会员信息
# 游客用户权限最严格，只允许阅读公开信息

# 向管理网站注册模型
# 在 应用程序目录(learming_logs)\admin.py导入自己创建的模型，并注册

# 管理网站会自动创建一些模型，如User和Group
# 自己创建的模型必须手工注册

# 访问网址 http://localhost:8000/admin/ ，输入用户名和密码，进入管理网站
# 在管理网站能够添加和修改用户和用户组、管理已注册的模型

# 添加主题
# 单击Topic，进入主题网页
# 单击Add，出现用于添加新主题的表单
# 在Text方框输入主题名，再单击Save，自动返回主题管理页面，其中包含刚创建的主题

# 添加主题Chess（国际象棋）、Rock Climbing（攀岩）

# 18.2.4 定义模型Entry
# 定义可以添加并与主题关联的条目Entry模型

# 18.2.5 迁移模型Entry
# 步骤已总结

# 18.2.6 向管理网站注册Entry
# 在 应用程序目录(learming_logs)\admin.py导入自己创建的模型，并注册

# 访问网址 http://localhost:8000/admin/ ，输入用户名和密码，进入管理网站

# 添加条目
# 单击Entry，进入条目网页
# 单击Add，出现用于添加新条目的表单
# 在Topic下拉列表选择条目所属的主题
# Text方框输入条目，再单击Save，自动返回条目管理页面，其中包含刚创建的条目

# 添加两个主题国际象棋的条目、一个主题攀岩的条目

# 18.2.7 Django shell
# 交互式环境Django shell可以通过交互式终端会话以编程方式查看数据，用于确认代码是否可以访问数据、测试项目和排除故障
# 在激活环境后，在项目目录执行 python manage.py shell，启动一个Python解释器
# 修改模型后，需要重启shell才能在shell查看修改结果
# 退出shell：通用：exit()
#     Windows：Ctrl+Z
#     Linux/OS X：Ctrl+D

# 用于查询的属性和函数：

# print(django.db.models.Model子类实例)
# 打印模型实例的字符串表示

# django.db.models.Model实例常用属性：
# id<整型数>：实例的id
# objects<django.db.models.manager.Manager.BaseManager类>：模型管理器属性，由django自动生成，是进行Model和数据库查询的接口

# django.db.models.Model子类.objects.all()
# 返回一个列表，称为查询集（queryset），查询集的元素为该模型的所有模型实例

# django.db.models.Model子类.objects.get(
#     *args,
#     **kwargs: 接收数个关键字实参:
#         id=待获取实例的id<整型数>)
# 返回某模型的指定id的实例

# django.db.models.Model实例1.[django.db.models.Model子类2小写名称]_set.all()
# 返回关联本模型实例1的模型2实例的集合

# 步骤：
# 导入自定义模型
# 调用方法

# 示例：
# 执行from learning_logs.models import Topic，导入自定义模型Topic
# 使用方法 Topic.objects.all()
# 执行 topics = Topic.objects.all()，遍历topics，打印模型实例的id和字符串表示
# 执行 t = Topic.objects.get(id=1)，访问 t.text和 t.date_added
# 执行 t.entry_set.all()，返回与t关联的条目实例的集合
