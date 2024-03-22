# 8.5 传递任意数量的实参
# *形参名
# 创建一个同名空元组，然后将传递的所有参数都封装到该元组中


def make_pizza_1(*toppings):
    """打印顾客点的所有配料"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza_1("pepperoni")
make_pizza_1("mushrooms", "green peppers", "extra cheese")

# 8.5.1 结合使用位置实参和任意数量实参
# 任意数量实参通常置于普通参数最后，Python先匹配位置实参和关键字实参，余下对应区域的的相邻若干个实参匹配任意数量实参
# 如果某参数在任意数量实参后，该参数只能使用关键字实参


def make_pizza(size, *toppings):
    """概述要制作的披萨"""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green peppers", "extra cheese")

# 8.5.2 使用任意数量的关键字实参
# **形参名
# 创建一个同名空字典，然后将传递的所有键值对都封装到该字典中
# 调用时键值对的格式为“键=值”


def build_profile(first, last, **user_info):
    """概述用户信息"""
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile(
    "albert", "einstein", location="princeton", field="physics"
)
print(user_profile)

# 由于位置实参、关键字实参、默认值、任意数量实参和任意数量关键字实参可以混用，因此实际参数列表具有极大的灵活性
# 传递实参时应当避免传递错误，先匹配位置实参，再匹配关键字实参，
#     余下的占据连续区域的键值对匹配任意数量关键字实参，剩下的占据连续区域的值匹配任意数量实参
