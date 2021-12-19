import pygame 
from pygame.draw import *
from random import *
pygame.init()

class Hexagon:
    """Тип данных, описывающий гекс.
    Содержит экран, на котором изображается, коррдинаты икс и игрек, длину
    стороны, собственный номер, цыет, информацию о еде первого и второго
    типа, вероятности распространения каждого из грибов на себя, надпись о
    чиле еды каждого типа
    """
    
    def __init__(self, screen, x, y, a, n):
        self.screen = screen
        """экран, на котором изображается"""
        
        self.x = x
        """координата икс"""
        
        self.y = y
        """координата игрек"""
        
        self.a = a
        """длина стороны"""
        
        self.number = n
        """собственный номер"""
        
        self.color = (255, 255, 255)
        """цвет"""
        
        self.food_1 = 0
        """количевто еды 1 гриба"""
        
        self.food_2 = 0
        """количество еды второго гриба"""
        
        self.probability_1 = 0
        """вероятность быть захваченным 1 грибом"""
        
        self.probability_2 = 0
        """вероятность быть захваченным 2 грибом"""
        
        self.f_1 = pygame.font.Font(None, 20)
        """надпись о количетве еды для 1 гриба"""
        
        self.f_2 = pygame.font.Font(None, 20)
        """надпись о количестве еды для 2 гриба"""
    
    def draw(self):
        """рисование гекса. По данным центра **self.x0**, **self.y0** и стороны
        **a** рисует щестиугольник, залитый собственнным цветом, обведенный
        черным"""
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

    def choice(self, move):
        """подсветка контура выбранного гекса. Принимает параметр хода **move**
         гелает обводку геска цветом, соответствующим ходящему игроку цветом"""
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
        
    def show_probability(self):
        """отображения вероятности распространения на себя для грибов.
        В текстовых полях **self.f_1**, **self.f_2** выводит ненулевую
        вероятность распространения **self.probability_1**, **self.probability_2** """
        if self.probability_1 != 0:
            self.text_1 = self.f_1.render(str(round(self.probability_1, 2)), True, (255, 0, 0) )
            self.screen.blit(self.text_1, (self.x - 2.5 - self.a / 2, self.y + 2 - self.a / 1.5))
        if self.probability_2 != 0:
            self.text_2 = self.f_2.render(str(round(self.probability_2, 2)), True, (0, 0, 255) )
            self.screen.blit(self.text_2, (self.x - 2.5 - self.a / 2, self.y - 2 + self.a / 6))

    def show_food(self):
        """отображение количества еды. В текстовых полях **self.f_1**, **self.f_2**
        выводит ненулевые значения о количестве еды **self.food_1**, **self.food_2**"""
        if self.food_1 != 0:
            self.text_1 = self.f_1.render(str(self.food_1), True, (255, 0, 0) )
            self.screen.blit(self.text_1, (self.x - self.a / 1.5, self.y ))

        if self.food_2 != 0:
            self.text_2 = self.f_2.render(str(self.food_2), True, (0, 0, 255) )
            self.screen.blit(self.text_2, (self.x + self.a / 20 , self.y ))

    def unconfirmed_move(self):
        """неподтвержденный ход. Пока ход не подтвержден, создает фиолетовую
        обводку гекса с только что положенной едой"""
        polygon(self.screen, (148, 0, 211), [(self.x, self.y - self.a),
                                     (self.x + self.a * 3**0.5 /2, self.y - self.a/2),
                                     (self.x + self.a * 3**0.5 /2, self.y + self.a/2),
                                     (self.x, self.y + self.a),
                                     (self.x - self.a * 3**0.5 /2, self.y + self.a/2),
                                     (self.x - self.a * 3**0.5 /2, self.y - self.a/2),
                                     (self.x, self.y - self.a)], 3)
        
