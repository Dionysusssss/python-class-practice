import pygame
from settings import Setting
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboad

def run_game():
    pygame.init()   #初始化pygame
    ai_settings = Setting()     #创建设置实例
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #创建实例
    play_button = Button(ai_settings, screen, "Play")
    ship = Ship(ai_settings, screen)
    stats = GameStats(ai_settings)
    sb = Scoreboad(ai_settings, screen, stats)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #游戏主循环
    while 1:
        #监控事件，鼠标或键盘
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            #每次都更新飞船的运行状况,更新在飞船实例里
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
        #每次循环都重新绘制屏幕（可以理解为一帧
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()