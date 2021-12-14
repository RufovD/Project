import pygame 
from pygame.draw import *



#Еда
class Food:

    #при создании
    def __init__(self, screen, x, y, a, color):
        self.screen = screen
        self.x = x 
        self.y = y - a / 2.5
        self.r = a / 7
        self.color = color
        self.f = pygame.font.Font(None, 20)

    #рисование
    def drawf(self):
        circle(self.screen, self.color, (self.x, self.y), self.r)
