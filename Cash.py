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
        if cash_type == 'receipt':
            self.image = pygame.image.load("world/receipt.png").convert_alpha()
            self.info_text = "$-2000"
            self.text_color = (255, 0, 0)
        elif cash_type == 'green':
            self.image = pygame.image.load("world/green-cash.png").convert_alpha()
            self.info_text = "$5000"
            self.text_color = (0, 255, 0)
        else:
            raise ValueError("Cash type must be either 'receipt' or 'green'.")
        font = pygame.font.SysFont('sans-serif', 24, True)
        self.text = font.render(self.info_text, True, self.text_color)
        self.collect_counter = 0
        self.state = None
        self.type = cash_type
        self.rect = self.image.get_rect()
        self.rect.x = x;
        self.rect.y = y;
        self.speed = speed
        self.dx = -(2.5 * speed);
        self.dy = 0;
        
    def update(self, surface):
        self.rect.x += self.dx
        self.rect.y += self.dy
        if self.rect.x < 0:
            self.rect.x = surface.get_rect().width
        if self.collect_counter > 0:
            self.collect_counter -= 1
            if self.collect_counter <= 0:
                self.state = None
            
    def start_collect(self):
         self.state = 'collect'
         self.collect_counter = 5 * self.speed
         