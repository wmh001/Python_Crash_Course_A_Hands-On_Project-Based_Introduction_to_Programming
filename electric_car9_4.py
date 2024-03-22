"""一组可用于表示电动汽车的类"""

from car9_4_2 import Car


class Battery:
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


class ElectricCar(Car):
    """模拟电动车"""

    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        self.battery = Battery()
