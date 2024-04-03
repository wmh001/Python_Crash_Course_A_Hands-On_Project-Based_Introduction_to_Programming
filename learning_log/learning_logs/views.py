from django.shortcuts import render

from .models import Topic

# 在这里创建视图


def index(request):
    """学习笔记的主页"""
    # django.shortcuts.render(
    #     request=原始请求<> | 无默认值,
    #     template_name=要渲染的模板名称<字符串/列表>: 模板名称为自定义html文件或其路径，
    #         可以选择绝对路径或相对路径，相对路径起点为应用程序目录\templates\;
    #         接收列表实参时，列表的元素为模板名称，Django将按照给定列表的顺序查找模板文件 | 无默认值,
    #     context=要传递给模板的数据<字典>: 字典键值对为"模板中的变量名"<字符串>:传递给模板变量的数据<> | None: 不传递数据,
    #     其他参数: 均有默认值)
    # 根据请求，将数据渲染的到指定的模板中，生成并返回接收请求后的响应（html内容）
    return render(request, "learning_logs/index.html")


def topics(request):
    """显示所有主题"""
    # django.db.models.Model子类.objects.order_by(
    #     *field_names: 接收子类属性字段，以字符串表示; 依据该字段进行排序)
    # 返回模型的所有实例依模型的某个属性排序后的集合
    topics = Topic.objects.order_by("date_added")
    context = {"topics": topics}
    return render(request, "learning_logs/topics.html", context)


def topic(request, topic_id):
    """显示特定主题全部条目"""
    topic = Topic.objects.get(id=topic_id)
    # django.db.models.Model实例1.[django.db.models.Model子类2小写名称]_set.order_by(
    #     用于排序的属性字段<字符串>: 以字符串表示; 字符串以-开头表示按降序排列)
    # 返回关联本模型实例1的所有模型2实例依模型2实例的某个属性排序后的集合
    # 获取所有条目依时间并由近到远排序
    entries = topic.entry_set.order_by("-date_added")
    context = {"topic": topic, "entries": entries}
    return render(request, "learning_logs/topic.html", context)
