# 9.3 继承
# 一个类继承另一个类时，它将自动获得另一个类的所有属性和方法，同时可以定义自己的属性和方法，对父类的方法进行重写
# 原有的类称为父类（超类），新类称为子类

# 9.3.1 子类的方法__init__()


class Car_1:
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


# class 子类名(父类名):
#     ···
#     def 方法i(参数列表):
#         方法i函数体
#     ···
# 继承父类（超类）定义子类
class ElectricCar_1(Car_1):
    """模拟电动车"""

    def __init__(self, make, model, year):
        """初始化父类的属性"""
        # super(子类名<>, self)
        # 返回子类实例假设中对应的父类的实例
        # 子类名<>, self可省略
        # 调用父类的__init__()函数，初始化子类继承自父类的属性
        super().__init__(make, model, year)


my_tesla = ElectricCar_1("tesla", "model s", 2016)
print(my_tesla.get_descriptive_name())

# 9.3.2 Python 2.7中的继承
# 父类定义行与Python 2.7普通类相同
# 子类定义行与Python 3普通子类相同
# super(子类名<>, self)
# Python 2.7中，返回父类实例，子类名<>, self不可省略

# 9.3.3 给子类定义属性和方法


class ElectricCar_2(Car_1):
    """模拟电动车"""

    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """打印电瓶容量"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


my_tesla = ElectricCar_2("tesla", "model s", 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

# 9.3.4 重写父类的方法
# 子类的同名方法将覆盖父类的方法


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

    def update_odometer(self, mileage):
        """修改里程表读数，并防止里程表读数回调"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的值"""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """填满油箱"""
        print("The gas tank is already full!")


class ElectricCar_3(Car_2):
    """模拟电动车"""

    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """打印电瓶容量"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def fill_gas_tank(self):
        """电动车没有油箱"""
        print("This car doesn't need a gas tank!")


my_tesla = ElectricCar_3("tesla", "model s", 2016)
print(my_tesla.get_descriptive_name())
my_tesla.fill_gas_tank()

my_new_car = Car_2("audi", "a4", 2016)
print(my_new_car.get_descriptive_name())
my_new_car.fill_gas_tank()

# 9.3.5 将实例用作属性
# 将小类作为大类的属性类型


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

    def update_odometer(self, mileage):
        """修改里程表读数，并防止里程表读数回调"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的值"""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """填满油箱"""
        print("The gas tank is already full!")


class Battery_1:
    """模拟电瓶"""

    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印电瓶容量"""
        print("This car has a " + str(self.battery_size) + "-kWh battery")


class ElectricCar_4(Car_3):
    """模拟电动车"""

    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        self.battery = Battery_1()


my_tesla = ElectricCar_4("tesla", "model s", 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

# 显示电瓶续航里程


class Battery_2:
    """模拟电瓶"""

    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印电瓶容量"""
        print("This car has a " + str(self.battery_size) + "-kWh battery")

    def get_range(self):
        """指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " mile on a full charge."
        print(message)


class ElectricCar_5(Car_3):
    """模拟电动车"""

    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        self.battery = Battery_2()


my_tesla = ElectricCar_5("tesla", "model s", 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
