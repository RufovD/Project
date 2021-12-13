import pygame 
import math
from pygame.draw import *
import random 
pygame.init()


"""Описание шестиугольных клеток"""
class Hexagon:

    """При создании"""
    def __init__(self, screen, x, y, a, n):
        self.screen = screen
        self.x = x
        self.y = y
        self.a = a
        self.number = n
        self.color = WHITE
        self.food_1 = 0
        self.food_2 = 0
        self.probability_1 = 0
        self.probability_2 = 0
        self.f_1 = pygame.font.Font(None, 20)
        self.f_2 = pygame.font.Font(None, 20)
        
        

    """Прорисовка"""
    def draw(self):
        polygon(self.screen, self.color, [(self.x, self.y - self.a),
                                          (self.x + self.a * 3**0.5 /2, self.y - self.a/2),
                                          (self.x + self.a * 3**0.5 /2, self.y + self.a/2),
                                          (self.x, self.y + self.a),
                                          (self.x - self.a * 3**0.5 /2, self.y + self.a/2),
                                          (self.x - self.a * 3**0.5 /2, self.y - self.a/2),
                                          (self.x, self.y - self.a)])
        
        polygon(self.screen, BLACK, [(self.x, self.y - self.a),
                                     (self.x + self.a * 3**0.5 /2, self.y - self.a/2),
                                     (self.x + self.a * 3**0.5 /2, self.y + self.a/2),
                                     (self.x, self.y + self.a),
                                     (self.x - self.a * 3**0.5 /2, self.y + self.a/2),
                                     (self.x - self.a * 3**0.5 /2, self.y - self.a/2),
                                     (self.x, self.y - self.a)], 1)

    #подсветка контура выбранного гекса цветом, соответствующим ходящему игроку
    def choice(self, finished_1, finished_2, move):
        if not finished_1 or move > 0:
            FRAME_COLOR = DARK_YELLOW_2
        if not finished_2 or move < 0:
            FRAME_COLOR = DARK_GREEN_1
        polygon(self.screen, FRAME_COLOR, [(self.x, self.y - self.a),
                                     (self.x + self.a * 3**0.5 /2, self.y - self.a/2),
                                     (self.x + self.a * 3**0.5 /2, self.y + self.a/2),
                                     (self.x, self.y + self.a),
                                     (self.x - self.a * 3**0.5 /2, self.y + self.a/2),
                                     (self.x - self.a * 3**0.5 /2, self.y - self.a/2),
                                     (self.x, self.y - self.a)], 5)
        
    #отображение вероятностей распространения
    def show_probability(self):
        if self.probability_1 != 0:
            self.text_1 = self.f_1.render(str(round(self.probability_1, 2)), True, RED )
            self.screen.blit(self.text_1, (self.x - 2.5 - self.a / 2, self.y + 2 - self.a / 1.5))
        if self.probability_2 != 0:
            self.text_2 = self.f_2.render(str(round(self.probability_2, 2)), True, BLUE )
            self.screen.blit(self.text_2, (self.x - 2.5 - self.a / 2, self.y - 2 + self.a / 6))

    #отображение количества еды
    def show_food(self):
        if self.food_1 != 0:
            self.text_1 = self.f_1.render(str(self.food_1), True, RED )
            self.screen.blit(self.text_1, (self.x - self.a / 1.5, self.y ))

        if self.food_2 != 0:
            self.text_2 = self.f_2.render(str(self.food_2), True, BLUE )
            self.screen.blit(self.text_2, (self.x + self.a / 20 , self.y ))

    #неподтвержденный ход
    def unconfirmed_move(self):
        polygon(self.screen, VIOLET, [(self.x, self.y - self.a),
                                     (self.x + self.a * 3**0.5 /2, self.y - self.a/2),
                                     (self.x + self.a * 3**0.5 /2, self.y + self.a/2),
                                     (self.x, self.y + self.a),
                                     (self.x - self.a * 3**0.5 /2, self.y + self.a/2),
                                     (self.x - self.a * 3**0.5 /2, self.y - self.a/2),
                                     (self.x, self.y - self.a)], 3)


"""Описание используемых цветов"""
RED = (255, 0, 0) #цвет еды и отображения вероятности для первого гриба
BLUE = (0, 0, 255) #цвет еды и отображения вероятности для второго гриба
BLACK = (0, 0, 0) #оконтовка клетки
WHITE = (255, 255, 255) #цвет нейтральной клетки
VIOLET = (148, 0, 211) #оконтовка клетки с только что поставленной едой
DARK_YELLOW_2 = (250, 165, 10) #обводка клетки, в которой находится курсор, для первого игрока
DARK_GREEN_1 = (35, 86, 54) #обводка клетки, в которой находится курсор, для второго игрока


