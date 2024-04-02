# 18.1 建立项目

# 18.1.1 制定规范
# 规范详细说明了项目的目标，阐述了项目的功能，并讨论了项目的外观和用户界面
# 应突出重点

# 本项目的规范：
# 编写一个名为“学习笔记”的Web应用程序，让用户能够记录感兴趣的主题，并在学习每个主题的过程中添加条目
# “学习笔记”的主页对这个网站进行描述，并邀请用户注册或登录
# 用户登录后，就可创建新主题、添加新条目以及阅读既有的条目

# 18.1.2 建立虚拟环境
# 虚拟环境与其他Python包隔离
# 在项目目录创建虚拟环境：python -m venv 虚拟环境名(ll_env)

# 18.1.3 安装virtualenv
# 较早的Python或系统设置不正确会导致模块venv不能使用，可安装virtualenv包代替：
# pip install virtualenv
# 在项目目录创建虚拟环境：指定python版本：virtualenv -p 指定版本python安装路径 虚拟环境创建路径(ll_env)
#     使用默认python版本：virtualenv 虚拟环境创建路径(ll_env)

# 18.1.4 激活虚拟环境
# Linux和OS X：在项目目录执行 source 虚拟环境名(ll_env)/bin/activate
# Windows：在项目目录执行 虚拟环境名(ll_env)\Scripts\activate

# 退出虚拟环境
# 在项目目录执行 deactivate

# 18.1.5 安装Django
# 激活环境后，pip install Django=1.11

# 18.1.6 在Django中创建项目
# 激活环境后，在项目目录执行 django-admin.py startproject 项目名(learning_log) .
# 注意必须有.

# manage.py  管理创建好了的项目
# 项目名\settings.py  总的设置文件，定义常量，指定Django如何与系统交互以及如何管理项目
# 项目名\urls.py  路由配置文件，告诉Django应响应哪些浏览器请求和如何响应请求
# 项目名\wsgi.py  Django实现的WSGI接口的文件，用来处理web请求，帮助Django提供它创建的文件

# 18.1.7 创建数据库
# 创建一个供Django使用的数据库
# 激活环境后，在项目目录执行 python manage.py migrate
# db.sqlite3为创建的数据库文件

# 修改数据库称为迁移数据库
# 执行命令migrate时，Django确保数据库与项目的当前状态匹配，如无数据库先创建数据库
# 命令的响应指出Django将创建必要的数据库表，用于存储将在本项目（同步未迁移的应用程序）中使用的信息，
#     再确保数据库结构与当前代码（应用所有的迁移）匹配
# SQLite是一种使用单个文件的数据库，简单易用

# 18.1.8 查看项目
# Django启动一个服务器用于查看当前项目生成的网页
# 激活环境后，在项目目录执行 python manage.py runserver或python manage.py runserver 端口号
# 系统先检查是否正确创建项目
# 再指出Django版本及使用的设置文件的名称
# 最后指出项目的URL，默认在本机（127.0.0.1，localhost）的端口8000上侦听请求
# 在浏览器访问该网站，该网站只处理本机发出的请求
# 启动服务器失败可能是因为默认端口8000已被占用，请更换端口
# Ctrl+C关闭服务器
