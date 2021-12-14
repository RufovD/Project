#import pygame 
#import math
#from pygame.draw import *
#import random 
#pygame.init()


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
        return random.randint(0, len(field) - 1)

    #выбирает, куда поставить еду
    def search(self, field, physarum_2):
        self.max_summa = 0
        for k in field:
            self.summa = 0
            k.food_2 += 1
            physarum_2.neighbors_2 = physarum_2.probability_of_motion(field)
            
            for d in physarum_2.neighbors_2:
                if (d.probability_2 >= random.uniform(0, 1)) and (d.color != physarum_2.color):
                    self.summa += 1
                if self.summa >= self.max_summa:
                    self.max_summa = self.summa
                    self.computer_choice = k.number
            k.food_2 += -1
