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
    # 用户添加新主题的网页
    url(r"^new_topic/$", views.new_topic, name="new_topic"),
    # 用户添加新条目的网页
    url(r"^new_entry/(?P<topic_id>\d+)/$", views.new_entry, name="new_entry"),
    # 用户编辑主题的网页
    url(r"^edit_topic/(?P<topic_id>\d+)/$", views.edit_topic, name="edit_topic"),
    # 用户编辑条目的网页
    url(r"^edit_entry/(?P<entry_id>\d+)/$", views.edit_entry, name="edit_entry"),
    # 用户删除主题的网页
    url(r"^delete_topic/(?P<topic_id>\d+)/$", views.delete_topic, name="delete_topic"),
    # 用户确认删除主题的网页
    url(
        r"^delete_topic_yes/(?P<topic_id>\d+)/$",
        views.delete_topic_yes,
        name="delete_topic_yes",
    ),
    # 用户删除条目的网页
    url(r"^delete_entry/(?P<entry_id>\d+)/$", views.delete_entry, name="delete_entry"),
    # 用户确认删除条目的网页
    url(
        r"^delete_entry_yes/(?P<entry_id>\d+)/$",
        views.delete_entry_yes,
        name="delete_entry_yes",
    ),
]
