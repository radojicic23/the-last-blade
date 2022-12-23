import pygame


# Set display surface (tile size is 32x32 so 1280/32 = 40 tiles wide, 736/32 = 23 tiles high)
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 736
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
game_icon = pygame.image.load("Assets/icon.png")
pygame.display.set_caption("The Last Blade")
pygame.display.set_icon(game_icon)
