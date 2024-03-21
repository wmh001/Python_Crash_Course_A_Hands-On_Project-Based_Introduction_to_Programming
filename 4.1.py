# 4.1 遍历整个列表
# 对列表的每个元素执行相同的操作

# for循环语句
# for 循环变量 in 可迭代对象:
#     循环体
# 每轮循环中，循环变量从头到尾依次取可迭代对象的一个元素，每次取值后执行循环体，然后取下一个值，
#     直到循环变量取到可迭代对象的最后一个元素并执行完该次循环体，结束该语句块
# 循环体中不访问循环变量时，可以用_代替循环变量
# 可以在循环结束后访问循环变量，此时该变量的值为可迭代对象最后一个元素
mangicians = ["alice", "david", "carolina"]
for mangician in mangicians:
    print(mangician)
print(mangician)

# 4.1.1 深入地研究循环
# 循环让计算机自动完成重复工作地常见方式之一
# 循环变量的命名应有意义，如可迭代对象命名为复数，循环变量命名为对应单数

# 4.1.2 在for循环中执行更多的操作
for mangician in mangicians:
    print(mangician.title() + ", that was a great trick!")

for mangician in mangicians:
    print(mangician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + mangician.title() + ".\n")

# 4.1.3 在for循环结束后执行一些操作
# 循环结束后缩进结束
# 没有缩进的代码脱离当前循环
print("Thank you, everyone. That was a great magic show!")
