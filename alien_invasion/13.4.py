# 13.4 让外星人群移动
# 外星人群在屏幕上向右移动，撞到画布边缘后向下移动，再沿反方向移动

# 13.4.1 向右移动外星人
# 添加外星人速度设置
# 重写外星人update()方法
# 添加update_aliens函数

# 13.4.2 创建表示外星人移动方向的设置
# 添加移动方向设置和下降速度设置

# 13.4.3 检测外星人是否撞到了屏幕边缘
# 编写外星人新方法，并修改update()

# 13.4.4 向下移动外星人群并改变移动方向
# 添加新函数check_fleet_edges()、change_fleet_direction()，修改update_aliens()
import game_functions13_4 as gf
import pygame
from pygame.sprite import Group
from settings13_4 import Settings
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
        # 更新外星人
        gf.update_aliens(ai_settings, aliens)

        # 更新画布
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
