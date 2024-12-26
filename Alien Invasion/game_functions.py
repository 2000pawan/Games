import sys 
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet."""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypress and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_bullets(ai_settings,screen,ship,aliens, bullets):
    """Update the position of bullets and get rid of old bullets."""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen,ship, aliens, bullets)
 
def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    """Respond to bullet-alien collisions."""
    # Remove any bullets and aliens that have collided.
    # collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        # Destroy existing bullets and create new fleet.
        bullets.empty()
        create_fleet(ai_settings, screen,ship, aliens)
        
        
def create_fleet(ai_settings, screen,ship, aliens):
    """Create a fleet of aliens."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    available_space_x = ai_settings.screen_width - (2 * alien_width)
    ship_height = ai_settings.ship_height
    available_space_y = ai_settings.screen_height - (3 * alien_height) - ship_height
    if available_space_x <= 0 or available_space_y <= 0:
        print("Not enough space for aliens.")
        return
    
    number_aliens_x = available_space_x // (2 * alien_width)
    number_rows = available_space_y // (2 * alien_height)
    
    print(f"Available Space X: {available_space_x}, Available Space Y: {available_space_y}")
    print(f"Number of Aliens X: {number_aliens_x}, Number of Rows: {number_rows}")
    
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in the row."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + (2 * alien_width * alien_number)
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + (2 * alien.rect.height * row_number)
    aliens.add(alien)
    # print(f"Alien created at X: {alien.rect.x}, Y: {alien.rect.y}")

def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Update images on the screen, and flip to the new screen."""
    screen.fill(ai_settings.bg_color)

    # Draw bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Draw ship
    ship.blitme()

    # Draw aliens
    aliens.draw(screen)

    pygame.display.flip()
    
def check_fleet_edges(ai_settings, aliens):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change its direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
  
def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """Respond to ship being hit by alien."""
    if stats.ships_left > 0:
        # Decrement ships left and reset ship's position.
        stats.ships_left -= 1
        ship.center_ship()
        # Pause.
        sleep(0.5)
    else:
        stats.game_active = False
        
def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break
 
def update_aliens(ai_settings,stats,screen,ship, aliens,bullets):
    """Update the Position of all aliens in the fleet."""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    # Look for alien-ship collisions.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets)
