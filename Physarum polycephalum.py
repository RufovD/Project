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


    def choise(self):
        polygon(self.screen, VIOLET, [(self.x, self.y - self.a),
                                     (self.x + self.a * 3**0.5 /2, self.y - self.a/2),
                                     (self.x + self.a * 3**0.5 /2, self.y + self.a/2),
                                     (self.x, self.y + self.a),
                                     (self.x - self.a * 3**0.5 /2, self.y + self.a/2),
                                     (self.x - self.a * 3**0.5 /2, self.y - self.a/2),
                                     (self.x, self.y - self.a)], 5)

    def show_probability(self):
        if self.probability_1 != 0:
            self.text_1 = self.f_1.render(str(self.probability_1), True, RED )
            screen.blit(self.text_1, (self.x - a / 2, self.y - a / 1.5))
        if self.probability_2 != 0:
            self.text_2 = self.f_2.render(str(self.probability_2), True, BLUE )
            screen.blit(self.text_2, (self.x - a / 2, self.y + a / 6))

    def show_food(self):
        if self.food_1 != 0:
            self.text_1 = self.f_1.render(str(self.food_1), True, RED )
            screen.blit(self.text_1, (self.x - a / 1.5, self.y ))

        if self.food_2 != 0:
            self.text_2 = self.f_2.render(str(self.food_2), True, BLUE )
            screen.blit(self.text_2, (self.x + a / 20 , self.y ))


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
                
        for j in self.neighbors_1:
            j.probability_1 = 0.2
            
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

    def draw(self):
        for i in self.mass:
            i.color = self.color

    def probability_of_motion(self):
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
     
        for j in self.neighbors_2:
            j.probability_2 = 0.2
            
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
GRAY = (128, 128, 128)



screen = pygame.display.set_mode((border_x, border_y))        
screen.fill(BLACK)
pygame.display.update()
clock = pygame.time.Clock()

click_position = 0

finished_1 = False
finished_2 = True
finished_3 = True
surface = False
move = 1


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
finished = False

while not finished_1:

    screen.fill(BLACK)
    
    for i in field:
        i.draw()


    clock.tick(FPS)

    click_position = pygame.mouse.get_pos()
    choise_hex_number = search(click_position, field)
    field[choise_hex_number].choise()
  
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished_1 = True
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                physarum_1 = Physarum_1(screen, field[choise_hex_number], YELLOW_1)
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
    choise_hex_number = search(click_position, field)
    if field[choise_hex_number] != physarum_1.mass[0]:
        field[choise_hex_number].choise()
    else:
        choise_hex_number = "1"

  
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished_2 = True
        else:
            if (event.type == pygame.MOUSEBUTTONDOWN) and (choise_hex_number != "1"):
                physarum_2 = Physarum_2(screen, field[choise_hex_number], GREEN_1)
                physarum_2.probability_of_motion()
                finished_2 = True
                finished_3 = False
    pygame.display.update()

physarum_1.draw()
physarum_2.draw()
physarum_1.neighbors_1 = physarum_1.probability_of_motion()
physarum_2.neighbors_2 = physarum_2.probability_of_motion()

while not finished_3:
    
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
           
        

    clock.tick(FPS)


    
    click_position = pygame.mouse.get_pos()
    choise_hex_number = search(click_position, field)
    field[choise_hex_number].choise()
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished_3 = True
        else:
            if (event.type == pygame.MOUSEBUTTONDOWN) and (move == 1):
                new_food = Food(screen, field[choise_hex_number].x - field[choise_hex_number].a / 2.5, field[choise_hex_number].y, field[choise_hex_number].a, RED )
                field[choise_hex_number].food_1 += 1
                feed_1 += [new_food]
                move = -1
                for i in field:
                    i.probability_1 = 0
                    i.probability_2 = 0
                physarum_1.neighbors_1 = physarum_1.probability_of_motion()
                physarum_2.neighbors_2 = physarum_2.probability_of_motion()



            elif (event.type == pygame.KEYDOWN) and (move == -1) and (event.key == pygame.K_RIGHT):
                move = 2
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
                
                
                


            elif (event.type == pygame.MOUSEBUTTONDOWN) and (move == 2):
                new_food = Food(screen, field[choise_hex_number].x + field[choise_hex_number].a / 2.5, field[choise_hex_number].y, field[choise_hex_number].a, BLUE)
                field[choise_hex_number].food_2 += 1
                feed_2 += [new_food]
                move = -2
                for i in field:
                    i.probability_1 = 0
                    i.probability_2 = 0
                physarum_1.neighbors_1 = physarum_1.probability_of_motion()
                physarum_2.neighbors_2 = physarum_2.probability_of_motion()

                

            elif (event.type == pygame.KEYDOWN) and (move == -2) and (event.key == pygame.K_RIGHT):
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
                
                
                


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    surface = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    surface = False
                    

    pygame.display.update()

pygame.quit()

