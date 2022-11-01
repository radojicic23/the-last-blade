import pygame, random


class Portal(pygame.sprite.Sprite):
    """A class that if collided with will teleport you"""
    def __init__(self, x, y, color, portal_group):
        """Initialize the portal"""
        super().__init__()
        
        # Animation frames
        self.portal_sprites = []
        
        # Portal animation
        if color == "green":
            # Green portal Images
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/portals/green/tile001.png"), (70, 70)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/portals/green/tile002.png"), (70, 70)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/portals/green/tile003.png"), (70, 70)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/portals/green/tile004.png"), (70, 70)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/portals/green/tile005.png"), (70, 70)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/portals/green/tile006.png"), (70, 70)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/portals/green/tile007.png"), (70, 70)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/portals/green/tile008.png"), (70, 70)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/portals/green/tile009.png"), (70, 70)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/portals/green/tile010.png"), (70, 70)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/portals/green/tile011.png"), (70, 70)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/portals/green/tile012.png"), (70, 70)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/portals/green/tile013.png"), (70, 70)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/portals/green/tile014.png"), (70, 70)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/portals/green/tile015.png"), (70, 70)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/portals/green/tile016.png"), (70, 70)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/portals/green/tile017.png"), (70, 70)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/portals/green/tile018.png"), (70, 70)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/portals/green/tile019.png"), (70, 70)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/portals/green/tile020.png"), (70, 70)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/portals/green/tile021.png"), (70, 70)))
        else:
            # Purple
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/portals/purple/tile001.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/portals/purple/tile002.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/portals/purple/tile003.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/portals/purple/tile004.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/portals/purple/tile005.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/portals/purple/tile006.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/portals/purple/tile007.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/portals/purple/tile008.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/portals/purple/tile009.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/portals/purple/tile010.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/portals/purple/tile011.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/portals/purple/tile012.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/portals/purple/tile013.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/portals/purple/tile014.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/portals/purple/tile015.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/portals/purple/tile016.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/portals/purple/tile017.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/portals/purple/tile018.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/portals/purple/tile019.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/portals/purple/tile020.png"), (72, 72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/portals/purple/tile021.png"), (72, 72)))
            
        # Load an image and get a rect
        self.current_sprite = random.randint(0, len(self.portal_sprites) - 1)
        self.image = self.portal_sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)
        
        # Add to the portal group
        portal_group.add(self)
        
    def update(self):
        """Update the portal"""
        self.animate(self.portal_sprites, .2)
    
    def animate(self, sprite_list, speed):
        """Animate the portal"""
        if self.current_sprite < len(sprite_list) - 1:
            self.current_sprite += speed
        else:
            self.current_sprite = 0
        
        self.image = sprite_list[int(self.current_sprite)]
