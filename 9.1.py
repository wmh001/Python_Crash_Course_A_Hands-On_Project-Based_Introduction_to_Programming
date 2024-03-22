# 9.1 创建和使用类
# 类模拟现实世界中的事物和情景
# 对象由类实例化而来

# 9.1.1 创建Dog类
# class 类名/类名():
#     def 方法1(参数列表1):
#         方法1函数体
#     ···
#     def 方法i(参数列表i)
#         方法i函数体
#     ···
#     def 方法n(参数列表n)
#         方法n函数体
# 定义类
# 通常类名首字母大写
# 类定义行后可以有"""···"""标记的被称为文档字符串的注释，它可以跨多行，作为描述类功能的文档
# 类中定义的成员函数称为方法；属于某类的实例的成员变量称为属性
# 以单下划线开头的属性/方法称为保护属性/方法，这些属性/方法不应该通过该类实例和该类子类实例直接访问，
#     而建议通过该类实例和该类子类实例的方法间接访问
# 以双下划线开头的属性/方法称为私有属性/方法，这些属性/方法无法通过该类实例直接访问，
#     也不能通过该类子类实例直接访问或该类子类实例的方法间接访问，而必须通过该类实例的方法间接访问或
#     该类实例._类名__属性/方法名的方法直接访问
# 以双下划线开头和结尾的方法为python预定义的特殊方法专用的标识，用于特殊用途，如__init__()代表类的构造函数
# 第一个方法可以是__init__方法，该方法在类创建时自动调用，可以完成对属性进行初始化等任务
# __init__()并未显式地包含return语句，但会自动返回一个该类地实例
# 定义类时，所有方法的第一个参数可以是self，表示实例本身，方法可以通过该参数访问属性和其他方法
# 调用方法时，参数列表不需要包含self
# 类名、属性名、方法名和参数名建议有实际意义


class Dog:
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def _sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")

    def sit(self):
        """模拟小狗被命令时蹲下"""
        self._sit()

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")


# 在Python 2.7中，类定义行应为
# class 类名(object):

# 9.1.2 根据类创建实例
# 类名(__init__方法除self参数列表)
# 返回新创建的该类的实例
# 通常实例名首字母小写
my_dog = Dog("willie", 6)
# 实例名.属性名
# 返回实例的属性
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
# 实例名.方法名(除self参数列表)
# 调用实例方法
my_dog.sit()
my_dog.roll_over()
# 创建更多实例
your_dog = Dog("lucy", 3)
print("My dog's name is " + your_dog.name.title() + ".")
print("My dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
your_dog.roll_over()
