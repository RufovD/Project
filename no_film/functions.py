import pygame 
import math
from pygame.draw import *
import random 
pygame.init()

from Hexagon import *
from basic_variables_and_constants import *


#ункция поиска гексаидера, в котором сейчас находится курсор
def search(click, field):
    minimum = 100000000000
    for i in range(0, len(field)):
        if (field[i].x - click[0])**2 + (field[i].y - click[1])**2 < minimum**2:
            minimum = ((field[i].x - click[0])**2 + (field[i].y - click[1])**2)**0.5
            m = i
    return m



#функция финального меню
def winner(win, screen, physarum_1, physarum_2, first_color, second_color):
    text01 = f_01.render('Нажмите стрелочку вверх, чтобы вернуться к полю,', True,
                    (255, 255, 255))
    screen.blit(text01, (20, 150))
    text02 = f_02.render('затем зажмите пробел, чтобы посмотреть вероятности', True,
                    (255, 255, 255))
    screen.blit(text02, (20, 200))
    text03 = f_03.render('Чтобы вернуться к результату, нажмите стрелочку вниз', True,
                    (255, 255, 255))
    screen.blit(text03, (20, 250))
    text05 = f_05.render('клеток захвачено желтым грибом: ' + str(len(physarum_1.mass)) + ', захвачено зеленым грибом: ' + str(len(physarum_2.mass)), True,
                    (255, 255, 255))
    screen.blit(text05, (20, 500))
    
    if win == 1:
        text = f.render('Победил желтый гриб!', True,
                    (first_color))
        screen.blit(text, (20, 20))
    elif win == 2:
        text = f.render('Победил зеленый гриб!', True,
                    (second_color))
        screen.blit(text, (20, 20))
    else:
        text = f.render('Ничья!', True,
                    (255, 255, 255))
        screen.blit(text, (20, 20))



#функция вывода правил игры
def rules(screen):
    screen.fill(BLACK)
    text_05 = f_05.render('В этой игре вам придется взять на себя роль ученого, у которого есть свой собтвенный гриб вида ', True,
                        (255, 255, 255))
    screen.blit(text_05, (5, 20))
    text_06 = f_06.render('свой собтвенный гриб Physarum polycephalum. Именно его судьбой ', True,
                    (255, 255, 255))
    screen.blit(text_06, (5, 50))
    text_07 = f_07.render('вам придется управлять. Для победы вам необходимо захватить как  ', True,
                    (255, 255, 255))
    screen.blit(text_07, (5, 80))
    text_08 = f_08.render('можно большую территорию на поле. Для этого расставляйте еду, ', True,
                    (255, 255, 255))
    screen.blit(text_08, (5, 110))
    text_09 = f_09.render('тем самым увеличивая желание гриба распространяться к ней, а не  ', True,
                     (255, 255, 255))
    screen.blit(text_09, (5, 140))
    text_10 = f_10.render('от нее. Но вот незадача - все придется делать в условиях настоящей', True,
                    (255, 255, 255))
    screen.blit(text_10, (5, 170))
    text_05 = f_05.render('конкуренции - на поле вы не одни, в достижении господства вам бу-', True,
                     (255, 255, 255))
    screen.blit(text_05, (5, 200))
    text_06 = f_06.render('дет мешать гриб соперника. Соревнуйтесь с друзьями или играйте ', True,
                        (255, 255, 255))
    screen.blit(text_06, (5, 230))
    text_07 = f_07.render('против компьтера!', True,
                        (255, 255, 255))
    screen.blit(text_07, (5, 260))
    text_08 = f_08.render('В свой первый ход игроки по очереди нажимают на выбранную клетку и', True,
                        (255, 255, 255))
    screen.blit(text_08, (5, 300))
    text_09 = f_09.render('ставят свой гриб. Далее вся игра происходит пошагово. В ход игрок  ', True,
                        (255, 255, 255))
    screen.blit(text_09, (5, 330))
    text_10 = f_10.render('ставит еду в ЛЮБУЮ выбранную клетку. Еда увеличивает вероят-', True,
                        (255, 255, 255))
    screen.blit(text_10, (5, 360))
    text_05 = f_05.render('ность распространения гриба к себе, уменьшает от себя. Вероятность', True,
                    (255, 255, 255))
    screen.blit(text_05, (5, 390))
    text_06 = f_06.render('в данный момент можно увидеть, зажав пробел. Еда для первого ', True,
                        (255, 255, 255))
    screen.blit(text_06, (5, 420))
    text_07 = f_07.render('(желтого) гриба - красная, для второго (зеленого) - синяя. Вероятнос- ', True,
                        (255, 255, 255))
    screen.blit(text_07, (5, 450))
    text_08 = f_08.render('ти соответствуют цвету еды. Один гриб может поедать клетки с дру-', True,
                    (255, 255, 255))
    screen.blit(text_08, (5, 480))
    text_09 = f_09.render('гим грибом. После установки еды, ее можно переместить, повторно  ', True,
                    (255, 255, 255))
    screen.blit(text_09, (5, 510))
    text_10 = f_10.render('нажав на только что установленную еду и выбрав новую клетку по-. ', True,
                    (255, 255, 255))
    screen.blit(text_10, (5, 540))
    text_05 = f_05.render('ля. Для передачи хода нажмите стрелку вправо на клавиатуре. Игра ', True,
                    (255, 255, 255))
    screen.blit(text_05, (5, 570))
    text_06 = f_06.render('заканчивается после того, как каждый сделает 50 ходов. Победите-', True,
                    (255, 255, 255))
    screen.blit(text_06, (5, 600))
    text_07 = f_07.render('лем объявляется тот, кто захватил своим грибом больше клеток поля.', True,
                    (255, 255, 255))
    screen.blit(text_07, (5, 630))
    text_08 = f_08.render('Нажмите 4, чтобы вернуться в меню.', True,
                    (255, 0, 255))
    screen.blit(text_08, (5, 660))



#функция создания игрового поля
def field_creation(field, x0, y0, a, screen):
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



#функия создания меню
def menu(screen):    
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

    text_04 = f_04.render('3 - узнать правила', True,
                        (255, 255, 255))
    screen.blit(text_04, (20, 320))

    grib_surf = pygame.image.load('grib1.png')

    grib_rect = grib_surf.get_rect(
    bottomright=(border_x, border_y + 20))
    screen.blit(grib_surf, grib_rect)


#функция определения победителя
def determining_the_winner(physarums, win):
    if len(physarums[0].mass) > len(physarums[1].mass):
        win = 1
    elif len(physarums[0].mass) < len(physarums[1].mass):
        win = 2
    else:
        win = 0
    pygame.mixer.music.stop()
    return win


#необходимые текстовые поля
f_01 = pygame.font.Font(None, 50)
f_02 = pygame.font.Font(None, 50)
f_03 = pygame.font.Font(None, 50)
f_04 = pygame.font.Font(None, 140)
f_05 = pygame.font.Font(None, 50)
f_06 = pygame.font.Font(None, 50)
f_07 = pygame.font.Font(None, 50)
f_08 = pygame.font.Font(None, 50)
f_09 = pygame.font.Font(None, 50)
f_10 = pygame.font.Font(None, 50)
f = pygame.font.Font(None, 140)
f_0 = pygame.font.Font(None, 140)
f_3 = pygame.font.Font(None, 140)
