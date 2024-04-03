"""定义learning_logs的URL模式"""

from django.conf.urls import url

# .表示文件所在文件夹
from . import views

urlpatterns = [
    # 主页
    # 开头结尾间没有东西的URL，与基础URL匹配
    url(r"^$", views.index, name="index"),
    # 显示全部主题的网页
    url(r"^topics/$", views.topics, name="topics"),
    # 显示特定主题全部条目的网页
    url(r"^topics/(?P<topic_id>\d+)/$", views.topic, name="topic"),
]
