"""为应用程序users定义URL模式"""

from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    # 登录页面
    # django.contrib.auth.views.login(
    #     request=用户请求<django.http.request.HttpRequest类> | 无默认值,
    #     template_name=模板路径<字符串> | "registration/login.html",
    #     其他参数: 均有默认值)
    # Django默认登录账户视图函数
    url(r"^login/$", login, {"template_name": "users/login.html"}, name="login"),
    # 注销账户
    url(r"^logout/$", views.logout_view, name="logout"),
    # 注册账户
    url(r"^register/$", views.register, name="register"),
]
