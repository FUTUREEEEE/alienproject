import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_settings, screen):                                  #初始化飞船 并设置其初始位置
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #加载飞船图像 并获取其外接矩形(rect)
        self.image = pygame.image.load('images/ship.bmp')        #加载图像 返回surface
        self.rect = self.image.get_rect()                        #获得相应surface的rect
        self.screen_rect = screen.get_rect()

        #将每艘飞船放在屏幕底部中央，处理rect对象 指定rect的位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        #移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        #根据移动标志调整飞船的位置
        #更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        #根据self.center更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        #在指定位置绘制飞船，根据self.rect()指定的位置
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        #飞船在屏幕剧中
        self.center = self.screen_rect.centerx


