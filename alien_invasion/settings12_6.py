"""存储游戏设置"""


class Settings:
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏设置"""

        # 窗口设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)  # 浅灰色

        # 飞船设置
        # 速度>1，飞船速度将比不设置速度快
        self.ship_speed_factor = 1.5
