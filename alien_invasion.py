#!/usr/bin/python3
import sys
import pygame
from setting import Settings
from ship import Ship

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    #screen = pygame.display.set_mode((1200,800))
    ai_settings = Settings()
    screen = pygame.display.set_mode(
    (ai_settings.screen_width,ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    #创建一艘飞船
    ship = Ship(screen)


    #设置背景颜色
    bg_color = (230, 230, 230)
    #开始游戏的主循环
    while True:

        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #每次循环时都会重绘屏幕
        #screen.fill(bg_color)
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        #让最近描绘的屏幕可见
        pygame.display.flip()

run_game()
