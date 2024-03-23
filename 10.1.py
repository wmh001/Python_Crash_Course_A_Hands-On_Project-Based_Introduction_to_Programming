# 10.1 从文件中读取数据

# 10.1.1 读取整个文件
# open(
#     file=文件路径<字符串>,
#     mode=读取模式<字符串>:
#         r只读，文件不存在时报错，文件打开后初始游标置于开头，进行文件写入报错;
#         w只写，文件不存在时创建该文件，文件已存在时先清空该文件，文件打开后初始游标置于开头，进行文件读取时先清空文件再报错;
#         a追加，文件不存在时创建该文件，文件已存在时不清空文件，文件打开后初始游标置于原文件结尾，进行文件读取时报错;
#         r+读写模式之一，文件不存在时报错，文件已存在时不清空文件，文件打开后初始游标置于开头，
#             进行文件写入时从游标开始逐字覆盖原字符，原字符完全覆盖后以增加字符的方式继续写入，进行文件读取不报错;
#         w+读写模式之一，文件不存在时创建该文件，文件已存在时先清空该文件，文件打开后初始游标置于开头，进行文件读取不报错;
#         a+读写模式之一，文件不存在时创建该文件，文件已存在时不清空文件，文件打开后初始游标置于原文件结尾，进行文件读取不报错;
#         x创建文件并写入，必须操作不存在的文件，文件已存在时报错，进行文件读取时报错，Python 3新增;
#         b二进制形式读写文件，用于处理非文本文件和Python 3中的byte字符串; t以文本方式打开文件;b、t可以与其他字符拼接使用
#         | "r",
#     buffering=缓冲策略<整型数> | -1: 默认缓冲策略,
#     ecoding=编码方式<字符串> | None: 平台默认编码,
#     其他参数，均有默认值)
# 返回按读取模式打开的文件路径对应的文件实例
# with 表达式 as 变量名:
#     语句体
# 先执行表达式的值的的__enter__函数，再将返回值赋给变量，然后执行语句，执行语句后执行执行表达式的值的的__exit__函数
# 若表达式的值为文件实例，__enter__函数的返回值为文件实例本身，__exit__函数可以关闭并删除文件实例
# 使用with语句打开文件可以防止文件未关闭
with open("pi_digits10_1.txt") as file_object:
    # 文件实例.read(
    #     一次最多可读取的字符数<整型数>: 仅限位置实参; 未给定或为负则读取所有内容 | None: 一次性读取所有内容)
    # 返回从文件实例读取的指定字符数的字符串
    contents = file_object.read()
    print(contents)

# 删除末尾空行
with open("pi_digits10_1.txt") as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# 10.1.2 文件路径
# 文件路径：指定文件位置的字符串

# 相对文件路径：相对于当前工作目录（在编辑器内开发程序时，当前工作目录未必是运行程序所在目录）的文件路径
# Windows中的格式：目标文件在当前工作目录下时："目标文件名"、
# 目标文件在当前工作目录的数级子目录下时："当前工作目录的目录名\前一目录的子目录名\···\前一目录的子目录名\目标文件名"
# Linux和OS X中的格式：目标文件在当前工作目录下时："目标文件名"、
# 目标文件在当前工作目录的若干级子目录下时："当前工作目录的目录名/前一目录的子目录名/···/前一目录的子目录名/目标文件名"

# 绝对文件路径：从根目录开始的文件路径
# Windows中的格式："盘符:\前一目录的子目录名\···\前一目录的子目录名\目标文件名"
# Linux和OS X中的格式："/home/前一目录的子目录名/···/前一目录的子目录名/目标文件名"

# 文件路径中，每个目录下有两个特殊子目录：
# ".\"（Windows）和"./"（Linux和OS X）表示目录本身
# "..\"（Windows）和"../"（Linux和OS X）表示当前目录的父目录

# 在Windows中，使用正斜杠"/"有时也能正确解读，但最好使用反斜杠"\"
# 另外，反斜杠"\"在Python字符串中还有转义符的功能，因此最好在字符串前加r，表示不转义的原始字符串

# 10.1.3 逐行读取
# 文件实例为可迭代对象，其每个元素为文件对应行的字符串
filename = "pi_digits10_1.txt"

with open(filename) as file_object:
    for line in file_object:
        print(line)

# 去除多余换行符
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# 10.1.4 创建一个包含文件各行内容的列表
# 将文件内容存储在列表中可以在with语句结束后继续访问文件内容
filename = "pi_digits10_1.txt"

with open(filename) as file_object:
    # 文件实例.readlines(
    #     控制读取行数的参数<整型数>: 仅限位置实参; 未给定或为负则读取所有内容 | -1: 一次性读取所有内容)
    # 返回记录文件实例内容的列表，列表的元素为文件实例对应行的字符串
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# 10.1.5 使用文件的内容
filename = "pi_digits10_1.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

# 打印时删除每行左侧的空格
filename = "pi_digits10_1.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# 10.1.6 包含一百万位的大型文件
filename = "pi_million_digits10_1.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + "...")
print(len(pi_string))

# 10.1.7 圆周率值中包含你的生日吗
filename = "pi_million_digits10_1.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi!")
