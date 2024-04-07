from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

# 在这里创建视图
# 导入表单
from .forms import EntryForm, TopicForm

# 导入模型
from .models import Entry, Topic


def index(request):
    """学习笔记的主页"""
    # django.shortcuts.render(
    #     request=原始请求<> | 无默认值,
    #     template_name=要渲染的模板名称<字符串/列表>: 模板名称为自定义html文件或其路径，
    #         可以选择绝对路径或相对路径，相对路径起点为应用程序目录\templates\;
    #         接收列表实参时，列表的元素为模板名称，Django将按照给定列表的顺序查找模板文件 | 无默认值,
    #     context=要传递给模板的数据<字典>: 字典键值对为 模板中的变量名<字符串>:传递给模板变量的数据<> | None: 不传递数据,
    #     其他参数: 均有默认值)
    # 根据请求，将数据渲染的到指定的模板中，生成并返回接收请求后的响应（网页）
    return render(request, "learning_logs/index.html")


@login_required
def topics(request):
    """显示所有主题"""
    # django.db.models.Model子类.objects.order_by(
    #     *field_names: 接收子类属性字段，以字符串表示; 依据该字段进行排序)
    # 返回模型的所有实例依模型的某个属性排序后的集合
    # topics = Topic.objects.order_by("date_added")
    # django.db.models.Model子类.objects.filter(
    #     *args,
    #     **kwargs: 接收数个关键字实参，作为筛选条件，条件的格式为模型属性=目标值)
    # 返回模型的所有实例中的符合条件的实例组成的集合，类型为django.db.models.manager.Manager.BaseManager（模型管理器）类
    topics = Topic.objects.filter(owner=request.user).order_by("date_added")
    context = {"topics": topics}
    return render(request, "learning_logs/topics.html", context)


@login_required
def topic(request, topic_id):
    """显示特定主题全部条目"""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        # raise Http404
        # 抛出404异常
        raise Http404
    # django.db.models.Model实例1.[django.db.models.Model子类2小写名称]_set.order_by(
    #     用于排序的属性字段<字符串>: 以属性名字符串表示; 字符串以-开头表示按降序排列)
    # 返回关联本模型实例1的所有模型2实例依模型2实例的某个属性排序后的集合
    # 获取所有条目依时间并由近到远排序
    entries = topic.entry_set.order_by("-date_added")
    context = {"topic": topic, "entries": entries}
    return render(request, "learning_logs/topic.html", context)


@login_required
def new_topic(request):
    """添加新主题"""
    # django.http.resquest.HttpRequest（请求）实例常用属性：
    # method<字符串>：标识请求所使用的HTTP方法，如GET获取、POST提交、PUT等
    # GET<django.http.QueryDict类（类似字典）>：包含GET请求中的所有参数及其实参，键和值都是字符串类型
    # POST<django.http.QueryDict类（类似字典）>：包含POST请求中提交的除文件外的表单数据参数及其实参，键和值都是字符串类型
    #     常用键值对："password1":注册网页中输入密码的框提交的数据、"password2":注册网页中确认输入密码的框提交的数据
    # FILES<django.http.QueryDict类（类似字典）>：包含所有的上传文件数据，
    #     每个键是html文件中上传文件的标签input的name属性，每个值是一个上传的文件数据
    # COOKIES<字典>：包含了一次请求的Cookie信息，键和值都是字符串
    # META<字典>：包含了所有的HTTP头部信息; 常用键值对：
    #     CONTENT_LENGTH:标识请求消息正文的长度: 对于POST请求这个请求头是必需的、
    #     CONTENT_TYPE:请求正文的MIME类型: 对应于post和hello请求，它的值可以是text和plain、
    #     HTTP_HOST:客户端发送的HTTP主机头、
    #     HTTP_USER_AGENT:浏览器的类型，通常被称为UA: 适用于视图准备的网页随浏览器的不同而不同的情况、
    #     REMOTE_ADDR:客户端的IP地址: 可以用于记录日志或根据IP确定地域再做处理、
    #     REMOTE_HOST:客户端的主机名、
    #     REQUEST_METHOD:请求方法: GET、POST等、
    #     SERVER_NAME:服务器的主机名、
    #     SERVER_PORT:服务器的端口号<字符串>: 如"8000"
    # user<django.contrib.auth.models.User（用户）类/django.contrib.auth.models.AnonymousUser（匿名用户）类>:标识当前登录用户: 在用
    #     户未登录时，被设置为匿名用户

    # django.contrib.auth.models.User（用户）实例常用属性：
    # username<django.db.models.CharField类>：用户名
    if request.method != "POST":
        # 未提交主题时，创建新表单
        # django.forms.ModelForm子类(
        #     data=填入表单的数据<字符串> | None: 表单各元素空白,
        #     files,
        #     auto_id,
        #     prefix,
        #     initial,
        #     error_class,
        #     label_suffix,
        #     empty_permitted,
        #     instance=创建表单时表单填入哪个模型实例的属性<django.db.models.Model子类> | None: 不填入数据,
        #     其他参数，均有默认值)
        # 返回新创建的表单实例
        form = TopicForm()
    else:
        # 提交主题后，对数据进行处理，并返回显示所有主题的网页
        form = TopicForm(request.POST)
        # django.forms.ModelForm子类实例.is_valid()
        # 检查用户是否填写表单的所有必填字段（默认所有字段必填），以及输入的数据符合要求
        if form.is_valid():
            # django.forms.ModelForm子类实例.save(
            #     commit=是否立即将数据存入数据库<布尔>: True立即存储到数据库内;
            #         False暂不存储到数据库内，之后手动随返回的模型实例一起保存，适用于模型实例需要修改后才存储的场景
            #         | True)
            # 返回新创建的存储填入表单的数据的表单所属模型的实例，并确定是否立即保存该实例到数据库
            # form.save()
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            # django.core.urlresolvers.reverse(
            #     viewname=URL别名<字符串>: "命名空间:URL别名" | None,
            #     urlconf,
            #     args=URL需要的参数列表<列表>: 在URL别名对应的URL尾加上 参数/; 列表元素为URL的参数 | None: 无参数,
            #     其他参数: 均有默认值)
            # 已知URL别名及URL参数，通过逆向解析获取URL，返回该URL的字符串
            # django.http.HttpResponseRedirect(
            #     redirect_to=URL<字符串>,
            #     其他参数: 均有默认值)
            # 将浏览器重新定向到URL对应的网页
            return HttpResponseRedirect(reverse("learning_logs:topics"))

    context = {"form": form}
    return render(request, "learning_logs/new_topic.html", context)


