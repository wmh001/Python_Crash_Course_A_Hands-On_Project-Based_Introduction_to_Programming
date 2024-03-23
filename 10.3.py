# 10.3 异常
# 异常是Python用来管理程序执行期间发生的错误的特殊对象
# 每当发生让Python不知所措的错误时，它会创建一个异常对象
# 如果编写了处理该异常的代码，程序将继续运行
# 如果未对异常进行处理，程序将停止，并显示一个traceback，其中包含有关异常的报告
# 处理异常的代码：try-except语句

# 10.3.1 处理ZeroDivisionError异常
# 零除异常
# print(5/0)

# 10.3.2 使用try-except代码块
# try:
#     正常代码
# except 异常类型1:
#     处理该异常的代码
# ···
# except 异常类型i:
#     处理该异常的代码
# ···
# except 异常类型n:
#     处理该异常的代码
# 先执行正常代码
# 如果未发生异常，执行结束后结束该程序块
# 如果发生了指定类型的异常，正常代码执行到发生异常的语句之前，然后执行处理该异常的代码，执行结束后结束该程序块
# 如果发生了未指定类型的异常，正常代码执行到发生异常的语句之前，程序将停止，并显示一个traceback，其中包含有关异常的报告
try:
    print("Hello!")
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# 10.3.3 使用异常避免崩溃
print("Give me two numbers, and I'll divide thme.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == "q":
        break
    second_number = input("Second number: ")
    if second_number == "q":
        break
    answer = int(first_number) / int(second_number)
    print(answer)

# 10.3.4 else代码块
# try:
#     正常代码
# except 异常类型:
#     处理该异常的代码
# else:
#     未发生异常时的代码
# 先执行正常代码
# 如果未发生异常，执行结束后执行else后的未发生异常时的代码，然后结束该程序块
# 如果发生了指定类型的异常，正常代码执行到发生异常的语句之前，然后执行处理该异常的代码，执行结束后结束该程序块
# 如果发生了未指定类型的异常，正常代码执行到发生异常的语句之前，程序将停止，并显示一个traceback，其中包含有关异常的报告
print("Give me two numbers, and I'll divide thme.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == "q":
        break
    second_number = input("Second number: ")
    if second_number == "q":
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)

# 10.3.5 处理FileNotFoundError异常
# 文件异常（文件找不到）
filename = "alice10_3_2.txt"

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)

# 10.3.6 分析文本
title = "Alice in Wonderland\t爱丽丝梦游仙境\nLewis Carroll"
# 字符串实例.split(
#     sep=分隔符<字符串> | None: 空白（空格、制表符和换行符等）,
#     maxsplit=最大分隔次数<整型数> | -1: 能分隔多少次就分隔多少次
#     )
# 返回一个元素为按照指定的分隔符进行分割后原字符串实例的片段的列表实例，列表实例元素顺序与在原字符串实例中的顺序相同
# 分割后的字符串不包含分隔符
print(title.split())

# 统计文章单词数
filename = "alice10_3_1.txt"
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")

# 10.3.7 使用多个文件


def count_words_1(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")


filename = "alice10_3_1.txt"
count_words_1(filename)

filenames = [
    "alice10_3_1.txt",
    "siddhartha10_3.txt",
    "moby_dick10_3.txt",
    "little_women10_3.txt",
]
for filename in filenames:
    count_words_1(filename)

# 10.3.8 失败时一声不吭


def count_words_2(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        # pass
        # 占位语句，程序执行时不发生任何操作
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")


filenames = [
    "alice10_3_1.txt",
    "siddhartha10_3.txt",
    "moby_dick10_3.txt",
    "little_women10_3.txt",
]
for filename in filenames:
    count_words_2(filename)

# 10.3.9 决定报告哪些错误
# 根据用户需求决定是否报告错误
# 在程序正常运行依赖外部因素，如用户输入、读取文件、网络链接等，时，容易出现异常
