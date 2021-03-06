# This class loads and updates the background image of the application. To
# keep a continious background, it's painted twice next to each other outside
# of the screen.
#
# The update method simply updates the x position of the rectangle that has
# the image.
#
# Author: Daniel Kvist
# E-mail: danielkvist81@gmail.com
# Python version: 2.7
# OS: OS X

import pygame
from pygame.locals import *

class Background():
    
    def __init__(self, speed):
        self.image = pygame.image.load("world/skyline.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.x1 = 0
        self.x2 = self.rect.width
        self.y1 = 0
        self.y2 = 0
        self.dx = -speed
        
    def update(self):
        self.x1 += self.dx
        self.x2 += self.dx
        if self.x1 < -self.rect.width:
            self.x1 = 0
            self.x2 = self.rect.width
            
    def draw(self, surface):
        surface.blit(self.image, (self.x1, self.y1))
        surface.blit(self.image, (self.x2, self.y2))

        