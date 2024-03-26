# 12.6 驾驶飞船
# 使用反向键控制飞船移动

# 12.6.1 响应按键
# 按下右键移动一个像素
# 修改类Ship，添加函数check_events()

# 12.6.2 允许不断移动
# 按下右键不放时，飞船不断移动，直到松开按键
# 修改类Ship，修改函数check_events()

# 12.6.3 左右移动
# 与向右移动的逻辑相同，添加向左移动
# 修改类Ship，修改函数check_events()

# 12.6.4 调整飞船的速度
# 在Settings类中添加属性，用于控制飞船速度，修改类Ship

# 12.6.5 限制飞船的活动范围
# 让飞船到达画布边缘后停止移动，修改类Ship

# 12.6.6 重构check_events()
# 将处理KEYDOWN事件和处理KEYUP事件的代码列为函数
import game_functions12_6 as gf
import pygame
from settings12_6 import Settings
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

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ship)

        # 更新飞船
        ship.update()

        # 更新画布
        gf.update_screen(ai_settings, screen, ship)


run_game()
