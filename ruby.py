import pygame, random

from display import WINDOW_WIDTH, WINDOW_HEIGHT


vector = pygame.math.Vector2


class RubyMaker(pygame.sprite.Sprite):
    """A tile that is animated. A ruby will be generated here"""
    def __init__(self, x, y, main_group):
        """Initialize the ruby maker"""
        super().__init__()
        
        # Animation frames
        self.ruby_sprites = []
        
        # Rotating animation
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/ruby/tile000.png"), (64, 64)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/ruby/tile001.png"), (64, 64)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/ruby/tile002.png"), (64, 64)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/ruby/tile003.png"), (64, 64)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/ruby/tile004.png"), (64, 64)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/ruby/tile005.png"), (64, 64)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/ruby/tile006.png"), (64, 64)))

        # Load image and get rect
        self.current_sprite = 0
        self.image = self.ruby_sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)
        
        # Add to the main group for drawing purposes
        main_group.add(self)
                
    def update(self):
        """Update the ruby maker"""
        self.animate(self.ruby_sprites, .25)
    
    def animate(self, sprite_list, speed):
        """Animate the ruby maker"""
        if self.current_sprite < len(sprite_list) - 1:
            self.current_sprite += speed
        # Start over
        else:
            self.current_sprite = 0
        
        self.image = sprite_list[int(self.current_sprite)]
        

class Ruby(pygame.sprite.Sprite):
    """A class the player must collect to earn points and health"""
    def __init__(self, platform_group, portal_group):
        """Initialize the ruby"""
        super().__init__()
        
        # Set constants
        self.vertical_acceleration = 3  # Gravity
        self.horizontal_velocity = 3
        
        # Animation frames
        self.ruby_sprites = []
        
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/ruby/tile000.png"), (50, 50)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/ruby/tile001.png"), (50, 50)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/ruby/tile002.png"), (50, 50)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/ruby/tile003.png"), (50, 50)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/ruby/tile004.png"), (50, 50)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/ruby/tile005.png"), (50, 50)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/ruby/tile006.png"), (50, 50)))
        
        # Load image and get rect
        self.current_sprite = 0
        self.image = self.ruby_sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (WINDOW_WIDTH//2, 100)
        
        # Attach sprite groups
        self.platform_group = platform_group
        self.portal_group = portal_group
        
        # Load sounds
        self.portal_sound = pygame.mixer.Sound("Assets/sounds/portal_sound.wav")
        
        # Kinematics vectors
        self.position = vector(self.rect.x, self.rect.y)
        self.velocity = vector(random.choice([-1 * self.horizontal_velocity, self.horizontal_velocity]), 0)
        self.acceleration = vector(0, self.vertical_acceleration)
            
    def update(self):
        """Update the ruby"""
        self.animate(self.ruby_sprites, .25)
        self.move()
        self.check_collisions()
    
    def move(self):
        """Move the ruby"""
        # Calculate the kinematics values
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5 * self.acceleration
            
        # Update rect based on kinematics calculations and wrap around movement
        if self.position.x < 0:
            self.position.x = WINDOW_WIDTH
        elif self.position.x > WINDOW_WIDTH:
            self.position.x = 0
                
        self.rect.bottomleft = self.position
            
    def check_collisions(self):
        """Check for collisions with platforms and portals"""
        # Collision check between roby and platforms when falling
        collided_platforms = pygame.sprite.spritecollide(self, self.platform_group, False)
        if collided_platforms:
            self.position.y = collided_platforms[0].rect.top + 1
            self.velocity.y = 0  
                    
        # Collision check with portals
        if pygame.sprite.spritecollide(self, self.portal_group, False):
            self.portal_sound.play()
            # Determine which portal you are moving to 
            # right and left
            if self.position.x > WINDOW_WIDTH//2:
                self.position.x = 86
            else:
                self.position.x = WINDOW_WIDTH - 150
                
            # Top and bottom
            if self.position.y > WINDOW_HEIGHT//2:
                self.position.y = 64
            else:
                self.position.y = WINDOW_HEIGHT - 132

            self.rect.bottomleft = self.position 

    def animate(self, sprite_list, speed):
        """Animate the ruby"""
        if self.current_sprite < len(sprite_list) - 1:
            self.current_sprite += speed
        else:
            self.current_sprite = 0
        
        self.image = sprite_list[int(self.current_sprite)]
