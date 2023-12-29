import pygame
from settings import Settings

class Button:
    def __init__(self, bomnigaem, msg):
        self.screen = bomnigaem.screen
        self.screen_rect = self.screen.get_rect()
        
        self.width, self.height = 75, 27
        self.button_color = (255, 182, 193)
        self.text_color = (0, 0, 0)
        self.settings = Settings
        self.font = pygame.font.Font("fonts\\Summer Beauty.otf", 30)
        
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x = 850
        self.rect.y = 13
        
        self.prep_msg(msg)
        
    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        
    
