from django.db import models

# 在这里创建模型


class Topic(models.Model):
    """用户学习的主题"""

    # django.db.models.CharField(
    #     verbose_name=<str> | None,
    #     name=<str> | None,
    #     primary_key=<bool> |,
    #     max_length=在数据库中预留多少空间<整型数>: 单位为字符 | None,
    #     其他参数: 均有默认值)
    # 返回依参数新创建的由字符或文本组成的数据CharField实例
    # 用于模拟存储少量文本的数据，如名称、标题或城市
    text = models.CharField(max_length=200)
    # django.db.models.DateTimeField(
    #     verbose_name=<str> | None,
    #     name=<str> | None,
    #     auto_now=<bool> |,
    #     auto_now_add=是否在创建实例时自动设置为当前日期和时间 | True,
    #     其他参数: 均有默认值)
    # 返回依参数新创建的记录日期和时间的数据DateTimeField实例
    date_added = models.DateTimeField(auto_now_add=True)

    # django.db.models.Model.__str__()
    # 指定在网页上有关模型默认显示为哪些数据即模型实例的字符串表示
    # Python 2.7中用__unicode__()代替
    def __str__(self):
        """返回模型的字符串表示"""
        return self.text


class Entry(models.Model):
    """学到的有关每个主题的具体知识"""

    # django.db.models.ForeignKey(
    #     to=关联的目标模型<字符串/类>: 字符串实参指明模型的路径 | 无默认值,
    #     on_delete=当关联实例被删除时的处理办法<函数>: django.db.models模块定义了多个函数，
    #         CASCADE级联删除，删除关联对象时同时删除本对象、
    #         PROTECT保护，删除关联对象时引发错误ProtectedError，防止删除关联对象、
    #         SET_NULL删除关联对象时属性设置为空（前提是blank=True、null=True即创建该属性时允许为空）、
    #         SET_DEFAULT删除关联对象时设置为默认值（前提是传递了默认值default实参）、
    #         SET(值/表达式)删除关联对象时设定为自定义值、
    #         DO_NOTHING除删除关联对象外什么也不做 | 无默认值)
    # 返回依参数新创建的本模型与目标模型间的外键（关联关系）ForeignKey实例
    # 外键是数据库术语，用于引用数据库中的另一条记录
    # 每个主题Topic实例创建时，给它分配一个键或ID
    # 将每个条目Entry实例关联到主题Topic实例时，使用主题Topic实例的键
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    # django.db.models.TextField()
    # 返回依参数新创建的由不限制长度的大量文本组成的数据TextField实例
    text = models.TextField()
    # 记录日期和时间的数据DateTimeField实例用于顺序显示条目和显示时间戳
    date_added = models.DateTimeField(auto_now_add=True)

    # 嵌套类的定义发生在外部类的定义内，可以像普通类一样定义属性和方法，并且可以被实例化和使用
    # 外部类.嵌套类(嵌套类__init__()实参列表)
    # 返回新创建的嵌套类实例
    # 通过传递外部类的实例作为嵌套属性的初始化参数或通过其他方式将外部类的属性传递给嵌套类，可以在嵌套类中访问外部类的属性
    # 嵌套类Mate用于管理模型的额外信息
    class Mate:
        # 设置特殊属性，用于在需要时Django使用Entries表示多个条目
        # 如果不定义这个类，Django使用Entrys来表示多个条目
        verbose_name_plural = "entries"

    def __str__(self):
        """返回模型的字符串表示"""
        # 网页上显示文本的前50个字符
        return self.text[:50] + "..."
