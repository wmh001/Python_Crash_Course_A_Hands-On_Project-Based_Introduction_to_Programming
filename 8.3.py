# 8.3 返回值
# 函数处理过一些数据

# 8.3.1 返回简单值


def get_formatted_name_1(first_name, last_name):
    """返回全名"""
    full_name = first_name + " " + last_name
    return full_name.title()


musician = get_formatted_name_1("jimi", "hendrix")
print(musician)

# 8.3.2 让实参变成可选的
# 可选值能增加函数灵活性，确保函数调用简单
# 常用的方法是设定默认值、使用任意数量的实参、使用任意数量的关键字实参


def get_formatted_name_2(first_name, last_name, middle_name=""):
    """返回全名，并在提供或没有提供中间名时依然可行"""
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()


musician = get_formatted_name_2("jimi", "hendrix")
print(musician)

musician = get_formatted_name_2("john", "hooker", "lee")
print(musician)

# 8.3.3 返回字典


def build_person_1(first_name, last_name):
    """返回一个包含一个人有关信息的字典"""
    person = {"first": first_name, "last": last_name}
    return person


musician = build_person_1("jimi", "hendrix")
print(musician)

# 扩展该函数


def build_person_2(first_name, last_name, age=None):
    """返回一个包含一个人有关信息的字典"""
    person = {"first": first_name, "last": last_name}
    if age:
        person["age"] = age
    return person


musician = build_person_2("jimi", "hendrix")
print(musician)
musician = build_person_2("jimi", "hendrix", age=27)
print(musician)

# 8.3.4 结合使用函数和while循环


def get_formatted_name_3(first_name, last_name):
    """返回全名"""
    full_name = first_name + " " + last_name
    return full_name.title()


while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == "q":
        break
    l_name = input("Last name: ")
    if l_name == "q":
        break
    formatted_name = get_formatted_name_3(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
