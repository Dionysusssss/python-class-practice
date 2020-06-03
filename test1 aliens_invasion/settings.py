class Setting():
    """相关设置内容"""
    def __init__(self):
        """初始化游戏的静态设置"""
        #屏幕
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        #飞船
        self.ship_limit = 2
        #子弹
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
        #外星人
        self.fleet_drop_speed = 10
        #以什么样的速度加快游戏节奏
        self.speedup_scale = 1.2
        self.score_scale = 2

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 2
        self.alien_speed_factor = 0.5
        self.fleet_direction = 1  # 1表示向右,-1表示向左
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
