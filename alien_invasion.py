import sys
import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    #screen = pygame.display.set_mode((1100,700))
    pygame.display.set_caption("Allien Invasion")

    #bg_color = (230, 230, 230)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    #创建一个外星人
    alien = Alien(ai_settings, screen)
    aliens = Group()
    #外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens )
    #创建一个用于存储游戏统计信息的事例
    stats = GameStats(ai_settings)

    while True:
        #for event in pygame.event.get():
        #    if event.type == pygame.QUIT:
        #        sys.exit()
        #screen.fill(bg_color)
        #screen.fill(ai_settings.bg_color) 
        #ship.blitme()  
        gf.check_events(ai_settings, screen, ship,  bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
     
       
        #print(len(bullets))核实子弹消除for循环移到game
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

        pygame.display.flip()

run_game()


    
