# This is the taxman class that displays the taxman's helicopter. It shows a simple
# animation when the level is updated.
#
# Author: Daniel Kvist
# E-mail: danielkvist81@gmail.com
# Python version: 2.7
# OS: OS X

import pygame
from pygame.locals import *

class TaxMan(pygame.sprite.Sprite):
    
    def __init__(self, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.frame_delay = 4
        self.images = ["actions/helicopter-0.png", "actions/helicopter-1.png",
                       "actions/helicopter-2.png", "actions/helicopter-3.png"]
        self.image = pygame.image.load(self.images[0]).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - self.rect.height
        
    def update(self, surface):
        self.frame += 1
        
        # Load the image each time frame is divided by 8 (2 * 4 if frame delay is 4) 
        self.image = pygame.image.load(self.images[self.frame / (2 * self.frame_delay)]).convert_alpha() 

        # If the frame number is 31 ((4 * (2 * 4)) - 1) with frame delay 4, we reset the frame to 0
        if self.frame == (self.frame_delay * (2 * self.frame_delay)) - 1:    
            self.frame = 0
        return None
                
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
        
        