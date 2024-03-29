# 14.2 提高等级
# 消灭一次外星人群后，加快游戏节奏

# 14.2.1 修改速度设置
# 重新组织Settings类

# 14.2.2 重置速度
# 修改函数check_play_button()
import game_functions14_2 as gf
import pygame
from button14_1 import Button
from game_stats14_1 import GameStats
from pygame.sprite import Group
from settings14_2 import Settings
from ship13_6 import Ship


def run_game():
    """运行游戏"""
    # 初始化游戏并创建一个窗口
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建数据跟踪实例
    stats = GameStats(ai_settings)
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
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)

        if stats.game_active:
            # 更新飞船
            ship.update()
            # 更新子弹
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            # 更新外星人
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        # 更新画布
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)


run_game()
