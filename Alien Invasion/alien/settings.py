import pygame
class Settings():
    # A class to store all settings for Alien Invasion.
    def __init__(self):
        # Initialize the game settings.
        
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255,215,0)
        self.heart_image=pygame.font.SysFont('arial', 50).render('❤️', True, (255, 0, 0))  # Red heart
        self.ship_limit=3
        self.fleet_drop_speed = 20
        
        # Ship Settings
        self.ship_height=60 
               
        # Bullet settings
        self.bullet_width = 3
        self.bullet_height =10
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 4
        
        # How quickly the game speeds up.
        self.speedup_scale = 1.1
        self.score_scale=1.5
        self.initialize_dynamic_settings()
        
        # How quickly the alien points increase.
        self.alien_points_scale = 1.5
        
    def initialize_dynamic_settings(self):
        # Initialize settings that change throughout the game.
        self.ship_speed_factor=4
        self.bullet_speed_factor=4
        self.alien_speed_factor=2
        
        # Fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        
        # Scoring
        self.alien_points = 50
    
    def increase_speed(self):
        # Increase speed settings and alien point values.
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
        self.alien_points=int(self.alien_points*self.score_scale)
        print(self.alien_points)
        
        
        
