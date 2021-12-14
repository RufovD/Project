#import pygame 
#import math
#from pygame.draw import *
import random 
#pygame.init()

#Фузарум 1 игрока
class Physarum:
    def __init__(self, screen, mass, color):
        self.screen = screen #экран
        self.mass = [mass] #клетки, захваченные фузарумом
        self.color = color #цвет фузарума
        self.neighbors = [] #соседи фузарума
        self.sum_prob = 0 #суммарная вероятность
        self.unnorm_prob = [] #ненормированная вероятность для одного соседа
        self.sum_unnorm_prob = 0 # суммарная ненормированная вероятность для все соседей

    #рисование
    def draw(self):
        for i in self.mass:
            i.color = self.color

    #пересчет соседей и вероятностей распространения в зависимости от количества и положения еды
    def probability_of_motion(self, field):
        self.neighbors = []
        for i in self.mass:
            if (i.number % 34 != 0) and (field[i.number - 1].color != self.color):
                self.neighbors += [field[i.number - 1]] 
            if ((i.number + 1) % 34 != 0) and (field[i.number + 1].color != self.color):
                self.neighbors += [field[i.number + 1]] 
            if (i.number - 34 >= 0) and (field[i.number - 34].color != self.color):
                self.neighbors += [field[i.number - 34]]
            if (i.number + 34 <= 781) and (field[i.number + 34].color != self.color):
                self.neighbors += [field[i.number +34]]
                
            if (i.number // 34) % 2 == 0:
                if (i.number - 35 >= 0) and (i.number % 34 != 0) and (field[i.number - 35].color != self.color):
                    self.neighbors += [field[i.number - 35]]
                if (i.number + 34 <= 781) and (i.number % 34 != 0) and (field[i.number + 33].color != self.color):
                    self.neighbors += [field[i.number + 33]]
            else:
                if (i.number + 34 <= 781) and ((i.number + 1) % 34 != 0) and (field[i.number + 35].color != self.color) :
                    self.neighbors += [field[i.number + 35]]
                if (i.number - 34 >= 0) and ((i.number + 1) % 34 != 0) and (field[i.number - 33].color != self.color) :
                    self.neighbors += [field[i.number - 33]]
                
        self.neighbors = list(set(self.neighbors))
            
        self.sum_prob = 0.2 * len(self.neighbors)
        self.unnorm_prob = []
        self.sum_unnorm_prob = 0
        
        for j in self.neighbors:
            self.p = 0
            for i in field:
                if self.color == (210, 200, 100):             
                    if ( j.x - i.x != 0) or ( j.y - i.y != 0):
                        self.p += ((i.food_1)**0.5) / ( ( j.x - i.x )**2 + ( j.y - i.y )**2 )
                    else:
                        self.p += ((i.food_1)**0.5) / ( i.a**2 )
                elif self.color == (120, 200, 125):
                    if ( j.x - i.x != 0) or ( j.y - i.y != 0):
                        self.p += ((i.food_2)**0.5) / ( ( j.x - i.x )**2 + ( j.y - i.y )**2 )
                    else:
                        self.p += ((i.food_2)**0.5) / ( i.a**2 )                
            self.unnorm_prob += [self.p]
            self.sum_unnorm_prob += self.p

        for j in range(0, len(self.neighbors)):
            if self.color == (210, 200, 100): 
                if self.sum_unnorm_prob != 0:
                    self.neighbors[j].probability_1 = min((self.unnorm_prob[j] * self.sum_prob) / (self.sum_unnorm_prob), 0.99)
                else:
                    self.neighbors[j].probability_1 = 0.2
            elif self.color == (120, 200, 125): 
                if self.sum_unnorm_prob != 0:
                    self.neighbors[j].probability_2 = min((self.unnorm_prob[j] * self.sum_prob) / (self.sum_unnorm_prob), 0.99)
                else:
                    self.neighbors[j].probability_2 = 0.2
            
        return self.neighbors

    #рост фузарума
    def rise(self):
        for i in self.neighbors:
            if self.color == (210, 200, 100):
                if (i.probability_1 >= random.uniform(0, 1)) and (i.color != self.color):
                    i.color = self.color
                    self.mass += [i]
            if self.color == (120, 200, 125):
                if (i.probability_2 >= random.uniform(0, 1)) and (i.color != self.color):
                    i.color = self.color
                    self.mass += [i]
        self.mass = list(set(self.mass))
        self.neighbors = []

    #этот фузарум поедается другим
    def eating(self, physarum_enemy):
        self.mass = list(set(self.mass))
        for i in self.mass:
            for j in physarum_enemy.mass:
                if i == j:
                    self.mass.remove(i)
