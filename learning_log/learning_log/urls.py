"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.contrib import admin

# 包含项目中的应用程序的URL模式（所有URL忽略基础URL http://localhost:8000/）
urlpatterns = [
    # django.conf.urls(
    #     regex=用于匹配URL的正则表达式字符串<字符串>: 脱字符^表示匹配字符串的开头; 美元符号$表示匹配字符串的结尾;
    #         /(?P<变量名>\d+)/表示匹配/和/间的一组数字字符串，并将字符串转换为数字然后赋值给变量，再传入视图函数处理;
    #         ()表示捕获URL中的值; ?P<变量名>表示将匹配的字符串切取、处理并赋值给变量; \d表示数字; +表示可以不止一位 | 无默认值,
    #     view=视图函数<函数> | 无默认值,
    #     kwargs=视图函数除URL提供的参数和用户请求外的参数名及其实参<字典>: 其中的键值对会按照随机顺序传入视图函数中;
    #         键为参数名的字符串，值为实参; 常用键值对："templeta_name":模板路径<字符串> |,
    #     name=别名<字符串>: 对本条URL取别名 |)
    # 返回新创建的URL和视图函数之间的映射关系，当用户访问某个URL时，Django将请求和其他参数发送给对应的视图函数来处理
    # django.contrib.admin.site.urls()
    # 返回管理网站的可以请求的所有视图函数
    # 以admin/开头的URL，即管理位置的URL
    url(r"^admin/", admin.site.urls),
    # django.conf.urls.include(
    #     arg=URLconf模块（urls.py）名称<字符串>: 如"应用程序文件夹.urls" | 无默认值,
    #     namespace=包含的URL条目的命名空间<字符串>: 用于与同项目中的其他URL区分开 |,
    #     其他参数: 均有默认值)
    # 剔除掉前面匹配到的部分后，将剩下的部分交给本函数中的另一个URLconf模块（urls.py）处理
    # users的URL
    url(r"^users/", include("users.urls", namespace="users")),
    # 空字符URL，即learning_logs的URL
    url(r"", include("learning_logs.urls", namespace="learning_logs")),
]
