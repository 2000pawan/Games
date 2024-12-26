import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien
from game_stats import GameStats

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion (Developed by @PawanYadav)")
    
    # Create an instance to store game statistics and create a ship, alien, and bullets.
    stats = GameStats(ai_settings)
    
    # Make a Ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)
    bullets = pygame.sprite.Group()
    aliens = pygame.sprite.Group()
    
    # Set the background color.
    bg_color = (135, 206, 235)
    
    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen,ship, aliens)
    
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen,ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats,screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
            
if __name__ == "__main__":
    run_game()