# 5.3 if语句

# 5.3.1 简单的if语句
# if 布尔表达式:
#     语句体
# 布尔表达式为True，则执行语句体，然后结束该程序块；布尔表达式为False，则不执行语句体，直接结束该程序块
age = 19
if age >= 18:
    print("You are old enough to vote!")

# 所有缩进行的代码都属于同一程序块
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")


# 5.3.2 if-else语句
# if 布尔表达式:
#     语句体1
# else:
#     语句体2
# 布尔表达式为True，则执行语句体1，然后结束该程序块；布尔表达式为False，则则执行语句体2，然后结束该程序块
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please regiater to vote as you as turn 18!")

# 5.3.3 if-elif-else结构
# if 布尔表达式1:
#     语句体1
# elif 布尔表达式2:
#     语句体2
# else:
#     语句体3
# 布尔表达式1为True，则执行语句体1，然后结束该程序块；否则计算布尔表达式2，若为True，
#     则执行语句体2，然后结束该程序块；否则执行语句体3，然后结束该程序块
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

# 5.3.4 使用多个elif代码块
# if 布尔表达式1:
#     语句体1
# elif 布尔表达式2:
#     语句体2
# elif 布尔表达式3:
#     语句体3
# ···
# elif 布尔表达式n-1:
#     语句体n-1
# else:
#     语句体n
# 依次计算每个布尔表达式，直到遇到了值为True的布尔表达式时，执行其后语句体，然后结束该程序块；
#     所有布尔表达式都为False时，执行else后语句体n，然后结束该程序块
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print("Your admission cost is $" + str(price) + ".")

# 5.3.5 省略else代码块
# if 布尔表达式1:
#     语句体1
# elif 布尔表达式2:
#     语句体2
# elif 布尔表达式3:
#     语句体3
# ···
# elif 布尔表达式n:
#     语句体n
# 依次计算每个布尔表达式，直到遇到了值为True的布尔表达式时，执行其后语句体，然后结束该程序块；
#     所有布尔表达式都为False时，直接结束该程序块
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print("Your admission cost is $" + str(price) + ".")

# 5.3.6 测试多个条件
requested_toppings = ["mushrooms", "extra cheese"]
if "mushrooms" in requested_toppings:
    print("Adding mushrooms.")
if "pepperoni" in requested_toppings:
    print("Adding pepperoni.")
if "extra cheese" in requested_toppings:
    print("Adding extra cheese.")
print("\nFinishing making your pizza!")
