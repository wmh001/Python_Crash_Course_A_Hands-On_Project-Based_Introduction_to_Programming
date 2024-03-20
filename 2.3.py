# 2.3 字符串
# 字符串（str）是由一系列按一定顺序排列的不可修改元素组成的集合
# Python中，字符串用''或""标记，元素间无分隔符，元素为单个字符

# 字符串实例[索引<整型数>: 索引从0开始]
# 返回字符串实例中对应索引的元素
name = "add lovelace"
print(name[2])

# 2.3.1 使用方法修改字符串的大小写
# 字符串实例.title()
# 返回各单词首字母大写的字符串实例，原字符串实例不变
name = "add lovelace"
print(name.title())
print(name)

# 字符串实例.upper()
# 返回各字母全部大写的字符串实例，原字符串实例不变
name = "Add Lovelace"
print(name.upper())
print(name)
# 字符串实例.lower()
# 返回各字母全部小写的字符串实例，原字符串实例不变
print(name.lower())
print(name)

# 2.3.2 合并（拼接）字符串
# 字符串实例1<字符串> + 字符串实例2<字符串>
# 返回拼接后的字符串实例
first_name = "add"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

# 名字首字母大写
print("Hello, " + full_name.title() + "!")

# 2.3.3使用制表符或换行符来添加空白
# 编程中，空白泛指任何非打印字符，如空格、制表符和换行符等
# 转义字符\t：制表符
print("\tPython")
# 转义字符\n：换行符
print("Language:\n\tPython\n\tC\n\tJavaScript")

# 2.3.4 删除空白
favorite_language = "python "
print("'" + favorite_language + "'")
# 字符串实例.rstrip(
#     待移除的末尾字符<字符串>: 不接收关键字实参 | None: 空白（空格、制表符和换行符等）)
# 返回删除末尾所有指定字符直到末尾不为该字符的字符串实例，原字符串实例不变
print("'" + favorite_language.rstrip() + "'")
print("'" + favorite_language + "'")
# 永久删除字符串中的空白需要改变变量的值
favorite_language = favorite_language.rstrip()
print("'" + favorite_language + "'")

favorite_language = " python "
print("'" + favorite_language.rstrip() + "'")
# 删除开头空白
# 字符串实例.lstrip(
#     待移除的开头字符<字符串>: 不接收关键字实参 | None: 空白（空格、制表符和换行符等）)
# 返回删除开头所有指定字符直到开头不为该字符的字符串实例，原字符串实例不变
print("'" + favorite_language.lstrip() + "'")
# 字符串实例.strip(
#     待移除的两端字符<字符串>: 不接收关键字实参 | None: 空白（空格、制表符和换行符等）)
# 返回删除两端所有指定字符直到两端不为该字符的字符串实例，原字符串实例不变
print("'" + favorite_language.strip() + "'")

# 2.3.5 使用字符串时避免语法错误
# ''标记的字符串可包含""
# ""标记的字符串可包含'和''
message = "One of Python's strengths is its diverse community."
print(message)

# 2.3.6 Python2中的print语句
# print 被打印的内容
# Python2中的print为关键字而非函数
