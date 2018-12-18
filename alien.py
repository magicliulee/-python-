import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        #加载外星人图像并且设置其rect属性
        self.image = pygame.image.load('D:\\python\\pythontext\\images\\hrg.bmp')
        self.rect = self.image.get_rect()

        #每个对方初始位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #存储对方准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        #指定位置绘制对方
        self.screen.blit(self.image, self.rect)

    
    def check_edges(self):
        "如果外星人位于屏幕边缘。则返回值true"
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
            
    def update(self):
        "向右移动外星人" "向左移动外星人"
        self.x += (self.ai_settings.alien_speed_factor *
            self.ai_settings.fleet_direction)
        self.rect.x = self.x
