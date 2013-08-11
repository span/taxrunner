# This class contains the game intro which displays a simple story background
# and then returns control to the calling method.
#
# If the user presses 'enter', 'menu' will be returned as the next state. Otherwise
# the intro will complete and return 'game' to launch the gameplay.
#
# Author: Daniel Kvist
# Modified from https://gist.github.com/rshk/5072375
# E-mail: danielkvist81@gmail.com
# Python version: 2.7
# OS: OS X

import sys
import time
import pygame
from pygame.locals import *

class Intro():
    
    global FADE_IN_EASING
    global FADE_OUT_EASING
    
    FADE_IN_TIME = 3
    FADE_OUT_TIME = 2
    FADE_IN_EASING = lambda x: x # Linear
    FADE_OUT_EASING = lambda x: x # Linear
    ST_FADEIN = 0
    ST_FADEOUT = 1
    FPS = 60
    
    def __init__(self, pygame, surface):
        self.texts = ["TaxRunner", 
                      "You've been manipulating taxes for years, but now they are coming to get you...",
                      "Collect as much green while you can and watch out for traps and receipts...",
                      "Uh oh, here they are, RUN!!!!!!!!!! (JUMP with UP arrow)"]
        self.textframe = 0
        self.surface = surface
        self.pygame = pygame
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('sans-serif', 160, True)
        self.text = self.font.render(self.texts[self.textframe], True, (255, 0, 0))
        self.text_rect = self.text.get_rect(center=(surface.get_rect().width / 2, surface.get_rect().height / 2))
        self.state = self.ST_FADEIN
        self.last_state_change = time.time()
        
    def show(self):
        while True:
            # Check for quit event 
            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT:
                    self.pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN and event.key == K_RETURN:
                    return 'menu'
                
            # Calculate time and check what state we should be in
            state_time = time.time() - self.last_state_change 
            if self.state == self.ST_FADEIN:
                if state_time >= self.FADE_IN_TIME:
                    self.state = self.ST_FADEOUT
                    state_time -= self.FADE_IN_TIME
                    self.last_state_change = time.time() - state_time
            elif self.state == self.ST_FADEOUT:
                if state_time >= self.FADE_OUT_TIME:
                    self.textframe += 1
                    if self.textframe < 4:
                        # We have faded out, update text
                        self.font = self.pygame.font.SysFont('sans-serif', 32, True)
                        self.text = self.font.render(self.texts[self.textframe], True, (255, 0, 0))
                        self.text_rect = self.text.get_rect(center = (self.surface.get_rect().width / 2, self.surface.get_rect().height / 2))
                        self.state = self.ST_FADEIN
                        state_time -= self.FADE_OUT_TIME
                        self.last_state_change = time.time() - state_time
                    else:
                        # Intro is finished, lets return
                        return 'game'
            else:
                raise ValueError()
 
            # Calculate alpha values
            if self.state == self.ST_FADEIN:
                alpha = FADE_IN_EASING(1.0 * state_time / self.FADE_IN_TIME)
            elif self.state == self.ST_FADEOUT:
                alpha = 1. - FADE_OUT_EASING(1.0 * state_time / self.FADE_OUT_TIME)
            else:
                raise ValueError()
 
            # Create surface with faded alpha values
            surf2 = self.pygame.surface.Surface((self.text_rect.width, self.text_rect.height))
            surf2.set_alpha(255 * alpha)
 
            # Blit and draw
            self.surface.fill((0, 0, 0))
            surf2.blit(self.text, (0, 0))
            self.surface.blit(surf2, self.text_rect)
 
            self.pygame.display.flip()
            self.clock.tick(self.FPS)
            