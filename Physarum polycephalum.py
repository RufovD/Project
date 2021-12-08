"""если целая часть номера клетки при делении на 34 дает нечетное число, то (+- 1, +- 34, -33, +35), иначе (+- 1, +- 34, +33, -35"""




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


    def choice(self):
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

    def show_probability(self):
        if self.probability_1 != 0:
            self.text_1 = self.f_1.render(str(round(self.probability_1, 2)), True, RED )
            screen.blit(self.text_1, (self.x - 2.5 - a / 2, self.y + 2 - a / 1.5))
        if self.probability_2 != 0:
            self.text_2 = self.f_2.render(str(round(self.probability_2, 2)), True, BLUE )
            screen.blit(self.text_2, (self.x - 2.5 - a / 2, self.y - 2 + a / 6))

    def show_food(self):
        if self.food_1 != 0:
            self.text_1 = self.f_1.render(str(self.food_1), True, RED )
            screen.blit(self.text_1, (self.x - a / 1.5, self.y ))

        if self.food_2 != 0:
            self.text_2 = self.f_2.render(str(self.food_2), True, BLUE )
            screen.blit(self.text_2, (self.x + a / 20 , self.y ))

    #неподтвержденный ход
    def unconfirmed_move(self):
        polygon(self.screen, VIOLET, [(self.x, self.y - self.a),
                                     (self.x + self.a * 3**0.5 /2, self.y - self.a/2),
                                     (self.x + self.a * 3**0.5 /2, self.y + self.a/2),
                                     (self.x, self.y + self.a),
                                     (self.x - self.a * 3**0.5 /2, self.y + self.a/2),
                                     (self.x - self.a * 3**0.5 /2, self.y - self.a/2),
                                     (self.x, self.y - self.a)], 3)


class Food:

    def __init__(self, screen, x, y, a, color):
        self.screen = screen
        self.x = x 
        self.y = y - a / 2.5
        self.r = a / 7
        self.color = color
        self.f = pygame.font.Font(None, 20)
        

    def drawf(self):
        circle(self.screen, self.color, (self.x, self.y), self.r)


