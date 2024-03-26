"""管理飞船"""

import pygame


class Ship:
    """管理飞船行为的类"""

    def __init__(self, screen):
        """初始化飞船并设置其初始位置"""
        # screen参数的类型为窗口Surface类
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        # pygame.image.load(
        #     图像文件路径<字符串> | 无默认值,
        #     其他参数: 均有默认值)
        # 返回一个Surface实例，记录从文件加载的新图像
        # 返回的Surface实例将包含与其源文件相同的颜色格式和alpha透明度等
        # Pygame并不总是支持所有的图像格式，至少支持未压缩的BMP，Pygame将根据文件扩展名确定图像类型
        self.image = pygame.image.load(r"alien_invasion\images\ship.bmp")

        # 在Pygame中，原点位于画布左上角，x轴正方向为水平向右，y轴正方向为垂直向下，单位长度为1像素

        # pygame.Surface实例.get_rect()
        # 返回一个Rect实例，记录Surface实例的外接矩形的宽、高、左上角坐标、中心坐标等属性
        # 修改Rect实例的各种坐标属性会根据宽、高属性自动调整其他属性

        # pygame.Rect实例常用属性：
        # x<整型数>：左上角横坐标
        # y<整型数>：左上角纵坐标
        # top<整型数>=y<整型数>：顶边纵坐标
        # left<整型数>=x<整型数>：左边横坐标
        # bottom<整型数>：底边纵坐标
        # right<整型数>：右边横坐标
        # w/width<整型数>：宽度
        # h/height<整型数>：高度
        # centerx<整型数>：中心横坐标
        # centery<整型数>：中心纵坐标
        # center<二元组>=(centerx<整型数>, centery<整型数>)：中心坐标
        # size<二元组>=(w<整型数>, h<整型数>)：尺寸
        # topleft<二元组>=(x<整型数>, y<整型数>)/(left<整型数>, top<整型数>)：左上角坐标
        # bottomleft<二元组>=(left<整型数>, bottom<整型数>)：左下角坐标
        # topright<二元组>=(right<整型数>, top<整型数>)：右上角坐标
        # bottomright<二元组>=(right<整型数>, bottom<整型数>)：右下角坐标
        # midtop<二元组>=(centerx<整型数>, top<整型数>)：顶边中心坐标
        # midleft<二元组>=(left<整型数>, centery<整型数>)：左边中心坐标
        # midbottom<二元组>=(centerx<整型数>, bottom<整型数>)：底边中心坐标
        # midright<二元组>=(right<整型数>, centery<整型数>)：右边中心坐标

        # 新创建图像Rect的默认左上角位置为(0, 0)，默认尺寸为图片原尺寸
        self.rect = self.image.get_rect()
        # 窗口Rect的左上角位置为(0, 0)，尺寸为窗口创建时设定尺寸
        self.screen_rect = screen.get_rect()

        # 设置飞船初始位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """在指定位置绘制飞船"""
        # pygame.Surface实例.blit(
        #     source=待绘制的图像<Surface类> | 无默认值,
        #     dest=绘制位置<二元组/Rect类>: 二元组格式为(横坐标, 纵坐标)，视为左上角坐标;
        #         接收一个Rect实例，那么函数会访问它的左上角坐标 | 无默认值,
        #     其他参数: 均有默认值)
        # 在指定位置将待绘制的图像Surface实例绘制到该Surface实例上
        self.screen.blit(self.image, self.rect)
