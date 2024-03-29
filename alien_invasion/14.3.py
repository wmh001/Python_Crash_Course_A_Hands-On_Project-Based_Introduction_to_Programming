# 14.3 记分
# 类GameStats添加属性

# 14.3.1 显示得分
# 创建新类Scoreboard

# 14.3.2 创建记分牌
# 创建Scoreboard实例
# 修改update_screen()

# 14.3.3 在外星人被消灭时更新得分
# 修改类Settings和函数check_bullet_alien_collisions()、update_bullets()

# 14.3.4 将消灭的每个外星人的点数都计入得分
# 一颗子弹消灭多个外星人时多次记分
# 修改函数check_bullet_alien_collisions()

# 14.3.5 提高点数
# 玩家提高等级时，击落每个外星人获得更多分数
# 修改类Settings

# 14.3.6 将得分圆整
# 分数通常为10的倍数
# 修改Scoreboard类

# 14.3.7 最高得分
# 在类GameStats中跟踪最高得分
# 显示最高得分
# 修改类GameStats、Scoreboard和函数check_bullet_alien_collisions()

# 14.3.8 显示等级
# 在GameStats中添加属性，修改函数check_bullet_alien_collisions()、check_play_button()

# 14.3.9 显示余下的飞船数
# 使用图像指出余下的飞船数
# 修改类Ship、Scoreboard和函数check_play_button()、upfate_aliens()、ship_hit()、check_aliens_bottom()
import game_functions14_3 as gf
import pygame
from button14_1 import Button
from game_stats14_3 import GameStats
from pygame.sprite import Group
from scoreboard14_3 import Scoreboard
from settings14_3 import Settings
from ship14_3 import Ship


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

    # 创建数据跟踪实例和记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
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
        gf.check_events(
            ai_settings, screen, stats, sb, play_button, ship, aliens, bullets
        )

        if stats.game_active:
            # 更新飞船
            ship.update()
            # 更新子弹
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            # 更新外星人
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        # 更新画布
        gf.update_screen(
            ai_settings, screen, stats, sb, ship, aliens, bullets, play_button
        )


run_game()
