import pygame 
from pygame.draw import *
from random import *
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
        self.color = (255, 255, 255)
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
        
        polygon(self.screen, (0, 0, 0), [(self.x, self.y - self.a),
                                     (self.x + self.a * 3**0.5 /2, self.y - self.a/2),
                                     (self.x + self.a * 3**0.5 /2, self.y + self.a/2),
                                     (self.x, self.y + self.a),
                                     (self.x - self.a * 3**0.5 /2, self.y + self.a/2),
                                     (self.x - self.a * 3**0.5 /2, self.y - self.a/2),
                                     (self.x, self.y - self.a)], 1)

    #подсветка контура выбранного гекса цветом, соответствующим ходящему игроку
    def choice(self, move):
        if move > 0:
            FRAME_COLOR = (250, 165, 10)
        if move < 0:
            FRAME_COLOR = (35, 86, 54)
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
            self.text_1 = self.f_1.render(str(round(self.probability_1, 2)), True, (255, 0, 0) )
            self.screen.blit(self.text_1, (self.x - 2.5 - self.a / 2, self.y + 2 - self.a / 1.5))
        if self.probability_2 != 0:
            self.text_2 = self.f_2.render(str(round(self.probability_2, 2)), True, (0, 0, 255) )
            self.screen.blit(self.text_2, (self.x - 2.5 - self.a / 2, self.y - 2 + self.a / 6))

    #отображение количества еды
    def show_food(self):
        if self.food_1 != 0:
            self.text_1 = self.f_1.render(str(self.food_1), True, (255, 0, 0) )
            self.screen.blit(self.text_1, (self.x - self.a / 1.5, self.y ))

        if self.food_2 != 0:
            self.text_2 = self.f_2.render(str(self.food_2), True, (0, 0, 255) )
            self.screen.blit(self.text_2, (self.x + self.a / 20 , self.y ))

    #неподтвержденный ход
    def unconfirmed_move(self):
        polygon(self.screen, (148, 0, 211), [(self.x, self.y - self.a),
                                     (self.x + self.a * 3**0.5 /2, self.y - self.a/2),
                                     (self.x + self.a * 3**0.5 /2, self.y + self.a/2),
                                     (self.x, self.y + self.a),
                                     (self.x - self.a * 3**0.5 /2, self.y + self.a/2),
                                     (self.x - self.a * 3**0.5 /2, self.y - self.a/2),
                                     (self.x, self.y - self.a)], 3)

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
                if (i.probability_1 >= uniform(0, 1)) and (i.color != self.color):
                    i.color = self.color
                    self.mass += [i]
            if self.color == (120, 200, 125):
                if (i.probability_2 >= uniform(0, 1)) and (i.color != self.color):
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

"""как работает ИИ: в каждую клетку он пробует положить еду в свой ход,
пересчитывает вероятности с учетом этой еды и пробует вырасти. Ситуацию,
в которой он вырос на большее число клеток, он запомиинает и оставляет
еду в той клетке, в которой она лежала при этой ситуации."""

#Искусственнный интелект
class Artificial_intelligence:

    #при создании
    def __init__(self):
        self.summa = 0 #оличесвто клеток, на которое вырас гриб при фиксированной еде
        self.summa_max = 0 #наибольшее количесто клеток, на которое грибу удалось вырасти
        self.computer_choice = -1 #номер клетки, выбранной для постановки туда еды

    #ставит первую клетку гриба
    def  beginning(self, field): 
        return randint(0, len(field) - 1)

    #выбирает, куда поставить еду
    def search(self, field, physarum_2):
        self.max_summa = 0
        for k in field:
            self.summa = 0
            k.food_2 += 1
            physarum_2.neighbors_2 = physarum_2.probability_of_motion(field)
            
            for d in physarum_2.neighbors_2:
                if (d.probability_2 >= uniform(0, 1)) and (d.color != physarum_2.color):
                    self.summa += 1
                if self.summa >= self.max_summa:
                    self.max_summa = self.summa
                    self.computer_choice = k.number
            k.food_2 += -1
