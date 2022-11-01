import pygame

from display import WINDOW_WIDTH, WINDOW_HEIGHT
from bullet import Bullet


vector = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    """A class the user can control"""
    def __init__(self, x, y, platform_group, portal_group, bullet_group):
        """Initialize the player"""
        super().__init__()
        
        # Set constant variables
        self.horizontal_acceleration = 1.5
        self.horizontal_friction = 0.15
        self.vertical_acceleration = 0.8  # Gravity
        self.vertical_jump_speed = 18  # Determines how high the player can jump
        self.starting_health = 100
        
        # Animation frames
        self.move_right_sprites = []
        self.move_left_sprites = []
        self.idle_right_sprites = []
        self.idle_left_sprites = []
        self.jump_right_sprites = []
        self.jump_left_sprites = []
        self.attack_right_sprites = []
        self.attack_left_sprites = []
        
        # Moving animation 
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/player/run/Run (1).png"), (90, 90)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/player/run/Run (2).png"), (90, 90)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/player/run/Run (3).png"), (90, 90)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/player/run/Run (4).png"), (90, 90)))
        
        for sprite in self.move_right_sprites:
            self.move_left_sprites.append(pygame.transform.flip(sprite, True, False))
        
        # Idle animation
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/player/idle/Idle (1).png"), (90, 90)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/player/idle/Idle (2).png"), (90, 90)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/player/idle/Idle (3).png"), (90, 90)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/player/idle/Idle (4).png"), (90, 90)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/player/idle/Idle (5).png"), (90, 90)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/player/idle/Idle (6).png"), (90, 90)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/player/idle/Idle (7).png"), (90, 90)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/player/idle/Idle (8).png"), (90, 90)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/player/idle/Idle (9).png"), (90, 90)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/player/idle/Idle (10).png"), (90, 90)))
        
        for sprite in self.idle_right_sprites:
            self.idle_left_sprites.append(pygame.transform.flip(sprite, True, False))
        
        # Jumping animation
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/player/jump/Jump (1).png"), (55, 90)))
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/player/jump/Jump (2).png"), (55, 90)))
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/player/jump/Jump (3).png"), (55, 90)))
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/player/jump/Jump (4).png"), (55, 90)))
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/player/jump/Jump (5).png"), (55, 90)))
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/player/jump/Jump (6).png"), (55, 90)))
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/player/jump/Jump (7).png"), (55, 90)))
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/player/jump/Jump (8).png"), (55, 90)))
        
        for sprite in self.jump_right_sprites:
            self.jump_left_sprites.append(pygame.transform.flip(sprite, True, False))
        
        # Attacking animation
        self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/player/attack/Attack (1).png"), (110, 90)))
        self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/player/attack/Attack (2).png"), (110, 90)))
        self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/player/attack/Attack (3).png"), (110, 90)))
        self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/player/attack/Attack (4).png"), (110, 90)))
        self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/player/attack/Attack (5).png"), (110, 90)))
        self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/player/attack/Attack (6).png"), (110, 90)))
        self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load("Assets/images/player/attack/Attack (7).png"), (110, 90)))
        
        for sprite in self.attack_right_sprites:
            self.attack_left_sprites.append(pygame.transform.flip(sprite, True, False))
        
        # Load image and get rect 
        self.current_sprite = 0 
        self.image = self.idle_right_sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)
        
        # Attach sprite groups
        self.platform_group = platform_group
        self.portal_group = portal_group
        self.bullet_group = bullet_group
        
        # Animation booleans
        self.animate_jump = False
        self.animate_fire = False
        
        # Load sounds
        self.jump_sound = pygame.mixer.Sound("Assets/sounds/jump_sound.wav")
        self.slash_sound = pygame.mixer.Sound("Assets/sounds/slash_sound.wav")
        self.portal_sound = pygame.mixer.Sound("Assets/sounds/portal_sound.wav")
        self.hit_sound = pygame.mixer.Sound("Assets/sounds/player_hit.wav")
        
        # Kinematics vectors
        self.position = vector(x, y)
        self.velocity = vector(0, 0)
        self.acceleration = vector(0, self.vertical_acceleration)
        
        # Set initial game values
        self.health = self.starting_health
        self.starting_x = x
        self.starting_y = y 
        
    def update(self):
        """Update the player"""
        self.move()
        self.check_collisions()
        self.check_animations()
        
        # Update player mask
        self.mask = pygame.mask.from_surface(self.image)
    
    def move(self):
        """Move the player"""
        # Set the acceleration vector 
        self.acceleration = vector(0, self.vertical_acceleration)
        
        # If the user is pressing a key, set the x - component of the acceleration to be non-zero
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acceleration.x = -1 * self.horizontal_acceleration
            self.animate(self.move_left_sprites, .20)
        elif keys[pygame.K_RIGHT]:
            self.acceleration.x = self.horizontal_acceleration
            self.animate(self.move_right_sprites, .20)
        else:
            if self.velocity.x > 0:
                self.animate(self.idle_right_sprites, .20)
            else:
                self.animate(self.idle_left_sprites, .20)
            
        # Calculate new kinematics values
        self.acceleration.x -= self.velocity.x * self.horizontal_friction
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5 * self.acceleration
        
        # Update rect based on kinematics calculation and add wrap around movement
        if self.position.x < 0:
            self.position.x = WINDOW_WIDTH
        elif self.position.x > WINDOW_WIDTH:
            self.position.x = 0
            
        self.rect.bottomleft = self.position
        
    def check_collisions(self):
        """Check for collisions with platforms and portals"""
        # Collision check between player and platforms when falling
        if self.velocity.y > 0:
            collided_platforms = pygame.sprite.spritecollide(self, self.platform_group, False, pygame.sprite.collide_mask)
            if collided_platforms:
                self.position.y = collided_platforms[0].rect.top + 1
                self.velocity.y = 0  
        
        # Collision check between player and platform if jumping up
        if self.velocity.y < 0:
            collided_platforms = pygame.sprite.spritecollide(self, self.platform_group, False, pygame.sprite.collide_mask)
            if collided_platforms:
                self.velocity.y = 0
                while pygame.sprite.spritecollide(self, self.platform_group, False):
                    self.position.y += 1
                    self.rect.bottomleft = self.position
                    
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
        """Check to see if jump/fire animations should run"""
        # Animate the player jump
        if self.animate_jump:
            if self.velocity.x > 0:
                self.animate(self.jump_right_sprites, .0005)
            else:
                self.animate(self.jump_left_sprites, .0005)
        
        # Animate the player attack
        if self.animate_fire:
            if self.velocity.x > 0:
                self.animate(self.attack_right_sprites, .005)
            else:
                self.animate(self.attack_left_sprites, .005)
    
    def jump(self):
        """Jump upwards if on a platform"""
        # Only jump if on a plarform 
        if pygame.sprite.spritecollide(self, self.platform_group, False):
            self.jump_sound.play()
            self.velocity.y = -1 * self.vertical_jump_speed
            self.animate_jump = True
    
    def fire(self):
        """Fire a 'bullet' from a sword"""
        self.slash_sound.play()
        Bullet(self.rect.centerx, self.rect.centery, self.bullet_group, self)
        self.animate_fire = True
    
    def reset(self):
        """Reset the players position"""
        self.velocity = vector(0, 0)
        self.position = vector(self.starting_x, self.starting_y)
        self.rect.bottomleft = self.position
    
    def animate(self, sprite_list, speed):
        """Animate the players actions"""
        if self.current_sprite < len(sprite_list) - 1:
            self.current_sprite += speed
        # Start over
        else:
            self.current_sprite = 0
            # End the jump animation
            if self.animate_jump:
                self.animate_jump = False
                
            # End the attack animation
            if self.animate_fire:
                self.animate_fire = False
                
        self.image = sprite_list[int(self.current_sprite)]
