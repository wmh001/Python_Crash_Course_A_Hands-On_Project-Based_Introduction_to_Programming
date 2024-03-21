# 7.2 while循环简介

# 7.2.1 使用while循环
# while 布尔表达式:
#     循环体
# 布尔表达式为True则运行循环体，直到布尔表达式为Flase时结束程序块
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# 7.2.2 让用户选择何时退出
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != "quit":
    message = input(prompt)
    if message != "quit":
        print(message)

# 7.2.3 使用标志
active = True
while active:
    message = input(prompt)

    if message == "quit":
        active = False
    else:
        print(message)

# 7.2.4 使用break退出循环
# break用于控制程序流程，执行后结束循环状态
# 可用于控制while循环和for循环
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'puit' when you are finished.) "
while True:
    city = input(prompt)

    if city == "quit":
        break
    else:
        print("I'd love to go to " + city.title() + "!")

# 7.2.5 在循环中使用continue
# continue用于控制程序流程，执行后结束本轮循环，进入下一轮循环条件判断
# 可用于控制while循环和for循环
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# 避免无限循环
# 保证循环至少有一条结束循环的路径
x = 1
while x <= 5:
    print(x)
    # 缺少下一句将陷入死循环
    x += 1
# 陷入死循环后，按Ctrl+C或关闭程序输出终端可脱离