@login_required
def new_entry(request, topic_id):
    """在特定主题添加新条目"""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    if request.method != "POST":
        # 未提交条目时，创建新表单
        form = EntryForm()
    else:
        # 提交条目后，对数据进行处理，并返回显示所有条目的网页
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            # 使条目关联到主题
            new_entry.topic = topic
            # django.db.models.Model子类实例.save()
            # 将模型实例存储到数据库内
            new_entry.save()
            return HttpResponseRedirect(reverse("learning_logs:topic", args=[topic_id]))

    context = {"topic": topic, "form": form}
    return render(request, "learning_logs/new_entry.html", context)


@login_required
def edit_topic(request, topic_id):
    """编辑主题"""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    if request.method != "POST":
        # 未编辑主题时，创建表单，填入原条目
        form = TopicForm(instance=topic)
    else:
        # 编辑并提交主题后，对数据进行处理，并返回显示所有条目的网页
        # 根据既有主题创建表单，再根据请求修改条目
        form = TopicForm(instance=topic, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("learning_logs:topics"))

    context = {"topic": topic, "form": form}
    return render(request, "learning_logs/edit_topic.html", context)


@login_required
def edit_entry(request, entry_id):
    """编辑条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method != "POST":
        # 未编辑条目时，创建表单，填入原条目
        form = EntryForm(instance=entry)
    else:
        # 编辑并提交条目后，对数据进行处理，并返回显示所有条目的网页
        # 根据既有条目创建表单，在根据请求修改条目
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("learning_logs:topic", args=[topic.id]))

    context = {"entry": entry, "topic": topic, "form": form}
    return render(request, "learning_logs/edit_entry.html", context)


@login_required
def delete_topic(request, topic_id):
    """删除主题的网页"""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    context = {"topic": topic}
    return render(request, "learning_logs/delete_topic.html", context)


@login_required
def delete_topic_yes(request, topic_id):
    """确认删除主题"""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    # django.db.models.Model子类实例.delete()
    # 删除模型实例
    topic.delete()
    return HttpResponseRedirect(reverse("learning_logs:topics"))


@login_required
def delete_entry(request, entry_id):
    """删除条目的网页"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    context = {"entry": entry, "topic": topic}
    return render(request, "learning_logs/delete_entry.html", context)


@login_required
def delete_entry_yes(request, entry_id):
    """确认删除条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    entry.delete()
    return HttpResponseRedirect(reverse("learning_logs:topic", args=[topic.id]))
