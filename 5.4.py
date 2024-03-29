# 5.4 使用if语句处理列表

# 5.4.1 检查特殊元素
requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")
print("\nFinishing making your pizza!")

for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")
print("\nFinishing making your pizza!")

# 5.4.2 确定列表不是空的
# 空列表、空元组、空字典、空字符串、整型数0、浮点数0.0、关键字None在自动类型转换为布尔值时转化为False，否则转化为True
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinishing making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

# 5.4.3 使用多个列表
available_toppings = [
    "mushrooms",
    "olives",
    "green peppers",
    "pepperoni",
    "pineapple",
    "extra cheese",
]
requested_toppings = ["mushrooms", "french fries", "extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinishing making your pizza!")
