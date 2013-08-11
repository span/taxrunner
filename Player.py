# This is the player class which handles the animation of the character when he
# runs and jumps. It also handles some hit-tests and collision calculations to find
# when the player has run into some cash.
#
# Updates are done in the update method that is called from the level.
#
# Author: Daniel Kvist
# E-mail: danielkvist81@gmail.com
# Python version: 2.7
# OS: OS X

import pygame
from pygame.locals import *
from Brick import Brick
from Cash import Cash
from Score import Score
from TaxMan import TaxMan

class Player(pygame.sprite.Sprite):
    
    def __init__(self, x, y, speed):
        self.image = pygame.image.load("actions/crook-0.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - self.rect.height
        self.dx = 0
        self.dy = 0
        self.jumping = False
        self.colliding = False
        self.speed = speed
        self.score = Score()
        self.state = 'free'
        self.running_sound = pygame.mixer.Sound('data/step.ogg')
        self.running_sound.set_volume(0.2)
        self.channel = None
        self.frame = 0
        self.images =   ["actions/crook-0.png","actions/crook-1.png",
                         "actions/crook-2.png", "actions/crook-3.png",
                         "actions/crook-4.png", "actions/crook-5.png",
                         "actions/crook-6.png", "actions/crook-7.png"]
        
        
    def update(self, up):
        # Jump!
        if up == True and self.jumping  == False and self.colliding == True:
            self.dy = -(self.rect.height / 4)
            self.jumping = True
        
        # Gravity
        if self.jumping == True:
            self.dy += 1.2
            self.rect.y += self.dy
        # Falling
        elif self.colliding == False:
            self.dy += 0.5
            self.rect.y += self.dy  
        # Running
        else:
            if self.channel == None or self.channel.get_busy() == False:
                self.channel = self.running_sound.play()
            self.image = pygame.image.load(self.images[self.frame]).convert_alpha()
            self.frame += 1
            if self.frame == 8:
                self.frame = 0
                
        # As long as we're free we get score points!
        if self.state == 'free':
            self.score.update()
        
    # Tests collisions with cash and bricks.    
    def collide(self, sprites, surface):
        self.colliding = False
        collision_sprites = pygame.sprite.spritecollide(self, sprites, False)
        for sprite in collision_sprites:
            if isinstance(sprite, Cash):
                sprite.start_collect()
                sprite.rect.x += 2 * surface.get_rect().width
                if sprite.type == 'receipt':
                    self.score.add_score(-2000)
                elif sprite.type == 'green':
                    self.score.add_score(5000)
            elif isinstance(sprite, Brick):
                if self.rect.bottom <= (sprite.rect.top + self.dy):
                    self.rect.y -= self.dy
                    self.dy = 0
                    self.colliding = True
                    self.jumping = False
                
    def draw(self, surface):
        if self.state == 'free':
            surface.blit(self.image, (self.rect.x, self.rect.y))
        
        