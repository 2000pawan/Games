class Settings():
    # A class to store all settings for Alien Invasion.
    def __init__(self):
        # Initialize the game settings.
        
        # Screen settings.
        self.screen_width = 1400
        self.screen_height = 900
        self.bg_color = (255,215,0)
        self.ship_speed_factor=1.5
        
        # Bullet settings
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 13
        self.bullet_color = 255,0,0
        self.bullets_allowed=4