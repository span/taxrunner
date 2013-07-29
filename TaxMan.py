import pygame
from pygame.locals import *

class TaxMan(pygame.sprite.Sprite):
    
    def __init__(self, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("world/helicopter.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - self.rect.height
        self.dx = (3 * speed) 
        
    def update(self, surface):
        #self.rect.x += self.dx
        #if self.rect.x <= -(self.rect.width / 2):
        #    self.rect.x = -(self.rect.width / 2)
        #else:
        #    self.rect.x -= 1
        return None
                
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
        
        