# 12.4 添加飞船图像
# 可以从网站http://pixabay.com 等获取无需许可的图形
# 游戏可以使用多种类型的图像文件，其中最简单的是Pygame默认加载的位图（.bmp）格式
# 配置Pygame以使用其他文件格式有时需要安装相应的图像库
# 为保证图像融入窗口背景，选择图像时尽可能选择背景透明的图像或将游戏背景颜色设置为与图像背景颜色相同

# 12.4.1 创建Ship类
import sys

import pygame
from settings12_3 import Settings
from ship12_4 import Ship


def run_game():
    """运行游戏"""
    # 初始化游戏并创建一个窗口
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")
    # 创建飞船
    ship = Ship(screen)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 每次循环时重绘画布
        screen.fill(ai_settings.bg_color)
        # 每次循环时重绘飞船
        ship.blitme()

        # 让最近的绘制的Surface实例显示
        pygame.display.flip()


run_game()
