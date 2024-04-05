from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

# 在这里创建视图


def logout_view(request):
    """注销账户"""
    # django.contrib.auth.logout(
    #     request=用户请求<django.http.request.HttpRequest类>,
    #     其他参数: 均有默认值)
    # 注销发出请求的账户，即删除请求的user属性中记录的用户
    logout(request)
    return HttpResponseRedirect(reverse("learning_logs:index"))


def register(request):
    """注册新账户"""
    if request.method != "POST":
        # 未提交信息时，创建新表单
        # django.contrib.auth.forms.UserCreationForm(
        #     *args,
        #     **kwargs: 接收数个关键字实参，均有默认值:
        #         data=传递给表单的数据<字符串>,
        #         其他参数)
        # 返回新创建的注册用户表单实例，包含用户名、密码、确认密码的输入框以及输入要求
        form = UserCreationForm()
    else:
        # 提交信息后，对数据进行处理，并返回主页
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # 登录账户
            # django.contrib.auth.authenticate(
            #     request=用户请求<django.http.request.HttpRequest类> | None,
            #     **credentials: 接收数个关键字实参，均有默认值:
            #         username=用户名<django.db.models.CharField类>,
            #         password=密码<字符串>)
            # 认证给出的用户名和密码，在存在给出的用户名和密码对应的用户时返回对应的认证成功的用户实例；不存在该用户时返回None
            authenticated_user = authenticate(
                username=new_user.username, password=request.POST["password1"]
            )
            # django.contrib.auth.login(
            #     request=请求<django.http.request.HttpRequest类> | 无默认值,
            #     user=用户<django.contrib.auth.models.User类> | 无默认值,
            #     backend | None)
            # 用户登录，为用户创建有效的会话，即在登录到注销间的所有请求的user属性中记录该用户
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse("learning_logs:index"))

    context = {"form": form}
    return render(request, "users/register.html", context)
