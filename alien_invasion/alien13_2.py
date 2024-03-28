"""管理外星人"""

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self, ai_settings, screen):
        """初始化外星人并设置其初始位置"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图像，并获取其外接矩形
        self.image = pygame.image.load(r"alien_invasion\images\alien.bmp")
        self.rect = self.image.get_rect()

        # 每个外星人最初设定在画布左上角附近，左边距为外星人宽度，右边距为外星人高度
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的小数位置
        self.x = float(self.rect.x)

    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)
