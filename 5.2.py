# 5.2 条件测试
# 值为布尔值的表达式称为条件测试或布尔表达式
# 布尔值仅包括True和False
# True表示真，False表示假

# 5.2.1 检查是否相等
# 表达式1 == 表达式2
# 返回表示表达式1的值与表达式2的值是否相等的布尔值
# 表达式的值的类型应当相同或进行自动类型转换后可以相同，如整型数向浮点数
car = "bmw"
print(car == "bmw")
car = "audi"
print(car == "bmw")

# 5.2.2 检查是否相等时不考虑大小写
car = "Audi"
# 一般的条件测试考虑大小写
print(car == "audi")
# 忽略大小写
print(car.lower() == "audi")
# 不影响原变量
print(car)

# 5.2.3 检查是否不相等
# 表达式1 ！= 表达式2
# 返回表示表达式1的值与表达式2的值是否不相等的布尔值
# 表达式的值的类型应当相同或进行自动类型转换后可以相同，如整型数向浮点数
requested_tooping = "mushroom"
if requested_tooping != "anchovies":
    print("Hold the anchovies")

# 5.2.4 比较数字
age = 18
print(age == 18)

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

age = 19
# 表达式1 < 表达式2
# 返回表示表达式1的值是否小于表达式2的值的布尔值
# 表达式的值的类型应当相同或进行自动类型转换后可以相同，如整型数向浮点数
print(age < 21)
# 表达式1 <= 表达式2
# 返回表示表达式1的值是否小于等于表达式2的值的布尔值
# 表达式的值的类型应当相同或进行自动类型转换后可以相同，如整型数向浮点数
print(age <= 21)
# 表达式1 > 表达式2
# 返回表示表达式1的值是否大于表达式2的值的布尔值
# 表达式的值的类型应当相同或进行自动类型转换后可以相同，如整型数向浮点数
print(age > 21)
# 表达式1 >= 表达式2
# 返回表示表达式1的值是否大于等于表达式2的值的布尔值
# 表达式的值的类型应当相同或进行自动类型转换后可以相同，如整型数向浮点数
print(age >= 21)

# 5.2.5 检查多个条件
# 布尔表达式1 and 布尔表达式2
# 当两个条件都为True时，返回True，否则返回False
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

age_1 = 22
print(age_0 >= 21 and age_1 >= 21)

# 为了改善可读性可将每个条件测试放在()内
print((age_0 >= 21) and (age_1 >= 21))

# 布尔表达式1 or 布尔表达式2
# 当两个条件都为False时，返回False，否则返回True
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)

age_0 = 18
print(age_0 >= 21 or age_1 >= 21)

# 5.2.6 检查特定值是否包含在列表中
# 元素 in 集合<列表/元组/字符串>
# 返回表示元素是否在集合中的布尔值
requested_toopings = ["mushrooms", "onions", "pineapple"]
print("mushrooms" in requested_toopings)
print("pepperoni" in requested_toopings)

# 5.2.7 检查特定值是否不包含在列表中
banned_users = ["andrew", "carolina", "david"]
user = "marie"
# 元素 not in 集合<列表/元组/字符串>
# 返回表示元素是否不在集合中的布尔值
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

# 5.2.8 布尔表达式
# 值为True或False的表达式
