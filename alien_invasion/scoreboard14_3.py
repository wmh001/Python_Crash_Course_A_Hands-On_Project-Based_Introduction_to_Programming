"""管理得分"""

import pygame.font
from pygame.sprite import Group
from ship14_3 import Ship


class Scoreboard:
    """显示得分信息的类"""

    def __init__(self, ai_settings, screen, stats):
        """初始化显示得分涉及的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # 显示得分信息时使用的字体设置
        self.text_color = (30, 30, 30)  # 深灰色
        self.font = pygame.font.SysFont(None, 48)

        # 准备初始化得分图像
        self.prep_score()
        # 准备初始化最高得分图像
        self.prep_high_score()
        # 准备初始化等级图像
        self.prep_level()
        # 准备初始化剩余飞船图像
        self.prep_ships()

    def prep_score(self):
        """将得分转换为一幅渲染的图像"""
        # round(
        #     number=原数<整型数/浮点数> | 无默认值,
        #     ndigits=保留小数点后的位数<整型数> | 无默认值)
        # 返回对原数在指定数位四舍五入的数字
        # 四舍五入规则：
        # 要求保留位数的后一位<=4，则进位
        # 要求保留位数的后一位=5，且该位数后面没有数字，则不进位
        # 要求保留位数的后一位=5，且该位数后面有数字，则进位
        # 要求保留位数的后一位>=6，则进位
        # 保留小数点后的位数<0，在小数点左侧数位进行四舍五入
        # 在Python 3中，转换结果为整数时类型转换为整型数
        # 在Python 2.7中，转换结果为整数时类型仍为浮点数
        rounded_score = round(self.stats.score, -1)
        # 字符串实例.format(
        #     *args: 接收数个填充量<> | 无默认值,
        #     其他可选参数)
        # python字符串的格式化，用填充量转换为字符串后替换字符串中的{}标记的内容，{}内可以有内容指定转换为字符串的方式
        # {:,}表示将用于填充的数字格式化为千分位分割格式，如100,000,000
        score_str = "{:,}".format(rounded_score)
        # score_str = str(self.stats.score)
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.ai_settings.bg_color
        )

        # 将得分放在画布右上角附近
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """将最高得分转换为渲染的图像"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color, self.ai_settings.bg_color
        )

        # 将得分放在画布右上角附近
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """将等级转换为渲染的图像"""
        self.level_image = self.font.render(
            str(self.stats.level), True, self.text_color, self.ai_settings.bg_color
        )
        # 将等级放在得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """显示还余下多少艘飞船"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """在画布上显示得分"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # 绘制飞船
        self.ships.draw(self.screen)
