import pygame


class Bullet(pygame.sprite.Sprite):
    """A projectile launched by the player"""
    def __init__(self, x, y, bullet_group, player):
        """Initialize the bullet"""
        super().__init__()
        
        # Set constants 
        self.velocity = 20
        self.range = 500
        
        # Load image and get rect
        if player.velocity.x > 0:
            self.image = pygame.transform.scale(pygame.image.load("Assets/images/player/slash.png"), (50, 13))
        else:
            self.image = pygame.transform.scale(pygame.transform.flip(pygame.image.load("Assets/images/player/slash.png"), True, False), (50, 13))
            self.velocity = -1 * self.velocity
            
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        self.starting_x = x
        
        bullet_group.add(self)
        
    def update(self):
        """Update the bullet"""
        self.rect.x += self.velocity
        
        # If the bullet has passed the range, kill it
        if abs(self.rect.x - self.starting_x) > self.range:
            self.kill()
