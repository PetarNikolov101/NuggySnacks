import pygame
from pygame.sprite import Sprite
from settings import Settings

class Nuggy(Sprite):
    def __init__(self, bomnigaem):       
        self.screen = bomnigaem.screen
        self.screen_rect = bomnigaem.screen_rect
        self.settings = Settings()
        
        self.image = pygame.image.load('images/nuggystand_red.bmp').convert_alpha()
        self.flipped = pygame.image.load('images/flipped.bmp').convert_alpha()
        self.sitting = pygame.image.load('images/nuggysit.bmp').convert_alpha()
        self.rect = self.image.get_rect()
        self.ground = self.settings.screen_height 
        self.rect.midbottom = self.screen_rect.midbottom
        
        self.movingRight = False
        self.movingLeft = False
        
        self.is_jumping = False
        self.speed = self.settings.nugget_speed
        self.jump_height = self.settings.nugget_jump_height
        
    def update(self):
        if self.is_jumping:
            self.jump()
        if self.movingRight and self.rect.right < self.screen_rect.right:
            self.rect.x += self.speed
        if self.movingLeft and self.rect.left > 0:
            self.rect.x -= self.speed

    
    def jump(self):
        if self.jump_count >= -self.jump_height:
            neg = 1
            if self.jump_count < 0:
                neg = -1
            self.rect.y -= (self.jump_count ** 2) * 0.5 * neg
            self.jump_count -= 1

            # Ensure the character stays within the screen boundaries
            # self.rect.y = max(self.rect.y, 0)
        else:
            # If jump_count is less than -self.jump_height, stop jumping
            self.is_jumping = False
            self.jump_count = self.jump_height

    def start_jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.jump_count = self.jump_height
    
    def blitme(self):
        if not self.movingLeft and not self.movingRight or (self.movingRight and self.movingLeft):
            self.screen.blit(self.sitting, self.rect)
        self.sitting.set_colorkey((248, 182, 204))
        if self.movingRight and not self.movingLeft:
            self.screen.blit(self.image, self.rect)
        self.image.set_colorkey((248, 182, 204))
        if self.movingLeft and not self.movingRight:
            self.screen.blit(self.flipped, self.rect)
        self.flipped.set_colorkey((248, 182, 204))