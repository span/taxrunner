import pygame
from pygame.locals import *

class Brick(pygame.sprite.Sprite):
    
    width = 150
    height = 25
    
    def __init__(self, x, y, speed, bricks):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("world/brick.png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dx = -(3 * speed)
        self.bricks = bricks
        
    def update(self, surface):
        self.rect.x += self.dx
        if self.rect.x < -self.width:
            self.rect.x += self.bricks * self.width
        