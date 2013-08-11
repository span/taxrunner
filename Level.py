# This class contains the level sprites that we see on the screen. When this class is
# instantiated it draws a level of bricks, adds a player, taxman, background and cash. This
# class is then called from the main game loop through the update method. These calls are
# then propagated to the proper sprite classes as necessary.
#
# Author: Daniel Kvist
# E-mail: danielkvist81@gmail.com
# Python version: 2.7
# OS: OS X

import pygame
from pygame.locals import *
from random import *
from Background import Background
from Brick import Brick
from Cash import Cash
from Player import Player
from TaxMan import TaxMan

class Level():
    
    start_pos_y  = 600
    start_pos_x = 600
    bricks = 24
    
    # Loads and initiates the level
    def __init__(self, game):
        self.finished = False
        self.sprites = pygame.sprite.Group()
        self.surface = game.surface
        self.speed = game.speed
        self.surface_rect = self.surface.get_rect()
        self.center = (self.surface_rect.width / 2, self.surface_rect.height / 2)
        self.background = Background(self.speed)
        self.heightfactor = 0
        self.x = 0
        self.y = 0

        for i in range(0, self.bricks):
            self.x = i * Brick.width
            if i % 4 == 0:
                self.x += Brick.width / 2
                if self.heightfactor == 4:
                    self.heightfactor -= 2
                else:
                    self.heightfactor += 1
            self.y = self.start_pos_y - (50 * self.heightfactor)
            brick = Brick(self.x, self.y, self.speed, self.bricks)
            self.sprites.add(brick)
            
        self.green_cash = Cash(self.surface_rect.width, self.y - 70, self.speed, 'green')    
        self.receipt = Cash(self.surface_rect.width, self.y - 50, self.speed * 1.5, 'receipt')
        self.sprites.add(self.green_cash)
        self.sprites.add(self.receipt)
        self.player = Player(self.start_pos_x, 0, self.speed)
        self.taxman = TaxMan(50, 100, self.speed)
        self.sprites.add(self.taxman)
      
    # Updates the sprite positions 
    def update(self, up):
        self.background.update()
        self.sprites.update(self.surface)
        self.player.update(up)
        self.player.collide(self.sprites, self.surface)

        if self.player.rect.y > self.surface_rect.height:
            self.player.state = 'busted'
    
    # Draws the sprites  
    def draw(self):
        self.background.draw(self.surface)
        self.sprites.draw(self.surface)
        self.player.draw(self.surface)
        
        # If we hit some cash during the update phase, draw cash info to screen
        if self.receipt.state == 'collect':
            self.surface.blit(self.receipt.text, self.center)
        if self.green_cash.state == 'collect':
            self.surface.blit(self.green_cash.text, self.center)
        
    def get_score(self):
        return self.player.score.get_score()