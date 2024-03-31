# 12.8 射击
# 玩家按空格时发射子弹（小矩形），子弹将在屏幕中向上穿行，抵达画布定边后消失

# 12.8.1 添加子弹设置
# 在Settings类中添加子弹Bullet类需要的设置

# 12.8.2 创建Bullet类

# 12.8.3 将子弹存储到编组中
# 编组用于存储所有的子弹
# pygame.sprite.Sprite（精灵）类可将游戏中相关的元素编组（加入pygame.sprite.Group（编组）类），进而同时操作编组中的所有元素

# 12.8.4 开火
# 修改函数check_keydown_events()、check_events()、update_screen()

# 12.8.5 删除已消失的子弹
# 移动到画布外的子弹需要手动删除，否则增加计算机负担

# 12.8.6 限制子弹数量
# 限制同时出现在屏幕上的子弹数量，以鼓励玩家有目标的射击
# 修改类Settings、函数check_keydown_events()

# 12.8.7 创建函数update_bullets()
# 将主函数的子弹管理代码整合到新函数中

# 12.8.8 创建函数fire_bullet()
# 将发射子弹的代码整合到新函数中
import game_functions12_8 as gf
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
    # pygame.sprite.Group()
    # 返回新创建的编组实例
    # 编组未规定元素顺序
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
