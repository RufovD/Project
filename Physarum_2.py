import pygame 
import math
from pygame.draw import *
import random 
pygame.init()

#Фузарум 2 игрока
class Physarum_2:
    def __init__(self, screen, mass, color):
        self.screen = screen #экран
        self.mass = [mass] #клетки, захваченные фузарумом
        self.color = color #цвет фузарума
        self.neighbors_2 = [] #соседи фузарума
        self.sum_prob = 0 #суммарная вероятность
        self.unnorm_prob = [] #ненормированная вероятность для одного соседа
        self.sum_unnorm_prob = 0 # суммарная ненормированная вероятность для все соседей

    #рисование
    def draw(self):
        for i in self.mass:
            i.color = self.color

    #пересчет соседей и вероятностей распространения в зависимости от количества и положения еды
    def probability_of_motion(self, field):
        global feed_2
        self.neighbors_2 = []
        for i in self.mass:
            if (i.number % 34 != 0) and (field[i.number - 1].color != self.color):
                self.neighbors_2 += [field[i.number - 1]] 
            if ((i.number + 1) % 34 != 0) and (field[i.number + 1].color != self.color):
                self.neighbors_2 += [field[i.number + 1]] 
            if (i.number - 34 >= 0) and (field[i.number - 34].color != self.color):
                self.neighbors_2 += [field[i.number - 34]]
            if (i.number + 34 <= 781) and (field[i.number + 34].color != self.color):
                self.neighbors_2 += [field[i.number +34]]
                
            if (i.number // 34) % 2 == 0:
                if (i.number - 35 >= 0) and (i.number % 34 != 0) and (field[i.number - 35].color != self.color):
                    self.neighbors_2 += [field[i.number - 35]]
                if (i.number + 34 <= 781) and (i.number % 34 != 0) and (field[i.number + 33].color != self.color):
                    self.neighbors_2 += [field[i.number + 33]]
            else:
                if (i.number + 34 <= 781) and ((i.number + 1) % 34 != 0) and (field[i.number + 35].color != self.color) :
                    self.neighbors_2 += [field[i.number + 35]]
                if (i.number - 34 >= 0) and ((i.number + 1) % 34 != 0) and (field[i.number - 33].color != self.color) :
                    self.neighbors_2 += [field[i.number - 33]]
                    
        self.neighbors_2 = list(set(self.neighbors_2))
            
        self.sum_prob = 0.2 * len(self.neighbors_2)
        self.unnorm_prob = []
        self.sum_unnorm_prob = 0
        
        for j in self.neighbors_2:
            self.p = 0
            for i in field:
                if ( j.x - i.x != 0) or ( j.y - i.y != 0):
                    self.p += ((i.food_2)**0.5) / ( ( j.x - i.x )**2 + ( j.y - i.y )**2 )
                else:
                    self.p += ((i.food_2)**0.5) / ( i.a**2 )
                
            self.unnorm_prob += [self.p]
            self.sum_unnorm_prob += self.p

        for j in range(0, len(self.neighbors_2)):
            if self.sum_unnorm_prob != 0:
                self.neighbors_2[j].probability_2 = min((self.unnorm_prob[j] * self.sum_prob) / (self.sum_unnorm_prob), 0.99)
            else:
                self.neighbors_2[j].probability_2 = 0.2
            
        return self.neighbors_2

    #рост фузарума
    def rise(self):
        for i in self.neighbors_2:
            if (i.probability_2 >= random.uniform(0, 1)) and (i.color != self.color):
                i.color = self.color
                self.mass += [i]
        self.mass = list(set(self.mass))
        self.neighbors_2 = []

        
    #этот фузарум поедается другим
    def eating(self, physarum_1):
        self.mass = list(set(self.mass))
        for i in self.mass:
            for j in physarum_1.mass:
                if i == j:
                    self.mass.remove(i)
