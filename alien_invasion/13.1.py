# 13.1 回顾项目

# 下一步计划
# 重构旧代码
# 添加外星人，指定合适边框
# 创建一系列外星人，填满画布的上半部分
# 外星人向下移动，在这个过程中外星人可以被子弹击落
# 外星人撞到飞船或到达底边时销毁飞船并再创建一群外星人
# 飞船击落所有的外星人后再创建一群外星人
# 玩家可用的飞船耗尽后，游戏结束

# 添加快捷键Q结束游戏
import game_functions13_1 as gf
import pygame
from pygame.sprite import Group
from settings12_8 import Settings
from ship12_6 import Ship


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
    ship = Ship(ai_settings, screen)
    # 创建子弹编组
    bullets = Group()

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)

        # 更新飞船
        ship.update()

        # 更新子弹
        gf.update_bullets(bullets)

        # 更新画布
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
