# 12.3 开始游戏项目
# 创建空白Pygame窗口，令其响应用户输入

# 12.3.1 创建Pygame窗口以及响应用户输入
import sys

import pygame
from settings12_3 import Settings


def run_game():
    """运行游戏"""
    # 初始化游戏并创建一个窗口
    # pygame.init()
    # 初始化pygame的所有模块
    pygame.init()

    # 12.3.2 设置背景色
    # 设置背景色
    # 在Pygame中，颜色为RGB格式

    # 12.3.3 创建设置类
    # 将游戏所有的设置存储在一个类的实例中，方便管理
    ai_settings = Settings()
    # 窗口内的区域称为画布
    # 在Pygame中，Pygame.Surface实例是屏幕的一部分，用于显示游戏元素
    # 窗口和游戏显示的其他元素各自都属于一个Surface实例
    # 窗口Surface实例在激活游戏的动画循环后，每经一轮循环都进行自动重绘
    # pygame.display.set_mode(
    #     size=窗口大小<二元组>: (宽（像素）, 高（像素）) | (0, 0),
    #     其他参数: 均有默认值)
    # 返回指定大小的窗口Surface实例
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    # pygame.display.set_caption(
    #     窗口标题<字符串> | 无默认值,
    #     其他参数: 均有默认值)
    # 设置当前窗口标题
    pygame.display.set_caption("Alien Invasion")

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        # pygame.event.get()
        # 返回Pyname检测到的事件组成的集合，其元素类型为pygame.event.EventType（事件）类

        # pygame.event.EventType（事件）实例的常用属性：
        # type<pygame定义的事件种类常量>：事件实例的种类
        # key<pygame定义的按键常量>：触发事件实例的键盘按键

        # 常用pygame定义的事件常量：
        # pygame.QUIT：窗口关闭事件，当用户点击窗口的关闭按钮时触发
        # pygame.KEYDOWN：按键按下事件，当用户键盘的某个键按下时触发
        # pygame.KEYUP：按键松开事件，当用户键盘的某个键松开时触发
        # pygame.MOUSEBUTTONDOWN：鼠标按键按下事件，当鼠标按键被按下时触发

        # 常用pygame定义的按键常量：
        # pygame.K_RIGHT：右方向键
        # pygame.K_LEFT：左方向键
        # pygame.K_SPACE：空格键
        # pygame.K_q：Q键
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # sys.exit()
                # 退出当前程序的执行
                sys.exit()

        # 每次循环时重绘屏幕
        # pygame.Surface实例.fill(
        #     color=填充颜色<三元组/四元组>: 颜色为RGB或RGBA格式,
        #     rect=绘制位置<pygame.Rect类> | 填充整个Surface实例,
        #     其他参数: 均有默认值)
        # 使用纯色依参数rect填充Surface实例上的矩形范围
        # 用颜色填充画布
        screen.fill(ai_settings.bg_color)

        # 让最近的绘制的窗口可见
        # pygame.display.flip()
        # 将所有待显示的Surface实例省略更新到屏幕上，去除旧Surface实例
        pygame.display.flip()


run_game()
