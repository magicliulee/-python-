import pygame
class Ship():

    def __init__(self,ai_settings, screen):
        #初始化飞船设置初试位置
        self.screen = screen
        self.ai_settings = ai_settings  #获取速度位置
        self.image = pygame.image.load('D:\\python\\pythontext\\images\\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #飞船属性储存最小值（为了准确存储飞船位置）
        self.center = float(self.rect.centerx)
        #移动标志
        self.moving_right = False
        self.moving_left = False
    def update(self):
        #根据移动标志做出反应    
        #更新  飞船self center 可存储小数
        if self.moving_right and self.rect.right < self.screen_rect.right:
            #self.rect.centerx += 1
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            #self.rect.centerx -= 1
            self.center -= self.ai_settings.ship_speed_factor
        #根据self center 更新rect
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        #让飞船在屏幕上居中
        self.center = self.screen_rect.centerx
