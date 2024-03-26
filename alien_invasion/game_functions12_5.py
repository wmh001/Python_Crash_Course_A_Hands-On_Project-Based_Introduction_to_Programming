"""定义游戏调用的函数"""

import sys

import pygame


def check_events():
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen, ship):
    """更新画布上的图像，并更新画布"""
    # 每次循环时重绘画布
    screen.fill(ai_settings.bg_color)
    # 每次循环时重绘飞船
    ship.blitme()

    # 让最近的绘制的Surface实例显示
    pygame.display.flip()
