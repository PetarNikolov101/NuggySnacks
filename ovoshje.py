import pygame
from pygame.sprite import Sprite
import random
from settings import Settings

class Ovoshje(Sprite):
    def __init__(self, bomnigaem):
        super().__init__()
        self.banana = pygame.image.load('images/banana1.bmp')
        self.jagoda = pygame.image.load('images/jagoda1.bmp')
        self.jabolko = pygame.image.load('images/jabolko1.bmp')
        self.lubenche = pygame.image.load('images/lubenche1.bmp')
        self.settings = Settings()
        
        self.screen = bomnigaem.screen
        self.screen_rect = bomnigaem.screen_rect
        self.speed = self.settings.ovoshe_speed
        self.is_outside_screen = False
        
        self.fruit_type = random.choice([self.banana, self.jagoda, self.jabolko, self.lubenche])
        
        self.image = self.fruit_type
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.width 
        self.x = float(self.rect.x)  
           
    def update(self):
        self.rect.x += self.speed  
        self.image.set_colorkey((121, 211, 239))
            

            
        
        