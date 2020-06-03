import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #加载飞船图像且获取其外接矩形,将屏幕数据入screen_rect，而飞机数据入rect，用于下一部分调用
        self.image = pygame.image.load('images/plane.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #把每一飞船放在屏幕底部中央，将屏幕的底部中间数据，赋值给飞机所在位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)

        #持续移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        #更新的是飞船的center值!!
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center     #先存入center再移动后存入rect.centerx

    def blitme(self):
        #在指定位置绘制飞船，调用函数，image为图像，rect为上述处理后飞机位置
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """让飞船居中"""
        self.center = self.screen_rect.centerx