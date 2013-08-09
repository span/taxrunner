#! /usr/bin/env python
# This file is the entry point into the application. It simply calls its own
# main method to start the game.
#
# Author: Daniel Kvist
# E-mail: danielkvist81@gmail.com
# Python version: 2.7
# OS: OS X

import pygame
from pygame.locals import *
from Game import Game

def main():
    game = Game()
    game.start()
          
main()