# 7.1 函数input()的工作原理

# input(
#     提示或说明<字符串>: 仅限位置实参 | "")
# 在终端打印提示或说明，然后让程序暂停，等待用户输入，用户回车后程序继续运行，返回用户输入的字符串实例
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# 7.1.1 编写清晰的程序
# 提示指定清晰明白，准确指出希望用户提供的信息
name = input("Please enter your name: ")
print("Hello, " + name + "!")

# 提示超过一行
prompt = "If you tell us who are, we can personalize the messages you see."
# ?后的 有利于清晰
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")

# 7.1.2 使用int()来获取数值输入
# 用户输入的数据类型为字符串
age = input("How old are you? ")
print(type(age))

# int(
#     待转换格式数字<字符串/浮点数>: 仅限位置实参; 接收字符串时按文字意思转换为整型数; 接收浮点数时取小数点前部分 | 无默认值)
# 返回其他类型转换来的整型数实例
# 不能直接将字符串类型的小数转换为整型数实例。若想实现，应先将字符串转换为浮点数，再转换为整型数
age = input("How old are you? ")
age = int(age)
print(type(age))

height = input("How tall are you, in inches? ")
height = int(height)
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

# 7.1.3 求模运算符
# 被除数<整型数/浮点数> % 除数<整型数/浮点数>
# 返回两数相除后的余数
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")

# 7.1.4 在Python 2.7中获取输入
# Python 2.7中，raw_input()函数与Python 3中的input()相同
# Python 2.7中，input()函数将用户输入解读为Python代码，并尝试运行它们，打印运行结果
