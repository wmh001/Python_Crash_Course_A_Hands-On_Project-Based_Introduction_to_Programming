# 9.2 使用类和实例

# 9.2.1 Car类


class Car_1:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()


my_new_car = Car_1("audi", "a4", 2016)
print(my_new_car.get_descriptive_name())

# 9.2.2 给属性指定默认值
# 给属性提供默认值后，定义类时的__init__()函数的形参列表和创建实例的实参列表就不包含给该属性赋值的参数了
# 具有默认值的属性可以不在__init__()函数定义内初始化而在所有方法定义外类定义内初始化，此时访问属性无self.，只需属性名


class Car_2:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        """打印汽车里程"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")


my_new_car = Car_2("audi", "a4", 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# 9.2.3 修改属性的值
# 方法一：直接修改属性的值
# 实例.属性 = 值<>


class Car_3:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        """打印汽车里程"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")


my_new_car = Car_3("audi", "a4", 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# 方法二：通过方法修改属性的值
# 定义修改属性的方法


class Car_4:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        """打印汽车里程"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """修改里程表读数，并防止里程表读数回调"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


my_new_car = Car_4("audi", "a4", 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.update_odometer(23)
my_new_car.read_odometer()
my_new_car.update_odometer(18)
my_new_car.read_odometer()

# 方法三：通过方法对属性的值进行递增
# 定义对属性进行递增的方法


class Car_5:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        """打印汽车里程"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """修改里程表读数，并防止里程表读数回调"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的值"""
        self.odometer_reading += miles


my_new_car = Car_5("subaru", "outback", 2013)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.update_odometer(23500)
my_new_car.read_odometer()
my_new_car.increment_odometer(100)
my_new_car.read_odometer()
