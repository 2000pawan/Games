import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    # Initialize game and create a screen object.
    pygame.init()  
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion (Developed by @PawanYadav)")
    
    # Create an instance to store game statistics and create a ship, alien, and bullets.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    # Make a Ship, a group of bullets, and a group of aliens,Play Button.
    ship = Ship(ai_settings, screen)
    bullets = pygame.sprite.Group()
    aliens = pygame.sprite.Group()
    play_button=Button(ai_settings,screen,"Play")
    
    # Set the background color.
    bg_color = (255,215,0)
    
    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen,ship, aliens)

    
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        
        if stats.game_active:
            # Update the ship and check for collisions
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
            
            # Update the scoreboard (check if high score is beaten)
            if stats.score > stats.high_score:
                stats.high_score=stats.score  # Update high score if needed
                sb.prep_high_score()  # Update displayed high score
        else:
            if stats.ships_left==0:
                sb.save_high_score()
            
        # If no ships left, show the "Game Over" screen
        if stats.ships_left==0:
            sb.show_game_over()
            pygame.display.flip()
            pygame.time.wait(1000)
            stats.game_active=False
            

        # Update the screen after each frame
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        
        pygame.display.flip()  # Refresh the display

if __name__ == "__main__":
    run_game()