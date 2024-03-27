"""定义游戏调用的函数"""

import sys

import pygame
from bullet12_8 import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        # ship.rect.centerx += 1
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 向左移动飞船
        ship.moving_left = True
        # 射击
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def fire_bullet(ai_settings, screen, ship, bullets):
    """如果还没有到达限制，就发射一颗子弹"""
    # 创建一颗子弹并加入编组
    # len(
    #     编组实例<pygame.sprite.Group类> | 无默认值)
    # 返回编组实例内元素的数量
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        # pygame.sprite.Group实例.add(
        #     待加入的精灵<pygame.sprite.Sprite子类> | 无默认值)
        # 将精灵实例加入编组实例
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    """更新画布上的图像，并更新画布"""
    # 每次循环时重绘画布
    screen.fill(ai_settings.bg_color)
    # 每次循环时重绘所有子弹
    # pygame.sprite.Group实例.sprites()
    # 返回包含编组实例内所有精灵实例的列表
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 每次循环时重绘飞船
    ship.blitme()

    # 让最近的绘制的Surface实例显示
    pygame.display.flip()


def update_bullets(bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    # 更新子弹的位置
    # pygame.sprite.Group实例.update()
    # 对编组实例内的每个精灵实例调用update()方法
    bullets.update()
    # 删除已消失的子弹
    # pygame.sprite.Group实例.copy()
    # 返回新创建的编组实例，其每个元素与原编组实例内的精灵实例是同一个
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            # pygame.sprite.Group实例.remove(
            #     已加入的精灵<pygame.sprite.Sprite类> | 无默认值)
            # 将精灵实例移出编组实例
            bullets.remove(bullet)
    # print(len(bullets))
