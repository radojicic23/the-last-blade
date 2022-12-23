import pygame


class Background(pygame.sprite.Sprite):
    """A tile that is animated. A background will be generated here"""
    def __init__(self, x, y, main_group):
        """Initialize the background"""
        super().__init__()
        
        # Animation frames
        self.background_sprites = []
        
        # Animation
        self.background_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/background/1.png"), (1280, 736)))
        self.background_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/background/2.png"), (1280, 736)))
        self.background_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/background/3.png"), (1280, 736)))
        self.background_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/background/4.png"), (1280, 736)))
        self.background_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/background/5.png"), (1280, 736)))
        self.background_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/background/6.png"), (1280, 736)))
        self.background_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/background/7.png"), (1280, 736)))
        self.background_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/background/8.png"), (1280, 736)))
        self.background_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/background/9.png"), (1280, 736)))
        self.background_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/background/10.png"), (1280, 736)))
        self.background_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/background/11.png"), (1280, 736)))
        self.background_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/background/12.png"), (1280, 736)))
        self.background_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/background/13.png"), (1280, 736))) 

        # Load image and get rect
        self.current_sprite = 0
        self.image = self.background_sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)
        
        # Add to the main group for drawing purposes
        main_group.add(self)
                
    def update(self):
        """Update the background"""
        self.animate(self.background_sprites, .25)
    
    def animate(self, sprite_list, speed):
        """Animate the background"""
        if self.current_sprite < len(sprite_list) - 1:
            self.current_sprite += speed
        # Start over
        else:
            self.current_sprite = 0
        
        self.image = sprite_list[int(self.current_sprite)]
