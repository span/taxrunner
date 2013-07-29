import eztext
import sys
import pygame
from pygame.locals import *
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
        self.font = pygame.font.Font(None, 18)
        self.surface = pygame.display.set_mode(self.SCREEN_SIZE, 0, 32)
        self.state = 'menu'
        self.menu = Menu(("Start game", "Quit"))
        pygame.mixer.music.load(self.MUSIC_FILE)
        pygame.mixer.music.play(-1)
        
    def start(self):
        while True:
            if self.state == 'menu':
                self.hiscores = Score.read_high_score()
                self.show_menu()
            elif self.state == 'game':
                self.load_level()
                self.game_loop()
            elif self.state == 'quit':
                pygame.quit()
                sys.exit()
        
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
            
    def load_level(self):
        self.up = False
        self.speed = 5
        self.nameinput = None
        self.level = Level(self)
        
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
        
    def show_final_score(self):
        font = pygame.font.Font(None, 36)
        text = font.render("$" + str(self.level.get_score()), 1, self.WHITE)
        self.surface.blit(text, (400, 475))
        self.surface.blit(font.render(self.message, 1, self.WHITE), (400, 400))
