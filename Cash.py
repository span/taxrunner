# This class loads and updates the cash images that make out the red & green cash that the
# running man can catch when running. The type of cash (red/green) is set as a paramter
# on instantiation.
#
# The update method simply updates the x position of the rectangle that has
# the cash image.
#
# Author: Daniel Kvist
# E-mail: danielkvist81@gmail.com
# Python version: 2.7
# OS: OS X

import pygame
from pygame.locals import *

class Cash(pygame.sprite.Sprite):
    
    def __init__(self, x, y, speed, cash_type):
        pygame.sprite.Sprite.__init__(self)
        if cash_type == 'red':
            self.image = pygame.image.load("world/red-cash.png").convert_alpha()
        elif cash_type == 'green':
            self.image = pygame.image.load("world/green-cash.png").convert_alpha()
        else:
            raise ValueError("Cash type must be either red or green.")
        self.type = cash_type
        self.rect = self.image.get_rect()
        self.rect.x = x;
        self.rect.y = y;
        self.dx = -(3 * speed);
        self.dy = 0;
        
    def update(self, surface):
        self.rect.x += self.dx
        self.rect.y += self.dy
        if self.rect.x < 0:
            self.rect.x = surface.get_rect().width
        