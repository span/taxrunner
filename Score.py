# This is the scoring class that reads and writes high scores to a file. It also keeps
# track of the players current score. This class can also be used to get printable strings
# to print the menu.
#
# Author: Daniel Kvist
# E-mail: danielkvist81@gmail.com
# Python version: 2.7
# OS: OS X

import csv
import os
import pygame
from pygame.locals import *

class Score():
    
    global HISCORE_FILE
    global WHITE
    
    HISCORE_FILE = 'data/hiscore'
    WHITE = (255, 255, 255)
    
    def __init__(self):
        self.score = 0
        self.scoreIncrementTimer = 0
        self.lastFrameTicks = 0
        
    def add_score(self, score):
        self.score += score
        
    def update(self):
        thisFrameTicks = pygame.time.get_ticks()
        ticksSinceLastFrame = thisFrameTicks - self.lastFrameTicks
        self.lastFrameTicks = thisFrameTicks
        self.scoreIncrementTimer = self.scoreIncrementTimer + ticksSinceLastFrame
        if self.scoreIncrementTimer > 100:
            self.score = self.score + 100
            self.scoreIncrementTimer = 0
        
    def get_score(self):
        return self.score;
        
    @staticmethod
    def is_highscore(score, hiscores):
        for hiscore in hiscores:
            if score > int(hiscore[1]):
                return True
    
    @staticmethod
    def read_high_score():
        hiscores = []
        try:
            with open(HISCORE_FILE, 'rb') as file:
                reader = csv.reader(file)
                for row in reader:
                    hiscores.append(row)
        except EnvironmentError as e:
            print "Could not open highscore file to read highscores."
            
        return hiscores
        
    @staticmethod
    def get_high_score_text(hiscore):
        text = ''
        text += hiscore[0]
        text += ' '
        text += hiscore[1]
        return text
        
    @staticmethod
    def draw_high_scores(hiscores, surface):
        current_line = -1
        line_height = 24
        font = pygame.font.SysFont('sans-serif', 24, True)
        x = (surface.get_rect().width / 2) - 80
        y = 100
        surface.blit(font.render("          HI-SCORE", 1, WHITE), (x, y + (line_height * current_line)))
        current_line += 1
        surface.blit(font.render("***********************", 1, WHITE), (x, y + (line_height * current_line)))
        
        font = pygame.font.Font(None, 18)
        for hiscore in hiscores:
            current_line += 1
            surface.blit(font.render(str(current_line) + '. ' + Score.get_high_score_text(hiscore), 1, WHITE), (x, y + (line_height * current_line)))

    @staticmethod
    def update_highscore(name, score, hiscores):
        for i in range(0, len(hiscores)):
            if score > int(hiscores[i][1]):
                hiscores.insert(i, [name, score])
                del hiscores[-1]
                Score.write_highscore(hiscores)
                return
            
    
    @staticmethod
    def write_highscore(scores):
        try:
            with open(HISCORE_FILE, 'wb') as file:
                writer = csv.writer(file)
                for hiscore in scores:
                    writer.writerow(hiscore)
        except EnvironmentError as e:
            print "Could not open highscore file to read highscores."
            