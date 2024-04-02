"""定义learning_logs的URL模式"""

from django.conf.urls import url

# .表示文件所在文件夹
from . import views

urlpatterns = [
    # 主页
    # 开头结尾间没有东西的URL，与基础URL匹配
    url(r"^$", views.index, name="index"),
]
