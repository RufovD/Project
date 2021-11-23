"""если целая часть номера клетки при делении на 34 дает нечетное число, то (+- 1, +- 34, -33, +35), иначе (+- 1, +- 34, +33, -35"""




import pygame
import math
from pygame.draw import *
from random import randint
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
        self.food = 0
        probability_1 = 0
        probability_2 = 0

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
        polygon(self.screen, RED, [(self.x, self.y - self.a),
                                     (self.x + self.a * 3**0.5 /2, self.y - self.a/2),
                                     (self.x + self.a * 3**0.5 /2, self.y + self.a/2),
                                     (self.x, self.y + self.a),
                                     (self.x - self.a * 3**0.5 /2, self.y + self.a/2),
                                     (self.x - self.a * 3**0.5 /2, self.y - self.a/2),
                                     (self.x, self.y - self.a)], 5)

class Food:

    def __init__(self, screen, x, y, a):
        self.screen = screen
        self.x = x + a / 2.5
        self.y = y - a / 2.5
        self.r = a / 7
        self.color = BLUE

    def drawf(self):
        circle(self.screen, self.color, (self.x, self.y), self.r)


class Physarum_1:
    def __init__(self, screen, mass, color):
        self.screen = screen
        self.mass = [mass]
        self.color = color

    def draw(self):
        for i in self.mass:
            i.color = self.color

    def probability_of_motion(self):
        neighbors_1 = []
        for i in self.mass:
            if i.number - 1 >= 0:
                neighbors_1 += [field[i.number - 1]]
            if i.number + 1 >= 0:
                neighbors_1 += [field[i.number + 1]]
            if i.number - 34 >= 0:
                neighbors_1 += [field[i.number - 34]]
            if i.number + 34 >= 0:
                neighbors_1 += [field[i.number +34]]
            if (i.number // 34) % 2 == 0:
                if i.number - 35 >= 0:
                    neighbors_1 += [field[i.number - 35]]
                if i.number + 33 >= 0:
                    neighbors_1 += [field[i.number + 33]]
            else:
                if i.number + 35 >= 0:
                    neighbors_1 += [field[i.number + 35]]
                if i.number - 33 >= 0:
                    neighbors_1 += [field[i.number - 33]]
                
            for j in neighbors_1:
                for l in self.mass:
                    if j == l:
                        neighbors_1.remove(j)
                j.probability_1 = 0.2
            
                




class Physarum_2:
    def __init__(self, screen, mass, color):
        self.screen = screen
        self.mass = [mass]
        self.color = color

    def draw(self):
        for i in self.mass:
            i.color = self.color

    def probability_of_motion(self):
        neighbors_2 = []
        for i in self.mass:
            if i.number - 1 >= 0:
                neighbors_2 += [field[i.number - 1]]
            if i.number + 1 >= 0:
                neighbors_2 += [field[i.number + 1]]
            if i.number - 34 >= 0:
                neighbors_2 += [field[i.number - 34]]
            if i.number + 34 >= 0:
                neighbors_2 += [field[i.number +34]]
            if (i.number // 34) % 2 == 0:
                if i.number - 35 >= 0:
                    neighbors_2 += [field[i.number - 35]]
                if i.number + 33 >= 0:
                    neighbors_2 += [field[i.number + 33]]
            else:
                if i.number + 35 >= 0:
                    neighbors_2 += [field[i.number + 35]]
                if i.number - 33 >= 0:
                    neighbors_2 += [field[i.number - 33]]
                
            for j in neighbors_2:
                for l in self.mass:
                    if j == l:
                        neighbors_2.remove(j)
                j.probability_2 = 0.2


            


        
def search(click, field):
    minimum = 100000000000
    for i in range(0, len(field)):
        if (field[i].x - click[0])**2 + (field[i].y - click[1])**2 < minimum**2:
            minimum = ((field[i].x - click[0])**2 + (field[i].y - click[1])**2)**0.5
            m = i
    return m




"""Описание игровых параметров (Границ игровой области, FPS"""
border_x = 1196
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
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
WHITE = (255, 255, 255)
VIOLET = (148, 0, 211)



screen = pygame.display.set_mode((border_x, border_y))        
screen.fill(BLACK)
pygame.display.update()
clock = pygame.time.Clock()

click_position = 0

finished_1 = False
finished_2 = True
finished_3 = True



feed = [] #здесь будут храниться данные о корме
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
        new_hexagon = Hexagon(screen, x0, y0, a, i)
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


while not finished_3:
    
    screen.fill(BLACK)
    
    for i in field:
        i.draw()

    physarum_1.draw()
    physarum_2.draw()
            
    for i in feed:
        i.drawf()

    physarum_1.probability_of_motion()
    physarum_2.probability_of_motion()

    clock.tick(FPS)


    
    click_position = pygame.mouse.get_pos()
    choise_hex_number = search(click_position, field)
    field[choise_hex_number].choise()
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished_3 = True
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                new_food = Food(screen, field[choise_hex_number].x, field[choise_hex_number].y, field[choise_hex_number].a)
                feed += [new_food]

            #if event.type == pygame.KEYDOWN:
                #for i in field:
                    #i.show_probability
           

    pygame.display.update()

pygame.quit()

