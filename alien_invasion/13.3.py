# 13.3 创建一群外星人

# 13.3.1 确定一行可容纳多少个外星人

# 13.3.2 创建多行外星人
# 修改函数update_screen()

# 13.3.3 创建外星人群
# 添加函数create_fleet()

# 13.3.4 重构create_fleet()
# 计算可以容纳多少外星人和创建外星人整合进函数

# 13.3.5 添加行
# 计算上方画布可以容纳多少行
import game_functions13_3 as gf
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
    # 创建编组
    # 创建子弹编组
    bullets = Group()
    # 创建外星人编组
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)

        # 更新飞船
        ship.update()

        # 更新子弹
        gf.update_bullets(bullets)

        # 更新画布
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
