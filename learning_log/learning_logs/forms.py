# 导入表单模块
from django import forms

# 导入模型
from .models import Entry, Topic


class TopicForm(forms.ModelForm):
    # 内嵌类，用于指定根据哪个模型创建表单
    class Meta:
        model = Topic
        # 该表单包含字段text
        # 输入给该字段对应表单元素的数据会赋值给所属模型实例的、名字与该字段相同的属性
        fields = ["text"]
        # 不为字段生成标签
        labels = {"text": ""}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ["text"]
        labels = {"text": ""}
        # django.forms.Textarea(
        #     attrs=小部件样式<字典>: 常用键值对："cols":宽度<整型数>: 默认40列)
        # 返回新创建的输入小部件
        # 创建输入小部件
        widgets = {"text": forms.Textarea(attrs={"cols": 80})}
