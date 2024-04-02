from django.contrib import admin

# 在这里注册你的模型
from learning_logs.models import Entry, Topic

# django.contrib.admin.site.register(
#     model_or_iterable=待注册的模型<类> |,
#     其他参数: 均有默认值)
# 在管理网站注册给定的模型
admin.site.register(Topic)
admin.site.register(Entry)
