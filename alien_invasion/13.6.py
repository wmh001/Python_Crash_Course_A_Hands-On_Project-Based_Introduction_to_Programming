# 13.6 结束游戏
# 外星人撞到飞船或画布底部，玩家损失一艘飞船，玩家损失三艘飞船后，游戏结束

# 13.6.1 检测外星人和飞船碰撞
# 修改update_aliens()

# 13.3.2 响应外星人和飞船的碰撞
# 创建统计飞船被撞次数的类GameStats

# 13.3.3 有外星人到达屏幕底端
# 添加新函数check_aliens_bottom()

# 13.3.4 游戏结束
# 类GameStats添加新属性
import game_functions13_6 as gf
import pygame
from game_stats13_6 import GameStats
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
        gf.check_events(ai_settings, screen, ship, bullets)

        # 更新飞船
        ship.update()
        # 更新子弹
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        # 更新外星人
        gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        # 更新画布
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
