import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings=Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion (Developed by @PawanYadav)")
    
    # Make a Ship.
    ship = Ship(ai_settings,screen)
     
    # Make a group to store bullets in.
    bullets = pygame.sprite.Group()
    
    # Set the background color.
    bg_color = (135,206,235)
    
    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings,screen,ship,bullets)

run_game()