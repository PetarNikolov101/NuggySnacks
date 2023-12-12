import pygame
from pygame.sprite import Sprite

class Platforms(Sprite):
    def __init__(self):
        pygame.init()
        super().__init__()
        self.image = pygame.image.load('images/platform.png')
        self.rect = self.image.get_rect()