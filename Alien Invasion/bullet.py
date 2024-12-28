import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""
    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.ship = ship

        # Create a bullet rect at (0,0) and set correct final position.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen."""
        # Update the bullet's position.
        self.y -= self.speed_factor
        # Update the rect position.
        self.rect.y = self.y

        # Check if the bullet has moved off the top of the screen.
        if self.is_off_screen():
            self.kill()

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def __str__(self):
        return f"Bullet at position ({self.rect.x}, {self.rect.y})"

    def __repr__(self):
        return f"Bullet(rect={self.rect}, color={self.color}, speed_factor={self.speed_factor})"

    def reset(self):
        """Reset the bullet to the ship's position."""
        self.rect.centerx = self.ship.rect.centerx
        self.rect.top = self.ship.rect.top
        self.y = float(self.rect.y)

    def is_off_screen(self):
        """Check if the bullet has moved off the top of the screen."""
        return self.rect.bottom < 0

    def move(self):
        """Move the bullet."""
        self.update()

    def draw(self):
        """Draw the bullet."""
        self.draw_bullet()