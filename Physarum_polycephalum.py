import pygame 
import math
from pygame.draw import *
import random
import cv2

pygame.init()

from Hexagon import *
from Food import *
from Physarum_1 import *
from Physarum_2 import *
from Artificial_intelligence import *
from functions import *
from basic_variables_and_constants import *
from for_1_player import *
from for_2_players import *


screen = pygame.display.set_mode((border_x, border_y))        
screen.fill(BLACK)
pygame.display.update()
clock = pygame.time.Clock()

music_off = True


#создание игрового поля
field_creation(field, x0, y0, a, screen)
pygame.display.update()
clock = pygame.time.Clock()

#загрузка превью и начальной музыки
video_name = "Music & Video/Physarum_Polycephalum.mp4"
cap = cv2.VideoCapture(video_name)
ret, img = cap.read()
#print(ret) #видео захвачено нормально, если ret == True
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.resize(img, (border_x, border_y))
img = cv2.transpose(img)
surf = pygame.surface.Surface((img.shape[0], img.shape[1]))

pygame.mixer.music.load("Music & Video/Refraction 1.33.mp3")
pygame.mixer.music.play(-1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            running = False
            break
        if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
            music_off = not music_off
            if music_off:
                pygame.mixer.music.pause()
            else:
                pygame.mixer.music.unpause()
            
    ret, img = cap.read()
    if not ret:
        running = False
        break
    else:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (border_x, border_y))
        img = cv2.transpose(img)
        pygame.surfarray.blit_array(surf, img)
        screen.blit(surf, (0, 0))

    pygame.display.flip()
    clock.tick(FPS)


#запуск меню (одиночная игра с ИИ, игра с другом, правила)
while not finished_0:

    #отображение самого меню
    if rule == 0:
        menu(screen)

    #отображение правил
    if rule != 0:
        rules(screen)

            
    pygame.display.update()

    #обработка действий в меню
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished_0 = True
        else:
            if (event.type == pygame.KEYDOWN) and (rule == 0):
                if event.key == pygame.K_1:
                    finished_0 = True
                    players = 1
                    finished_1 = False
            if (event.type == pygame.KEYDOWN) and (rule == 0):
                if event.key == pygame.K_2:
                    finished_0 = True
                    players = 2
                    finished_1 = False
            if (event.type == pygame.KEYDOWN) and (rule == 0):
                if event.key == pygame.K_3:
                    rule = 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_4:
                    rule = 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                music_off = not music_off
                if music_off:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()


    
first_run = True




#запуск одиночной игры (против ИИ)
if players == 1:
    physarums = play_1(finished_1, finished_2, finished_3, screen, clock, move, surface, feed_1, feed_2,
           hex_with_new_food, remainder_of_moves)
    if len(physarums) == 2:
        finished_4 = False



#запуск игры (с другом)
if players == 2:
    physarums = play_2(finished_1, finished_2, finished_3, screen, clock, move, surface, feed_1, feed_2,
           hex_with_new_food, remainder_of_moves)
    if len(physarums) == 2:
        finished_4 = False


#если игра завершилась, то функция определит победителя
if not finished_4:
    win = determining_the_winner(physarums, win)
    
#отображение результатов игры (финальное меню)
while not finished_4:

    screen.fill(BLACK)

    #отображает конечное игровое поле с грибами, едой и возможностью посмотреть вероятности при нажатии пробела
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

    #показывает победителя и количесвто захваченных каждым игроком клеток
    else:
        winner(win, screen, physarums[0], physarums[1], DARK_YELLOW_2, GREEN) 
        
    
    #обработка событий в финальном меню
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

