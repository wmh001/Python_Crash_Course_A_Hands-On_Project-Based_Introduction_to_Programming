from django.shortcuts import render

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
