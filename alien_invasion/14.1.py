# 14.1 添加Play按钮
# 添加Play按钮，在游戏开始前和游戏结束后出现，让玩家开始游戏
# 让游戏一开始处于非活动状态

# 14.1.1 创建Button类
# 创建按钮类

# 14.1.2 在屏幕上绘制按钮
# 修改update_screen()

# 14.1.3 开始游戏
# 修改check_events()

# 14.1.4 重置游戏
# 点击Play按钮后重置统计信息、外星人和子弹
# 修改check_play_button()

# 14.1.5 将Play按钮切换到非活动状态
# 游戏开始后，点击Play不可响应
# 修改check_play_button()

# 14.1.6 隐藏光标
# 游戏开始后，隐藏鼠标光标
# 修改check_play_button()和ship_hit()
import game_functions14_1 as gf
import pygame
from button14_1 import Button
from game_stats14_1 import GameStats
from pygame.sprite import Group
from settings13_6 import Settings
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
