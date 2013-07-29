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
    
    def __init__(self, game):
        self.finished = False
        self.sprites = pygame.sprite.Group()
        self.surface = game.surface
        self.speed = game.speed
        self.surface_rect = self.surface.get_rect()
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
        self.red_cash = Cash(self.surface_rect.width, self.y - 50, self.speed * 1.5, 'red')
        self.sprites.add(self.green_cash)
        self.sprites.add(self.red_cash)
        self.player = Player(self.start_pos_x, 0, self.speed)
        self.taxman = TaxMan(50, 100, self.speed)
        self.sprites.add(self.taxman)
       
    def update(self, up):
        self.background.update()
        self.sprites.update(self.surface)
        self.player.update(up)
        self.player.collide(self.sprites, self.surface)

        if self.player.rect.y > self.surface_rect.height:
            self.player.state = 'busted'
        
    def draw(self):
        self.background.draw(self.surface)
        self.sprites.draw(self.surface)
        self.player.draw(self.surface)   
    
    def end():
        self.game.show_resul
    
    def respawn(self):
        self.player = Player(self.start_pos_x, self.start_pos_y, self.speed)
        
    def get_score(self):
        return self.player.score.get_score()