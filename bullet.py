import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    "一个对飞船发射子弹速度进行管理的类"
    def __init__(self, ai_settings, screen, ship):
        "飞船所处于的位置创建一个子弹对象"
        super(Bullet, self).__init__()
        self.screen = screen

        "（0,0）处创建一个表示子弹的矩形，再设置正确位置"
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
            ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx   
        self.rect.top = ship.rect.top

        #存储小数表示子弹位置
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    def update(self):
        "y值减去速度值，方便管理位置"
        self.y -= self.speed_factor
        self.rect.y = self.y
    def draw_bullet(self):
        "绘制子弹在屏幕上"
        pygame.draw.rect(self.screen, self.color, self.rect)
