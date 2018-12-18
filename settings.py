class Settings():
    def __init__(self):
        self.screen_width = 1100
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        #rect centerx只能存储整数
        self.ship_speed_factor = 2.5   
        self.ship_limit = 3
        self.bullet_speed_factor = 5
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = 60, 60 ,60
        self.bullets_allowed = 10
        
        self.alien_speed_factor = 2
        self.fleet_drop_speed = 10
        #fleet direction +1向右移动  -1向左移动
        self.fleet_direction = 1
