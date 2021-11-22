import pygame
import math
from pygame.draw import *
from random import randint
pygame.init()

"""Описание шестиугольных клеток"""
class Hexagon:

    """При создании"""
    def __init__(self, screen, x, y, a):
        self.screen = screen
        self.x = x
        self.y = y
        self.a = a
        self.color = WHITE
        self.food = 0

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

class Food:

    def __init__(self, screen, x, y, a):
        self.screen = screen
        self.x = x
        self.y = y
        self.r = a / 2.5
        self.color = BLUE

    def drawf(self):
        circle(self.screen, self.color, (self.x, self.y), self.r)
            
        
def search(click, field):
    global feed
    minimum = 100000000000
    for i in range(0, len(field)):
        if (field[i].x - click[0])**2 + (field[i].y - click[1])**2 < minimum**2:
            minimum = ((field[i].x - click[0])**2 + (field[i].y - click[1])**2)**0.5
            m = i
    field[m].food += 1
    if field[m].food == 1:
        new_food = Food(screen, field[m].x, field[m].y, field[m].a)
        new_food.drawf()
        feed += [new_food]


"""Описание игровых параметров (Границ игровой области, FPS"""
border_x = 1196
border_y = 700
FPS = 200

"Описание используемых цветов"
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

finished = False

feed = [] #здесь будут храниться данные о корме
field = [] #здесь будут храниться все клетки 

a = 20
x0 = 0
y0 = a

for i in range(0, 23):
    if i % 2 == 0:
        x0 = a * (3**0.5) / 2
    else:
        x0 = a * (3**0.5)        
    for j in range(0, 34):
        new_hexagon = Hexagon(screen, x0, y0, a)
        new_hexagon.draw()
        field += [new_hexagon]
        x0 += new_hexagon.a * (3**0.5)
    y0 += 1.5 * a  




pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    for i in field:
        i.draw()

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                search(event.pos, field)

    for i in feed:
        i.drawf()
    pygame.display.update()

pygame.quit()


