"""管理骰子的类"""

from random import randint


class Die:
    """表示一个骰子的类"""

    def __init__(self, num_sides=6):
        """初始化6面骰子"""
        self.num_sides = num_sides

    def roll(self):
        """返回一个位于1和骰子面数间的随机值"""
        # random.randint(
        #     a=下限<整型数>,
        #     b=上限<整型数>)
        # 返回一个指定范围（包含上下限）内的整数
        return randint(1, self.num_sides)
