import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from gama_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()   #初始化背景设置
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))  #创建名字为screen的显示窗口 指定游戏窗口尺寸  可调
    pygame.display.set_caption("Alien Invasion")

    #创建play按钮
    play_button = Button(ai_settings, screen, "play")
    bg_color = (230, 230, 230)            #设置背景色

    #创建一艘飞船,子弹，外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    #创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #创建一个用于储存游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    #开始游戏主循环
    while True:

        #监视键盘和鼠标事件
        gf.check_event(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game() #初始化游戏 并开始主循环


