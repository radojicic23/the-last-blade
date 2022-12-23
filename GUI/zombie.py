import pygame, random

from GUI.display import WINDOW_WIDTH, WINDOW_HEIGHT


vector = pygame.math.Vector2
FPS = 60


class Zombie(pygame.sprite.Sprite):
    """An enemy class that moves across the screen"""
    def __init__(self, platform_group, portal_group, min_speed, max_speed):
        """Initialize the zombie"""
        super().__init__()
        
        # Set constants
        self.vertical_acceleration = 2  # Gravity
        self.rise_time = 3
        
        # Animation frames
        self.walk_right_sprites = []
        self.walk_left_sprites = []
        self.die_right_sprites = []
        self.die_left_sprites = []
        self.rise_right_sprites = []
        self.rise_left_sprites = []
        
        # Pick a gender 
        gender = random.randint(0, 1)
        if gender == 0:
            # Walking 
            self.walk_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/boy/walk/Walk (1).png"), (64, 64)))
            self.walk_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/boy/walk/Walk (2).png"), (64, 64)))
            self.walk_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/boy/walk/Walk (3).png"), (64, 64)))
            self.walk_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/boy/walk/Walk (4).png"), (64, 64)))
            self.walk_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/boy/walk/Walk (5).png"), (64, 64)))
            self.walk_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/boy/walk/Walk (6).png"), (64, 64)))
            self.walk_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/boy/walk/Walk (7).png"), (64, 64)))
            self.walk_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/boy/walk/Walk (8).png"), (64, 64)))
            self.walk_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/boy/walk/Walk (9).png"), (64, 64)))
            self.walk_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/boy/walk/Walk (10).png"), (64, 64)))
            
            for sprite in self.walk_right_sprites:
                self.walk_left_sprites.append(pygame.transform.flip(sprite, True, False))
                
            # Dying
            self.die_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/boy/dead/Dead (1).png"), (64, 64)))
            self.die_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/boy/dead/Dead (2).png"), (64, 64)))
            self.die_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/boy/dead/Dead (3).png"), (64, 64)))
            self.die_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/boy/dead/Dead (4).png"), (64, 64)))
            self.die_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/boy/dead/Dead (5).png"), (64, 64)))
            self.die_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/boy/dead/Dead (6).png"), (64, 64)))
            self.die_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/boy/dead/Dead (7).png"), (64, 64)))
            self.die_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/boy/dead/Dead (8).png"), (64, 64)))
            self.die_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/boy/dead/Dead (9).png"), (64, 64)))
            self.die_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/boy/dead/Dead (10).png"), (64, 64)))
            
            for sprite in self.die_right_sprites:
                self.die_left_sprites.append(pygame.transform.flip(sprite, True, False))  
                
            # Rising
            self.rise_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/boy/dead/Dead (10).png"), (64, 64)))
            self.rise_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/boy/dead/Dead (9).png"), (64, 64)))
            self.rise_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/boy/dead/Dead (8).png"), (64, 64)))
            self.rise_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/boy/dead/Dead (7).png"), (64, 64)))
            self.rise_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/boy/dead/Dead (6).png"), (64, 64)))
            self.rise_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/boy/dead/Dead (5).png"), (64, 64)))
            self.rise_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/boy/dead/Dead (4).png"), (64, 64)))
            self.rise_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/boy/dead/Dead (3).png"), (64, 64)))
            self.rise_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/boy/dead/Dead (2).png"), (64, 64)))
            self.rise_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/boy/dead/Dead (1).png"), (64, 64)))
            
            for sprite in self.rise_right_sprites:
                self.rise_left_sprites.append(pygame.transform.flip(sprite, True, False))  
        else:
            # Walking 
            self.walk_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/girl/walk/Walk (1).png"), (64, 64)))
            self.walk_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/girl/walk/Walk (2).png"), (64, 64)))
            self.walk_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/girl/walk/Walk (3).png"), (64, 64)))
            self.walk_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/girl/walk/Walk (4).png"), (64, 64)))
            self.walk_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/girl/walk/Walk (5).png"), (64, 64)))
            self.walk_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/girl/walk/Walk (6).png"), (64, 64)))
            self.walk_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/girl/walk/Walk (7).png"), (64, 64)))
            self.walk_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/girl/walk/Walk (8).png"), (64, 64)))
            self.walk_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/girl/walk/Walk (9).png"), (64, 64)))
            self.walk_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/girl/walk/Walk (10).png"), (64, 64)))
            
            for sprite in self.walk_right_sprites:
                self.walk_left_sprites.append(pygame.transform.flip(sprite, True, False))
                
            # Dying
            self.die_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/girl/dead/Dead (1).png"), (64, 64)))
            self.die_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/girl/dead/Dead (2).png"), (64, 64)))
            self.die_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/girl/dead/Dead (3).png"), (64, 64)))
            self.die_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/girl/dead/Dead (4).png"), (64, 64)))
            self.die_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/girl/dead/Dead (5).png"), (64, 64)))
            self.die_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/girl/dead/Dead (6).png"), (64, 64)))
            self.die_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/girl/dead/Dead (7).png"), (64, 64)))
            self.die_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/girl/dead/Dead (8).png"), (64, 64)))
            self.die_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/girl/dead/Dead (9).png"), (64, 64)))
            self.die_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/girl/dead/Dead (10).png"), (64, 64)))
            
            for sprite in self.die_right_sprites:
                self.die_left_sprites.append(pygame.transform.flip(sprite, True, False))  
                
            # Rising
            self.rise_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/girl/dead/Dead (10).png"), (64, 64)))
            self.rise_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/girl/dead/Dead (9).png"), (64, 64)))
            self.rise_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/girl/dead/Dead (8).png"), (64, 64)))
            self.rise_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/girl/dead/Dead (7).png"), (64, 64)))
            self.rise_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/girl/dead/Dead (6).png"), (64, 64)))
            self.rise_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/girl/dead/Dead (5).png"), (64, 64)))
            self.rise_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/girl/dead/Dead (4).png"), (64, 64)))
            self.rise_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/girl/dead/Dead (3).png"), (64, 64)))
            self.rise_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/girl/dead/Dead (2).png"), (64, 64)))
            self.rise_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/zombie/girl/dead/Dead (1).png"), (64, 64)))
            
            for sprite in self.rise_right_sprites:
                self.rise_left_sprites.append(pygame.transform.flip(sprite, True, False))
        
        # Load an image and get rect
        self.direction = random.choice([-1, 1])
        
        self.current_sprite = 0
        if self.direction == -1:
            self.image = self.walk_left_sprites[self.current_sprite]
        else:
            self.image = self.walk_right_sprites[self.current_sprite]
            
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (random.randint(100, WINDOW_WIDTH - 100), -100)
        
        # Attach sprite groups
        self.platform_group = platform_group
        self.portal_group = portal_group
        
        # Animation booleans
        self.animate_death = False
        self.animate_rise = False
        
        # Load sounds
        self.hit_sound = pygame.mixer.Sound("Assets/sounds/zombie_hit.wav")
        self.kick_sound = pygame.mixer.Sound("Assets/sounds/zombie_kick.wav")
        self.portal_sound = pygame.mixer.Sound("Assets/sounds/portal_sound.wav")
        
        # Kinematics
        self.position = vector(self.rect.x, self.rect.y)
        self.velocity = vector(self.direction * random.randint(min_speed, max_speed), 0)
        self.acceleration = vector(0, self.vertical_acceleration)
        
        # Initial zombie values
        self.is_dead = False
        self.round_time = 0
        self.frame_count = 0 
                        
    def update(self):
        """Update the zombie"""
        self.move()
        self.check_collisions()
        self.check_animations()
        
        # Determine when the zombie should rise from the death
        if self.is_dead:
            self.frame_count += 1
            if self.frame_count % FPS == 0:
                self.round_time += 1
                if self.round_time == self.rise_time:
                    self.animate_rise = True
                    # When the zombie died, the image was kept as the last image
                    # When it rises, we want to start at index 0 of rise_sprite lists
                    self.current_sprite = 0
                    
    def move(self):
        """Move the zombie"""
        # We don't need to update the acceleration vector because it never changes
        if not self.is_dead:
            if self.direction == -1:
                self.animate(self.walk_left_sprites, .25)
            else:
                self.animate(self.walk_right_sprites, .25)
            
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
        # Collision check between zombie and platforms when falling
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
        
    def check_animations(self):
        """Check to see if death/rise animations should run"""
        # Animate the zombie death
        if self.animate_death:
            if self.direction == 1:
                self.animate(self.die_right_sprites, .095)
            else:
                self.animate(self.die_left_sprites, .095)
        
        # Animate the zombie rise 
        if self.animate_rise:
            if self.direction == 1:
                self.animate(self.rise_right_sprites, .1)
            else:
                self.animate(self.rise_left_sprites, .1)
    
    def animate(self, sprite_list, speed):
        """Animate the zombies actions"""
        if self.current_sprite < len(sprite_list) - 1:
            self.current_sprite += speed
        # Start over
        else:
            self.current_sprite = 0
            # End the death animation
            if self.animate_death:
                self.current_sprite = len(sprite_list) - 1
                self.animate_death = False
            
            # End the rise animation
            if self.animate_rise:
                self.animate_rise = False
                self.is_dead = False
                self.frame_count = 0
                self.round_time = 0
        
        self.image = sprite_list[int(self.current_sprite)]
