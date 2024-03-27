# 12.7 简单回顾

# 12.7.1 主文件
# 主文件：创建所有对象：设置实例、窗口实例、飞船实例
#     包含游戏主循环：处理事件、更新飞船、更新画布

# 12.7.2 settings.py
# Settings类：__init__()：存储窗口属性和飞船速度

# 12.7.3 game_functions.py
# check_events()：检测事件
#     check_keydown_events()：处理按下事件
#     check_keyup_events()：处理松开事件
# update_screen()：重绘画布

# 12.7.4 ship.py
# Ship类：模拟飞船
#     __init__()：初始化飞船属性
#     update()：更新飞船位置
#     blitme()：绘制飞船
