# 8.1 定义函数


# def 函数名(参数列表):
#     函数体
# 定义函数
# 函数体开头可以有"""···"""标记的被称为文档字符串的注释，它可以跨多行，作为描述程序的文档
# 函数结尾可以有 return 返回值 ，用于产生返回值即函数表达式的值
# 没有return语句等价于显式返回关键字None，两者都表示没有有意义的返回值
# 函数名和参数名建议有实际意义
def greet_user_1():
    print("Hello!")


# lambda 参数列表: 返回值表达式
# 定义匿名函数


# 函数名(实参列表)
# 调用函数
greet_user_1()

# 8.1.1 向函数传递信息
# 向函数传递参数


def greet_user_2(username):
    print("Hello, " + username.title() + "!")


greet_user_2("jesse")

# 8.1.2 实参和形参
# 定义函数时表示参数的变量称为形参
# 调用函数时传递的参数值称为实参
# 调用函数时，实参赋值给形参
