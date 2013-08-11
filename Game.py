# This class contains the main game loop and handles the lifecycle of the game. It
# uses several different 'states' to keep track of what is going on at any given
# time. It starts by loading the 'intro' using the 'intro' state and then moves
# on to use 'menu' and 'game' states as appropriate.
#
# Author: Daniel Kvist
# E-mail: danielkvist81@gmail.com
# Python version: 2.7
# OS: OS X

import eztext
import sys
import pygame
from pygame.locals import *
from Intro import Intro
from Level import Level
from Menu import Menu
from Score import Score

class Game():
    FPS = 60
    SCREEN_SIZE = (1280, 720)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    DARK_GREY = (10, 10, 10)
    MUSIC_FILE = 'data/singsingsing.ogg'
    
    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont('sans-serif', 18, True)
        self.surface = pygame.display.set_mode(self.SCREEN_SIZE, 0, 32)
        self.state = 'intro'
        self.hiscores = Score.read_high_score()
        self.menu = Menu(("Start game", "Quit"))
        pygame.mixer.music.load(self.MUSIC_FILE)
        pygame.mixer.music.play(-1)
        
    def start(self):
        while True:
            if self.state == 'intro':
                # Show the intro and when it's done we move directly to game state
                intro = Intro(pygame, self.surface);
                new_state = intro.show()
                self.state = new_state
            elif self.state == 'menu':
                # Show the menu and run the menu loop
                self.hiscores = Score.read_high_score()
                self.show_menu()
            elif self.state == 'game':
                # Run a game and run the game loop
                self.load_level()
                self.game_loop()
            elif self.state == 'quit':
                # Quit, we're done.
                pygame.quit()
                sys.exit()
    
    # Contains the main menu loop and handles starting and quitting while showing the high scores
    def show_menu(self):
        pygame.mouse.set_visible(1)
        self.menu.drawMenu()
        while True:
            pygame.time.Clock().tick(self.FPS)
            for event in pygame.event.get():
                self.menu.handleEvent(event)
                if event.type == Menu.MENUCLICKEDEVENT or event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    if event.text == "Quit":
                        self.state = 'quit'
                        return
                    elif event.text == 'Start game':
                        self.state = 'game'
                        self.menu.deactivate()
                        return
                elif event.type == KEYDOWN and event.key == K_RETURN:
                    self.state = 'game'
                    self.menu.deactivate()
                    return
                        
            if self.menu.isActive():
                self.menu.drawMenu()
                
            Score.draw_high_scores(self.hiscores, self.surface)
            pygame.display.flip()
        
    # Loads and resets a level    
    def load_level(self):
        self.up = False
        self.speed = 6
        self.nameinput = None
        self.level = Level(self)
    
    # The main game loop that updates the level as the game progresses
    def game_loop(self):
        pygame.mouse.set_visible(0)
        while True:
            pygame.time.Clock().tick(self.FPS)
            events = pygame.event.get()
            for event in events:
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    self.state = 'quit'
                    return
                elif self.state == 'game':
                    if event.type == KEYDOWN:
                        if event.key == K_UP:
                            self.up = True
                    if event.type == KEYUP:
                        if event.key == K_UP:
                            self.up = False
                elif self.state == 'gameover':
                    if event.type == KEYUP:
                        if event.key == K_RETURN:
                            if self.nameinput != None:
                                name = self.nameinput.value
                                if name == '':
                                    name = 'no name'
                                Score.update_highscore(name, self.level.get_score(), self.hiscores)
                            self.state = 'menu'
                            return
             
            # Update level 
            self.level.update(self.up)
            self.level.draw()
            self.text = self.font.render("$" + str(self.level.get_score()), 1, self.DARK_GREY)
            self.surface.blit(self.text, (10, 10))

            # If player is busted the level is ended
            if self.level.player.state == 'busted':
                if Score.is_highscore(self.level.get_score(), self.hiscores):
                    self.message = "NEW HISCORE!"
                    if self.nameinput == None:
                        self.nameinput = eztext.Input(x = 400, y = 440, maxlength = 6, color = self.GREEN, prompt = 'Enter name: ')
                    self.nameinput.update(events)
                    self.nameinput.draw(self.surface)
                else:
                    self.message = "You did not collect enough cash, try again!"
                self.show_final_score()
                self.up = False
                self.state = 'gameover'

            # Flip the buffer to show the updates
            pygame.display.flip()
       
    # Blits the final score to the screen 
    def show_final_score(self):
        font = pygame.font.SysFont('sans-serif', 36, True)
        text = font.render("$" + str(self.level.get_score()), True, self.WHITE)
        self.surface.blit(text, (400, 475))
        self.surface.blit(font.render(self.message, 1, self.WHITE), (400, 400))
