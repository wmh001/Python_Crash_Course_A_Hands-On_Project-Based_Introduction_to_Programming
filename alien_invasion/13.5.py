# 13.5 射杀外星人
# 使用pygame.sprite.groupcollide()检测碰撞

# 13.5.1 检测子弹与外星人的碰撞
# 修改函数update_bullets()

# 13.5.2 为测试创建大子弹
# 将子弹宽度设置为300，便于击落外星人

# 13.5.3 生成新的外星人群
# 修改update_bullets()
# 消灭所有外星人后删除现有子弹并新建一群外星人

# 13.5.4 提高子弹速度
# 每次循环中，Pygame的工作更多了，使子弹速度减慢，需要微调子弹速度

# 13.5.5 重构update_bullets()
# 处理碰撞的代码整合到函数中
import game_functions13_5 as gf
import pygame
from pygame.sprite import Group
from settings13_5 import Settings
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
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        # 更新外星人
        gf.update_aliens(ai_settings, aliens)

        # 更新画布
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
