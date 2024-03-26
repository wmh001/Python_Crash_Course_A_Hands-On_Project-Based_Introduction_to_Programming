# 12.5 重构：模块game_functions
# 在大型项目中，重构既有代码旨在简化代码的结构，使其更容易扩展
import game_functions12_5 as gf
import pygame
from settings12_3 import Settings
from ship12_4 import Ship


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
    ship = Ship(screen)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        # 12.5.1 函数check_events()
        # 将管理事件的代码移到模块game_functions的函数check_events()中
        gf.check_events()

        # 12.5.2 函数update_screen()
        # 将管理每次循环时重绘游戏内容的代码移到模块game_functions的函数updata_screen()中
        gf.update_screen(ai_settings, screen, ship)


run_game()
