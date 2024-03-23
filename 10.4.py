# 10.4 存储数据
# 使用模块json来存储数据到JSON格式文件中
# JSON格式文件应用广泛

# 10.4.1 使用json.dump()和json.load()
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = "numbers10_4.json"

# 存储数据
with open(filename, "w") as f_obj:
    # json.dump(
    #     obj=要存储的数据<> | 无默认值,
    #     fp=JSON格式存储文件实例<文件类> | 无默认值,
    #     其他参数: 仅限关键字实参，均有默认值)
    # 将数据写入一个JSON格式文件实例中，数据以文本形式存储在文件实例中，文本与该数据的常量形式的代码文本相同，
    #     即对于集合类型的数据，类型标记如[]、""等和元素分隔符如，等也被记录
    json.dump(numbers, f_obj)

# 读取数据
with open(filename) as f_obj:
    # json.load(
    #     fp=JSON格式存储文件实例<文件类> | 无默认值,
    #     其他参数: 仅限关键字实参，均有默认值)
    # 返回JSON格式文件实例中存储的数据，将读取的文本视为代码文本，以确定常量数据类型的规则确定该数据的数据类型，如依[]、""等确定
    numbers = json.load(f_obj)

print(numbers)

# 10.4.2 保存和读取用户生成的数据
username = input("What is your name? ")
filename = "username10_4_1.json"

# 保存用户数据
with open(filename, "w") as f_obj:
    json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username + "!")

# 读取用户数据
with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username + "!")

# 文件不存在，则保存用户输入；文件存在，则读取并打印用户数据
filename = "username10_4_2.json"
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, "w") as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")

# 10.4.3 重构
# 将代码划分为一系列完成具体工作的函数


def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = "username10_4_3.json"
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        # 函数返回None表示返回无意义的值
        return None
    else:
        return username


def get_new_username():
    """提示用户输入用户名"""
    username = input("What is your name? ")
    filename = "username10_4_3.json"
    with open(filename, "w") as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """问候用户"""
    username = get_stored_username()

    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")


greet_user()
