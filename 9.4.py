# 9.4 导入类
# 导入类的与导入函数类似
# 模块中定义的以单下划线和双下划线开头的类为私有类，建议仅能在模块内部调用

# 9.4.1 导入单个类
# from 模块名 import 类名
# 导入模块中的一个类
from car9_4_1 import Car

my_new_car = Car("audi", "a4", 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# 9.4.3 在一个模块中导入多个类
# from 模块名 import 类名1, 类名2, ···
# 导入模块中的多个类
from car9_4_1 import Car, ElectricCar

my_new_car = Car("audi", "a4", 2016)
print(my_new_car.get_descriptive_name())
my_tesla = ElectricCar("tesla", "model s", 2016)
print(my_tesla.get_descriptive_name())

# 9.4.4 导入整个模块
# import 模块名
# 导入整个模块
import car9_4_1

# 模块名.类名(参数列表)
# 创建已导入的模块中定义的类的实例
my_beetle = car9_4_1.Car("volkswagen", "beetle", 2016)
print(my_beetle.get_descriptive_name())

my_tesla = car9_4_1.ElectricCar("tesla", "roadster", 2016)
print(my_tesla.get_descriptive_name())

# 9.4.5 导入模块中的所有类
# from 模块名 import *
# 导入模块中的除以单下划线和双下划线开头的类外的所有类
# 使用这种方式可能导致名称冲突

# 9.4.6 在一个模块中导入另一个模块
from car9_4_2 import Car
from electric_car9_4 import ElectricCar

my_beetle = Car("volkswagen", "beetle", 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar("tesla", "roadster", 2016)
print(my_tesla.get_descriptive_name())

# 9.4.7 自定义工作流程
# 让代码更为组织有序
