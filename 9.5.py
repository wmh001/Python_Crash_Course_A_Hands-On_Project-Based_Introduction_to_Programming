# 9.5 Python标准库
# Python标准库是安装Python时包含的一组模块
# Python标准库中包含模块collections
# 该模块包含类OrderedDict
# 该类为记录键值对添加顺序的字典。兼具列表和字典的主要优点
from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages["jen"] = "python"
favorite_languages["sar"] = "c"
favorite_languages["edward"] = "ruby"
favorite_languages["phil"] = "python"

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
