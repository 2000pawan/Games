import pygame.font
from pygame.sprite import Group
from ship import Ship
import pygame
import os

class Heart(pygame.sprite.Sprite):
    """A class to represent the heart (life) as a sprite"""
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('G:\\Coding\\Git Uploads\\Project\\Games\\Alien Invasion\\assets\\heart.png')
        self.image = pygame.transform.scale(self.image, (30,30)) 
        self.rect = self.image.get_rect()
    
    def update(self):
        """Update the position of the heart"""
        pass

class Scoreboard():
    '''A class to handle the scoreboard'''
    def __init__(self, ai_settings, screen, stats):
        '''Initialize the scoreboard attributes'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        
        # Font settings for the scoreboard
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont('arial', 30)
        
        # Prepare the initial score images
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
        self.high_score_file = os.path.join('high_score.txt')
        
        self.game_over_image = self.font.render("Game Over", True, self.text_color, self.ai_settings.bg_color)
        self.game_over_rect = self.game_over_image.get_rect()
        self.game_over_rect.center = self.screen_rect.center
        
    def load_high_score(self):
        try:
            with open(self.high_score_file, "r") as file:
                self.stats.high_score = int(file.read().strip())
        except FileNotFoundError:
            self.stats.high_score = 0

    def save_high_score(self):
        '''Save the high score to a file.'''
        with open(self.high_score_file, "w") as file:
            file.write(str(self.stats.high_score))

    def prep_score(self):
        '''Turn the score into a rendered image'''
        round_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(round_score)
        self.score_image = self.font.render(f"Score: {score_str}", True, self.text_color, self.ai_settings.bg_color)
        
        # Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def prep_high_score(self):
        '''Turn the high score into a rendered image'''
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(f"High Score: {high_score_str}", True, self.text_color, self.ai_settings.bg_color)
        
        # Center the high score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx+250
        self.high_score_rect.top = self.score_rect.top
    
    def update_high_score(self):
        '''Update the high score if the current score exceeds it'''
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
        
    def show_score(self):
        '''Draw the score on the screen'''  
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # Draw the ships remaining
        self.ships.draw(self.screen)
            
            
    def prep_level(self):
        '''Turn the level into a rendered image'''
        level_str = f"Level: {self.stats.level}"
        self.level_image = self.font.render(level_str, True, self.text_color, self.ai_settings.bg_color)
        
        # Position the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
        
    def prep_ships(self):
        ''' Show how many hearts (lives) are left '''
        self.ships = Group()  # Still using 'ships' as the group name
        for ship_number in range(self.stats.ships_left):
            # Create a Heart sprite for each remaining life
            heart = Heart(self.ai_settings, self.screen)
            heart.rect.x = 10 + ship_number * (heart.rect.width + 5)  # Position hearts with space
            heart.rect.y = 10
            self.ships.add(heart)  # Add the heart sprite to the group

            
    def show_game_over(self):
        '''Display Game Over message'''
        self.screen.blit(self.game_over_image, self.game_over_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        
        # Draw hearts (lives) one by one
        for heart in self.ships:
            heart_rect = heart.rect
            self.screen.blit(heart.image, heart_rect)