class Food:
    """Тип данный, описыающий едую
    Содержит координаты положения, экран, на котором отображается, свой радиус,
    цвет.
    """

    def __init__(self, screen, x, y, a, color):
        """принимает экран для отображения **screen**, координаты для еды **x**
        и **y**, сторону гекса, в котором находится еда **a**, цвет"""
        
        self.screen = screen
        """экран, на котором отображается"""
        
        self.x = x
        """координата икс"""
        
        self.y = y - a / 2.5
        """координата игрек"""
        
        self.r = a / 7
        """радиус"""
        
        self.color = color
        """цвет"""
        
    def drawf(self):
        """рисование еды. Круг с центром в координатах **self.x**, **self.x**
        радиусом **self.r**"""
        circle(self.screen, self.color, (self.x, self.y), self.r)

class Physarum:
    """Тип данных, описывающий гриб.
    Содерит массу (список захваченных клеток), экран, на которм изображается, цвет,
    список соседних клеток, суммарную вероятность распространения, ненормированный
    обычную и суммарную вероятности распространения.
    """
    
    def __init__(self, screen, mass, color):
        """Принимает данные об экране **screen**, **mass**, состоящий из начальной
        клетки, где гриб юыл поставлен, цвет гриба"""
        
        self.screen = screen
        """экран, на котором изображается"""
        
        self.mass = [mass]
        """масса (список захваенных клеток)"""

        self.color = color
        """цвет гриба"""
        
        self.neighbors = []
        """список соедей"""
        
        self.sum_prob = 0
        """суммарная вероятность распространения"""
        
        self.unnorm_prob = []
        """ненормированная вероятность распространения"""
        self.sum_unnorm_prob = 0
        """суммарная ненормарованная вероятность распространения"""
        
    def draw(self):
        """рисование гриба, а именно присваивание клеткам из его
        массы **self.mass*** собственного цвета **self.color**"""
        for i in self.mass:
            i.color = self.color

    def probability_of_motion(self, field):
        """пересчет списка соседей **self.neighbors** и вероятности распространения
        на клетки из принимаемого поля **field**. Возвращает обновленный список
        соседей **self.neighbors**"""
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

    def rise(self):
        """рост гриба присоединяет некоторые клетки из списка соседей **self.neighbors**
        к себе в **self.mass** и обнуляет список соседей **self.neighbors**"""
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

    def eating(self, physarum_enemy):
        """принимает вражеский гриб **physarum_enemy**, который поедает данный,
        удаляет съеденные клетки из **self.mass** данного гриба"""
        self.mass = list(set(self.mass))
        for i in self.mass:
            for j in physarum_enemy.mass:
                if i == j:
                    self.mass.remove(i)

"""как работает ИИ: в каждую клетку он пробует положить еду в свой ход,
пересчитывает вероятности с учетом этой еды и пробует вырасти. Ситуацию,
в которой он вырос на большее число клеток, он запомиинает и оставляет
еду в той клетке, в которой она лежала при этой ситуации."""

class Artificial_intelligence:
    """Тип данных, описывающий игрока в лице компьютера.
    Сожержит количесвто клеток, на которое гриб компьютера вырастает,
    наибольшее из возможных таких чисел, и номер выбранной клетка для
    размещения еды.
    """
    
    def __init__(self):
        self.summa = 0
        """количество клеток, на которое гриб смог вырасти при данном положении
        новой еды"""
        
        self.summa_max = 0
        """наибольшее количесвто клеток, на которое ему удалось вырасти"""
        
        self.computer_choice = -1
        """номер клетки, выбранной для размещения еды"""

    def  beginning(self, field):
        """возвращает номер случайной клeтки принимаемого игрового поля
        **field**"""
        return randint(0, len(field) - 1)

    def search(self, field, physarum_2):
        """поиск клетки из принимаемого **field**, на которую надо поставить еду,
        чтобы принимаемый **physarum_2** распространился на наибольшее количество клеток"""
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

if __name__ == "__main__":
    print("Этот модуль не заупускает игру! Запустите файл main!")

    