class Physarum_1:
    def __init__(self, screen, mass, color):
        self.screen = screen
        self.mass = [mass]
        self.color = color
        self.neighbors_1 = []
        self.sum_prob = 0
        self.unnorm_prob = []
        self.sum_unnorm_prob = 0

    def draw(self):
        for i in self.mass:
            i.color = self.color

    def probability_of_motion(self):
        self.neighbors_1 = []
        for i in self.mass:
            if (i.number % 34 != 0) and (field[i.number - 1].color != self.color):
                self.neighbors_1 += [field[i.number - 1]] 
            if ((i.number + 1) % 34 != 0) and (field[i.number + 1].color != self.color):
                self.neighbors_1 += [field[i.number + 1]] 
            if (i.number - 34 >= 0) and (field[i.number - 34].color != self.color):
                self.neighbors_1 += [field[i.number - 34]]
            if (i.number + 34 <= 781) and (field[i.number + 34].color != self.color):
                self.neighbors_1 += [field[i.number +34]]
                
            if (i.number // 34) % 2 == 0:
                if (i.number - 35 >= 0) and (i.number % 34 != 0) and (field[i.number - 35].color != self.color):
                    self.neighbors_1 += [field[i.number - 35]]
                if (i.number + 34 <= 781) and (i.number % 34 != 0) and (field[i.number + 33].color != self.color):
                    self.neighbors_1 += [field[i.number + 33]]
            else:
                if (i.number + 34 <= 781) and ((i.number + 1) % 34 != 0) and (field[i.number + 35].color != self.color) :
                    self.neighbors_1 += [field[i.number + 35]]
                if (i.number - 34 >= 0) and ((i.number + 1) % 34 != 0) and (field[i.number - 33].color != self.color) :
                    self.neighbors_1 += [field[i.number - 33]]
                
        self.neighbors_1 = list(set(self.neighbors_1))
            
        self.sum_prob = 0.2 * len(self.neighbors_1)
        self.unnorm_prob = []
        self.sum_unnorm_prob = 0
        
        for j in self.neighbors_1:
            self.p = 0
            for i in field:
                if ( j.x - i.x != 0) or ( j.y - i.y != 0):
                    self.p += ((i.food_2)**0.5) / ( ( j.x - i.x )**2 + ( j.y - i.y )**2 )
                else:
                    self.p += ((i.food_2)**0.5) / ( i.a**2 )
                
            self.unnorm_prob += [self.p]
            self.sum_unnorm_prob += self.p

        for j in range(0, len(self.neighbors_1)):
            if self.sum_unnorm_prob != 0:
                self.neighbors_1[j].probability_1 = min((self.unnorm_prob[j] * self.sum_prob) / (self.sum_unnorm_prob), 0.99)
            else:
                self.neighbors_1[j].probability_1 = 0.2
            
        return self.neighbors_1

    def rise(self):
        for i in self.neighbors_1:
            if (i.probability_1 >= random.uniform(0, 1)) and (i.color != self.color):
                i.color = self.color
                self.mass += [i]
        self.mass = list(set(self.mass))
        self.neighbors_1 = []

    def eating(self):
        self.mass = list(set(self.mass))
        for i in self.mass:
            for j in physarum_2.mass:
                if i == j:
                    self.mass.remove(i)
            #if i.color != self.color:
                #self.mass.remove(i)
                
            

class Physarum_2:
    def __init__(self, screen, mass, color):
        self.screen = screen
        self.mass = [mass]
        self.color = color
        self.neighbors_2 = []
        self.sum_prob = 0
        self.unnorm_prob = []
        self.sum_unnorm_prob = 0

    def draw(self):
        for i in self.mass:
            i.color = self.color

    def probability_of_motion(self):
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

    def rise(self):
        for i in self.neighbors_2:
            if (i.probability_2 >= random.uniform(0, 1)) and (i.color != self.color):
                i.color = self.color
                self.mass += [i]
        self.mass = list(set(self.mass))
        self.neighbors_2 = []

    def eating(self):
        self.mass = list(set(self.mass))
        for i in self.mass:
            for j in physarum_1.mass:
                if i == j:
                    self.mass.remove(i)
            #if i.color != self.color:
                #self.mass.remove(i)



        
def search(click, field):
    minimum = 100000000000
    for i in range(0, len(field)):
        if (field[i].x - click[0])**2 + (field[i].y - click[1])**2 < minimum**2:
            minimum = ((field[i].x - click[0])**2 + (field[i].y - click[1])**2)**0.5
            m = i
    return m

def winner(win):
    text01 = f_01.render('Нажмите стрелочку вверх, чтобы вернуться к полю,', True,
                    (255, 255, 255))
    screen.blit(text01, (20, 150))
    text02 = f_02.render('затем зажмите пробел, чтобы посмотреть вероятности', True,
                    (255, 255, 255))
    screen.blit(text02, (20, 200))
    text03 = f_03.render('Чтобы вернуться к результату, нажмите стрелочку вниз', True,
                    (255, 255, 255))
    screen.blit(text03, (20, 250))
    if win == 1:
        text = f.render('Победил желтый гриб!', True,
                    (255, 255, 255))
        screen.blit(text, (20, 20))
    elif win == 2:
        text = f.render('Победил зеленый гриб!', True,
                    (255, 255, 255))
        screen.blit(text, (20, 20))
    else:
        text = f.render('Ничья!', True,
                    (255, 255, 255))
        screen.blit(text, (20, 20))


"""как работает ИИ: в каждую клетку он пробует положить еду в свой ход
пересчитывает вероятности с учетом этой еды. Находит сумму всех вероятностей
в итоге он положит еду туда, где эта сумма оказалась больше всего"""


class Artificial_intelligence:

    def __init__(self):
        self.summa = 0
        self.summa_max = 0
        self.computer_choice = -1

    def  beginning(self):
        return random.randint(0, len(field) - 1)
    
    def search(self):
        global field
        self.max_summa = 0
        for k in field:
            self.summa = 0
            k.food_2 += 1
            physarum_2.neighbors_2 = physarum_2.probability_of_motion()
            for d in field:
                self.summa += d.probability_2
            if self.summa >= self.max_summa:
                self.max_summa = self.summa
                self.computer_choice = k.number
            k.food_2 += -1
    

            
        


"""Описание игровых параметров (Границ игровой области, FPS"""
border_x = 1198
border_y = 700
FPS = 200

"Описание используемых цветов"
YELLOW_1 = (210, 200, 100)
GREEN_1 = (120, 200, 125)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
VIOLET = (148, 0, 211)
DARK_YELLOW_1 = (111, 103, 32) 
DARK_YELLOW_2 = (250, 165, 10) #обводка клетки, в которой находится курсор, для первого игрока
DARK_GREEN_1 = (35, 86, 54) #обводка клетки, в которой находится курсор, для второго игрока
GRAY = (128, 128, 128)



screen = pygame.display.set_mode((border_x, border_y))        
screen.fill(BLACK)
pygame.display.update()
clock = pygame.time.Clock()

click_position = 0

players = 0
finished_0 = False
finished_1 = True
finished_2 = True
finished_3 = True
finished_4 = True
surface = False
surface_1 = False
move = 1
remainder_of_moves = 12 #всего ходов на партию (остаток ходов)
win = -1
hex_with_new_food = 0

f_01 = pygame.font.Font(None, 50)
f_02 = pygame.font.Font(None, 50)
f_03 = pygame.font.Font(None, 50)
f = pygame.font.Font(None, 140)
f_0 = pygame.font.Font(None, 140)
f_3 = pygame.font.Font(None, 140)


feed_1 = [] #здесь будут храниться данные о корме для 1 (желтого) гриба
feed_2 = [] #здесь будут храниться данные о корме для 2 (зеленого) гриба
field = [] #здесь будут храниться все клетки (23*34)

a = 20
x0 = 0
y0 = a


for i in range(0, 23):
    if i % 2 == 0:
        x0 = a * (3**0.5) / 2
    else:
        x0 = a * (3**0.5)        
    for j in range(0, 34):
        new_hexagon = Hexagon(screen, x0, y0, a,  34 * i + j)
        new_hexagon.draw()
        field += [new_hexagon]
        x0 += new_hexagon.a * (3**0.5)
    y0 += 1.5 * a




pygame.display.update()
clock = pygame.time.Clock()


while not finished_0:

    screen.fill(BLACK)
    text = f.render('Нажмите:', True,
                    (255, 255, 255))
    screen.blit(text, (20, 20))

    text_0 = f_0.render('1 - играть с ИИ', True,
                    (255, 255, 255))
    screen.blit(text_0, (20, 120))

    text_3 = f_3.render('2 - играть вдвоем', True,
                    (255, 255, 255))
    screen.blit(text_3, (20, 220))
    
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished_0 = True
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    finished_0 = True
                    players = 1
                    finished_1 = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    finished_0 = True
                    players = 2
                    finished_1 = False
    

if players == 1:

    while not finished_1:
        
        screen.fill(BLACK)
        
        for i in field:
            i.draw()


        clock.tick(FPS)

        click_position = pygame.mouse.get_pos()
        choice_hex_number = search(click_position, field)
        field[choice_hex_number].choice()
      
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished_1 = True
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    physarum_1 = Physarum_1(screen, field[choice_hex_number], YELLOW_1)
                    physarum_1.probability_of_motion()
                    finished_1 = True
                    finished_2 = False
        pygame.display.update()

    if not finished_2:
        computer = Artificial_intelligence()


    while not finished_2:

        screen.fill(BLACK)
        
        for i in field:
            i.draw()

        physarum_1.draw()
        
        clock.tick(FPS)

        choice_hex_number = computer.beginning()        

        if field[choice_hex_number] != physarum_1.mass[0]:
            physarum_2 = Physarum_2(screen, field[choice_hex_number], GREEN_1)
            finished_2 = True
            finished_3 = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished_2 = True

                
        pygame.display.update()


    if not finished_3:
        physarum_1.draw()
        physarum_2.draw()
        physarum_1.neighbors_1 = physarum_1.probability_of_motion()
        physarum_2.neighbors_2 = physarum_2.probability_of_motion()

    while not finished_3:

        if (len(physarum_1.mass) == 0) or (len(physarum_2.mass) == 0):
            finished_3 = True
            finished_4 = False
        
        screen.fill(BLACK)
        
        for i in field:
            i.draw()


        if surface:
            for i in field:
                i.show_probability()
        else:
            for i in field:
                i.show_food()
            for i in feed_1:
                i.drawf()
            for i in feed_2:
                i.drawf()

        if hex_with_new_food != 0:
            hex_with_new_food.unconfirmed_move()
               
            

        clock.tick(FPS)


        
        click_position = pygame.mouse.get_pos()
        choice_hex_number = search(click_position, field)
        field[choice_hex_number].choice()
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished_3 = True
            else:
                if (event.type == pygame.MOUSEBUTTONDOWN) and (move == 1):
                    new_food = Food(screen, field[choice_hex_number].x - field[choice_hex_number].a / 2.5,
                                    field[choice_hex_number].y, field[choice_hex_number].a, RED )
                    field[choice_hex_number].food_1 += 1
                    hex_with_new_food = field[choice_hex_number]
                    feed_1 += [new_food]
                    move = 11
                    for i in field:
                        i.probability_1 = 0
                        i.probability_2 = 0
                    physarum_1.neighbors_1 = physarum_1.probability_of_motion()
                    physarum_2.neighbors_2 = physarum_2.probability_of_motion()


                elif (event.type == pygame.MOUSEBUTTONDOWN) and (move == 11) and (field[choice_hex_number] == hex_with_new_food):
                    hex_with_new_food.food_1 += -1
                    hex_with_new_food = 0
                    feed_1.pop(-1)
                    move = 1
                    for i in field:
                        i.probability_1 = 0
                        i.probability_2 = 0
                    physarum_1.neighbors_1 = physarum_1.probability_of_motion()
                    physarum_2.neighbors_2 = physarum_2.probability_of_motion()


                elif (event.type == pygame.KEYDOWN) and (move == 11) and (event.key == pygame.K_RIGHT):
                    hex_with_new_food = 0
                    move = -2
                    physarum_1.rise()

                    #print("__________________")
                    #print("первый", len(physarum_1.mass), "клетки" )
                    #for j in physarum_1.mass:
                        #print(j.number)
                        
                    physarum_2.eating()
                    for j in physarum_2.mass:
                        if j.color != GREEN_1:
                            physarum_2.mass.remove(j)
                    
                    #print("второй", len(physarum_2.mass), "клетки" )
                    #for j in physarum_2.mass:
                        #print(   j.number)
                        
                    for i in field:
                        i.probability_1 = 0
                        i.probability_2 = 0
                    physarum_1.neighbors_1 = physarum_1.probability_of_motion()
                    physarum_2.neighbors_2 = physarum_2.probability_of_motion()
                    
                    
                    


                elif move == -2:
                    computer.search()
                    new_food = Food(screen, field[computer.computer_choice].x + field[computer.computer_choice].a / 2.5,
                                    field[computer.computer_choice].y, field[computer.computer_choice].a, BLUE)
                    field[computer.computer_choice].food_2 += 1
                    feed_2 += [new_food]
                    move = 1
                    for i in field:
                        i.probability_1 = 0
                        i.probability_2 = 0
                    physarum_1.neighbors_1 = physarum_1.probability_of_motion()
                    physarum_2.neighbors_2 = physarum_2.probability_of_motion()
                    physarum_2.rise()
                    physarum_1.eating()
                    for j in physarum_1.mass:
                        if j.color != YELLOW_1:
                            physarum_1.mass.remove(j)
                    for i in field:
                        i.probability_1 = 0
                        i.probability_2 = 0
                    physarum_1.neighbors_1 = physarum_1.probability_of_motion()
                    physarum_2.neighbors_2 = physarum_2.probability_of_motion()

                    remainder_of_moves += -1
                    if remainder_of_moves <= 0:
                        finished_3 = True
                        finished_4 = False
                    
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        surface = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        surface = False
                        

        pygame.display.update()
        


if players == 2:
    
    while not finished_1:

        screen.fill(BLACK)
        
        for i in field:
            i.draw()


        clock.tick(FPS)

        click_position = pygame.mouse.get_pos()
        choice_hex_number = search(click_position, field)
        field[choice_hex_number].choice()
      
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished_1 = True
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    physarum_1 = Physarum_1(screen, field[choice_hex_number], YELLOW_1)
                    physarum_1.probability_of_motion()
                    finished_1 = True
                    finished_2 = False
        pygame.display.update()


    while not finished_2:

        screen.fill(BLACK)
        
        for i in field:
            i.draw()

        physarum_1.draw()
        
        clock.tick(FPS)

        click_position = pygame.mouse.get_pos()
        choice_hex_number = search(click_position, field)
        if field[choice_hex_number] != physarum_1.mass[0]:
            field[choice_hex_number].choice()
        else:
            choice_hex_number = "1"

      
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished_2 = True
            else:
                if (event.type == pygame.MOUSEBUTTONDOWN) and (choice_hex_number != "1"):
                    physarum_2 = Physarum_2(screen, field[choice_hex_number], GREEN_1)
                    finished_2 = True
                    finished_3 = False
        pygame.display.update()

    if not finished_3:
        physarum_1.draw()
        physarum_2.draw()
        physarum_1.neighbors_1 = physarum_1.probability_of_motion()
        physarum_2.neighbors_2 = physarum_2.probability_of_motion()

    while not finished_3:

        if (len(physarum_1.mass) == 0) or (len(physarum_2.mass) == 0):
            finished_3 = True
            finished_4 = False
        
        screen.fill(BLACK)
        
        for i in field:
            i.draw()


        if surface:
            for i in field:
                i.show_probability()
        else:
            for i in field:
                i.show_food()
            for i in feed_1:
                i.drawf()
            for i in feed_2:
                i.drawf()
               
        if hex_with_new_food != 0:
            hex_with_new_food.unconfirmed_move()

        clock.tick(FPS)


        
        click_position = pygame.mouse.get_pos()
        choice_hex_number = search(click_position, field)
        field[choice_hex_number].choice()
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished_3 = True
            else:
                if (event.type == pygame.MOUSEBUTTONDOWN) and (move == 1):
                    new_food = Food(screen, field[choice_hex_number].x - field[choice_hex_number].a / 2.5,
                                    field[choice_hex_number].y, field[choice_hex_number].a, RED )
                    field[choice_hex_number].food_1 += 1
                    hex_with_new_food = field[choice_hex_number]
                    feed_1 += [new_food]
                    move = 11
                    for i in field:
                        i.probability_1 = 0
                        i.probability_2 = 0
                    physarum_1.neighbors_1 = physarum_1.probability_of_motion()
                    physarum_2.neighbors_2 = physarum_2.probability_of_motion()


                elif (event.type == pygame.MOUSEBUTTONDOWN) and (move == 11) and (field[choice_hex_number] == hex_with_new_food):
                    hex_with_new_food.food_1 += -1
                    hex_with_new_food = 0
                    feed_1.pop(-1)
                    move = 1
                    for i in field:
                        i.probability_1 = 0
                        i.probability_2 = 0
                    physarum_1.neighbors_1 = physarum_1.probability_of_motion()
                    physarum_2.neighbors_2 = physarum_2.probability_of_motion()


                elif (event.type == pygame.KEYDOWN) and (move == 11) and (event.key == pygame.K_RIGHT):
                    hex_with_new_food = 0
                    move = -2
                    physarum_1.rise()

                    #print("__________________")
                    #print("первый", len(physarum_1.mass), "клетки" )
                    #for j in physarum_1.mass:
                        #print(j.number)
                        
                    physarum_2.eating()
                    for j in physarum_2.mass:
                        if j.color != GREEN_1:
                            physarum_2.mass.remove(j)
                    
                    #print("второй", len(physarum_2.mass), "клетки" )
                    #for j in physarum_2.mass:
                        #print(   j.number)
                        
                    for i in field:
                        i.probability_1 = 0
                        i.probability_2 = 0
                    physarum_1.neighbors_1 = physarum_1.probability_of_motion()
                    physarum_2.neighbors_2 = physarum_2.probability_of_motion()
                    
                    
                    


                elif (event.type == pygame.MOUSEBUTTONDOWN) and (move == -2):
                    new_food = Food(screen, field[choice_hex_number].x + field[choice_hex_number].a / 2.5,
                                    field[choice_hex_number].y, field[choice_hex_number].a, BLUE)
                    field[choice_hex_number].food_2 += 1
                    feed_2 += [new_food]
                    hex_with_new_food = field[choice_hex_number]
                    move = -22
                    for i in field:
                        i.probability_1 = 0
                        i.probability_2 = 0
                    physarum_1.neighbors_1 = physarum_1.probability_of_motion()
                    physarum_2.neighbors_2 = physarum_2.probability_of_motion()
                    

                elif (event.type == pygame.MOUSEBUTTONDOWN) and (move == -22) and (field[choice_hex_number] == hex_with_new_food):
                    hex_with_new_food.food_2 += -1
                    hex_with_new_food = 0
                    feed_2.pop(-1)
                    move = -2
                    for i in field:
                        i.probability_1 = 0
                        i.probability_2 = 0
                    physarum_1.neighbors_1 = physarum_1.probability_of_motion()
                    physarum_2.neighbors_2 = physarum_2.probability_of_motion()

                    

                elif (event.type == pygame.KEYDOWN) and (move == -22) and (event.key == pygame.K_RIGHT):
                    hex_with_new_food = 0
                    move = 1
                    physarum_2.rise()

                    #print("__________________")
                    #print("второй", len(physarum_2.mass), "клетки" )
                    #for j in physarum_2.mass:
                        #print(   j.number)
                    
                    physarum_1.eating()
                    for j in physarum_1.mass:
                        if j.color != YELLOW_1:
                            physarum_1.mass.remove(j)

                    #print("первый", len(physarum_1.mass), "клетки" )
                    #for j in physarum_1.mass:
                        #print(j.number)
                    
                    for i in field:
                        i.probability_1 = 0
                        i.probability_2 = 0
                    physarum_1.neighbors_1 = physarum_1.probability_of_motion()
                    physarum_2.neighbors_2 = physarum_2.probability_of_motion()

                    remainder_of_moves += -1
                    if remainder_of_moves <= 0:
                        finished_3 = True
                        finished_4 = False
                    
                    
                    


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        surface = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        surface = False
                        

        pygame.display.update()

if not finished_4:
    if len(physarum_1.mass) > len(physarum_2.mass):
        win = 1
    elif len(physarum_1.mass) < len(physarum_2.mass):
        win = 2
    else:
        win = 0
    
if not finished_4:
    print("клеток захвачено желтым грибом: ", len(physarum_1.mass), "захвачено зеленым грибом: ", len(physarum_2.mass))

while not finished_4:

    screen.fill(BLACK)

    if surface_1:
        for i in field:
            i.draw()
        if surface:
            for i in field:
                i.show_probability()
        else:
            for i in field:
                i.show_food()
            for i in feed_1:
                i.drawf()
            for i in feed_2:
                i.drawf()
    else:
        winner(win) 
        
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished_4 = True

        if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        surface_1 = True
                    if event.key == pygame.K_DOWN:
                        surface_1 = False

        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                        surface = True
        if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    surface = False

    pygame.display.update()

pygame.quit()

