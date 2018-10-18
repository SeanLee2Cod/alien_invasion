# -*- coding:utf-8 -*-
'''
@author: SeanLee
@licence: (C)Copyright
'''
import sys

import pygame


def check_event(ship):
    '''响应按钮和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                #向右移动飞船
                ship.moving_right = True
            if event.key == pygame.K_LEFT:
                #向左移动飞船
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                #停止飞船向右移动
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                #停止飞船向左移动
                ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    '''更新屏幕上的图像，并切换到新屏幕'''

    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()