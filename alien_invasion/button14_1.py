"""管理按钮类Button"""

import pygame.font


class Button:
    """带标签按钮"""

    def __init__(self, ai_settings, screen, msg):
        """初始化按钮属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 设置按钮尺寸和其他属性
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)  # 亮绿色
        self.text_color = (255, 255, 255)  # 白色
        # pygame.font.SysFont(
        #     name=字体名<str>: None表示Pygame内建的默认字体 | 无默认值,
        #     size=字体大小<整型数> | 无默认值,
        #     bold=是否加粗<布尔> | False,
        #     italic=是否斜体<布尔> | False)
        # 返回依据参数从系统字体库新创建的一个字体实例（pygame.font.Font实例）
        self.font = pygame.font.SysFont(None, 48)

        # 创建按钮Rect实例，并使按钮居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 按钮的标签只需创建一次
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """将msg渲染为图像，并使其在按钮上居中"""
        # pygame.font.Font实例.render(
        #     text=待绘制的文字<字符串>: 仅支持渲染一行文本，换行符不会被渲染 | 无默认值,
        #     antialias=是否抗锯齿<布尔> | 无默认值,
        #     color=文字颜色<三元组>: 颜色为RGB格式,
        #     background=背景颜色<三元组>: 颜色RGB格式 | None: 表示透明)
        # 返回一个新创建的其上依据参数绘制有文本的Surface实例
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """绘制按钮和文本"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
