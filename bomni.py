import pygame
import sys
from settings import Settings
from nuggy import Nuggy
from ovoshje import Ovoshje
import random
import pygame.font
from button import Button
        
class Bomni:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.game_active = False
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Bomni")
        self.font = pygame.font.Font(None, 36)
        self.screen_rect = self.screen.get_rect()
        self.background = pygame.image.load('images/pink_background.webp')
        self.collect_sound = pygame.mixer.Sound('sound effects/mixkit-game-ball-tap-2073.wav')
        
        self.restart_button = Button(self, "Restart")
        self.nuggy = Nuggy(self)
        self.ovoshje = Ovoshje(self)
        self.ovoshje_grupa = pygame.sprite.Group()
        self.ovoshje_grupa.add(self.ovoshje)
        self.createFruits()
        self.ovoshje_speed = self.settings.ovoshe_speed
        
        self.clock = pygame.time.Clock()
        
    def collect_fruit(self):
        fruit_collisions = pygame.sprite.spritecollide(self.nuggy, self.ovoshje_grupa, True)
        for fruit in fruit_collisions:
            self.settings.score += 1
            pygame.mixer.Sound.play(self.collect_sound)
            self.createFruits()
            if self.settings.score >= 20:
                self.ovoshje_speed = random.randrange(10,15)
            else:
                self.ovoshje_speed = random.randrange(4, 9)
           
            
            
    def createFruits(self):
    # Check if all fruits in the group are outside the screen
        if all(fruit.is_outside_screen for fruit in self.ovoshje_grupa): 
        # Determine which side of the screen the fruits will appear on
            side = random.choice(['left', 'right'])
        
            fruit = Ovoshje(self)  # Create a new fruit
            fruit_width = fruit.rect.width
            fruit_height = fruit.rect.height

            if side == 'left':
                fruit.speed = abs(self.ovoshje_speed)  
                fruit.x = 0 - fruit_width
                fruit.rect.x = fruit.x
                fruit.rect.y = random.randint(0, self.settings.screen_height - fruit_height)
            elif side == 'right':
                fruit.speed = -abs(self.ovoshje_speed)  
                fruit.x = self.settings.screen_width
                fruit.rect.x = fruit.x
                fruit.rect.y = random.randint(0, self.settings.screen_height - fruit_height)
            self.ovoshje_grupa.add(fruit)

    def show_score(self):
        score_text = self.font.render(f"Score: {self.settings.score}", True, (0, 0, 0))
        score_rect = score_text.get_rect()
        score_rect.centerx = self.screen_rect.centerx
        score_rect.top = 30  # Adjust the top position as needed
        self.screen.blit(score_text, score_rect)

    def check_play_button(self, mouse_pos):
        if self.restart_button.rect.collidepoint(mouse_pos):
            self.game_active = True
            self.settings.score = 0
            self.createFruits()
                        
    def _check_events(self):        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.nuggy.movingRight = True
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.nuggy.movingLeft = True
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.nuggy.start_jump()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.nuggy.movingRight = False
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.nuggy.movingLeft = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_play_button(mouse_pos)
                                                                                  
    def _update_screen(self):        
        self.restart_button.draw_button()
        self.nuggy.blitme()
        self.ovoshje_grupa.draw(self.screen)
        self.show_score()
        pygame.display.flip()

    def run_game(self):
        while True:
            self.clock.tick(60)
            self.screen.blit(self.background, (0, 0))
            self._check_events()
            self.nuggy.update()
            self.collect_fruit()    
            self.ovoshje_grupa.update()
            self._update_screen()
            
    
if __name__ == '__main__':
    bomni = Bomni()
    bomni.run_game()    
        
    
