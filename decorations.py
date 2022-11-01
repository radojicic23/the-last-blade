import pygame


class Decoration(pygame.sprite.Sprite):
    """A class that represent decorations"""
    def __init__(self, x, y, image_int, main_group):
        """Initialize decorations"""
        super().__init__()
        
        if image_int == 11:
            self.image = pygame.transform.scale(pygame.image.load("Assets/images/tiles/Barel.png"), (32, 34))
        elif image_int == 12:
            self.image = pygame.transform.scale(pygame.image.load("Assets/images/tiles/Bush.png"), (70, 40))
        elif image_int == 13:
            self.image = pygame.transform.scale(pygame.image.load("Assets/images/tiles/Stone.png"), (100, 80))
        elif image_int == 14:
            self.image = pygame.transform.scale(pygame.image.load("Assets/images/tiles/Flag.png"), (50, 140))
        elif image_int == 15:
            self.image = pygame.transform.scale(pygame.image.load("Assets/images/tiles/Tree.png"), (180, 140))
        elif image_int == 16:
            self.image = pygame.transform.scale(pygame.image.load("Assets/images/tiles/ArrowSign.png"), (64, 64))
        elif image_int == 17:
            self.image = pygame.transform.scale(pygame.image.load("Assets/images/tiles/Crate.png"), (32, 35))
        elif image_int == 18:
            self.image = pygame.transform.scale(pygame.image.load("Assets/images/tiles/Bush (1).png"), (64, 32))
        elif image_int == 19:
            self.image = pygame.transform.scale(pygame.image.load("Assets/images/tiles/Sign.png"), (64, 64))
        elif image_int == 20:
            self.image = pygame.transform.flip(pygame.transform.scale(pygame.image.load("Assets/images/tiles/ArrowSign.png"), (64, 64)), True, False)
        elif image_int == 21:
            self.image = pygame.transform.scale(pygame.image.load("Assets/images/tiles/Tree (1).png"), (130, 180))
        
        # Add to main group
        main_group.add(self)
        # Get rect
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
