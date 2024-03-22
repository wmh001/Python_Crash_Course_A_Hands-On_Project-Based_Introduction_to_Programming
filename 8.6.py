# 8.6 将函数存储在模块中

# 8.6.1 导入整个模块
# import 模块名
# 导入模块
import pizza8_6

# 模块名.函数名(参数列表)
# 调用已导入的模块中的函数
print("1")
pizza8_6.make_pizza(16, "pepperoni")
pizza8_6.make_pizza(12, "mushrooms", "green peppers", "extra cheese")

# 8.6.2 导入特定的函数
# from 模块名 import 函数名
# 导入模块中的特定函数
from pizza8_6 import make_pizza

print("2")
make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green peppers", "extra cheese")

# 8.6.3 使用as给函数指定别名
# 用于避免名称冲突或简化调用

# from 模块名 import 函数名 as 别名
# 给模块中的函数指定别名
from pizza8_6 import make_pizza as mp

print("3")
# 函数别名(参数列表)
mp(16, "pepperoni")
mp(12, "mushrooms", "green peppers", "extra cheese")

# 8.6.4 使用as给模块指定别名
# import 模块名 as 别名
import pizza8_6 as p

print("4")
# 模块别名.函数名(参数列表)
# 调用模块中的函数
p.make_pizza(16, "pepperoni")
p.make_pizza(12, "mushrooms", "green peppers", "extra cheese")

# 8.6.5 导入模块中的所有函数
# from 模块名 import *
# 导入模块中的除以单下划线和双下划线开头的函数外的所有函数
from pizza8_6 import *

print("5")
make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green peppers", "extra cheese")

# 注意，使用并非自己编写的大型模块时，导入所有函数可能导致名称冲突进而覆盖冲突函数
