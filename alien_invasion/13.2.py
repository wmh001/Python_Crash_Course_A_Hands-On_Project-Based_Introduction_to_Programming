# 13.2 创建第一个外星人
# 创建类似Ship类的Alien类

# 13.2.1 创建Alien类
# 与Ship类似

# 13.2.2 创建Alien实例

# 13.2.3 让外星人出现在画布上
# 修改函数update_screen()
import game_functions13_2 as gf
import pygame
from alien13_2 import Alien
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
    # 创建外星人实例
    alien = Alien(ai_settings, screen)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)

        # 更新飞船
        ship.update()

        # 更新子弹
        gf.update_bullets(bullets)

        # 更新画布
        gf.update_screen(ai_settings, screen, ship, alien, bullets)


run_game()
