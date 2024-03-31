"""射击子弹"""

import pygame
from pygame.sprite import Sprite


# pygame.sprite.Sprite（精灵）子类可将游戏中相关的元素编组（加入可迭代类pygame.sprite.Group（编组）类），进而统一操作编组中的所有元素
class Bullet(Sprite):
    """一个对飞船发射的子弹进行管理的类"""

    def __init__(self, ai_settings, screen, ship):
        """在飞船所处的位置创建一个子弹对象"""
        # pygame.sprite.Sprite实例.__init__()
        # 初始化精灵
        super().__init__()
        self.screen = screen

        # 在(0, 0)处创建一个表示子弹的矩形，再设置正确的位置
        # pygame.Rect(
        #     left=左边横坐标<浮点数> | 无默认值,
        #     top=顶边纵坐标<浮点数> | 无默认值,
        #     width=宽<浮点数> | 无默认值,
        #     height=高<浮点数> | 无默认值)
        # 返回新创建的Rect实例
        self.rect = pygame.Rect(
            0, 0, ai_settings.bullet_width, ai_settings.bullet_height
        )
        # 将子弹的横坐标中点设置在飞船的横坐标中点
        self.rect.centerx = ship.rect.centerx
        # 将子弹的顶边纵坐标设置在飞船的顶边纵坐标
        self.rect.top = ship.rect.top

        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)
        # 设定子弹颜色
        self.color = ai_settings.bullet_color
        # 设定子弹速度
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        # 更新小数子弹位置
        self.y -= self.speed_factor
        # 更新子弹位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在画布上绘制子弹"""
        # pygame.draw.rect(
        #     surface=待绘制矩形的窗口<pygame.Surface类> | 无默认值,
        #     color=颜色<三元组> | 无默认值,
        #     rect=绘制位置<pygame.Rect类> | 无默认值,
        #     width=边框宽度<整型数> | 0,
        #     其他可选参数)
        # 在画布上指定位置绘制指定颜色的矩形
        pygame.draw.rect(self.screen, self.color, self.rect)
