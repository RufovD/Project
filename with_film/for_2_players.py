import pygame 
import math
from pygame.draw import *
import random 
pygame.init()

from Hexagon import *
from Food import *
from Physarum_1 import *
from Physarum_2 import *
from Artificial_intelligence import *
from functions import *
from basic_variables_and_constants import *


#игра с другом
def play_2(finished_1, finished_2, finished_3, screen, clock, move, surface, feed_1, feed_2,
           hex_with_new_food, remainder_of_moves):

    first_run = True

    #размещение желтого гриба
    while not finished_1:

        screen.fill(BLACK)
        
        for i in field:
            i.draw()


        clock.tick(FPS)

        click_position = pygame.mouse.get_pos()
        choice_hex_number = search(click_position, field)
        field[choice_hex_number].choice(finished_1, finished_2, move)

        if first_run:
            pygame.mixer.music.load("Music & Video/Rip & Tear.mp3")
            pygame.mixer.music.play(-1)
            music_off = False
            first_run = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished_1 = True
            else:
                if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                    physarum_1 = Physarum_1(screen, field[choice_hex_number], YELLOW_1) 
                    physarum_1.probability_of_motion(field)
                    finished_1 = True
                    finished_2 = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        music_off = not music_off
                        if music_off:
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.unpause()
        pygame.display.update()

    #размещение зеленого гриба
    while not finished_2:

        screen.fill(BLACK)
        
        for i in field:
            i.draw()

        physarum_1.draw()
        
        clock.tick(FPS)

        click_position = pygame.mouse.get_pos()
        choice_hex_number = search(click_position, field)
        if field[choice_hex_number] != physarum_1.mass[0]:
            field[choice_hex_number].choice(finished_1, finished_2, move)
        else:
            choice_hex_number = "1"

      
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished_2 = True
            else:
                if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (choice_hex_number != "1"):
                    physarum_2 = Physarum_2(screen, field[choice_hex_number], GREEN_1)
                    finished_2 = True
                    finished_3 = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        music_off = not music_off
                        if music_off:
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.unpause()

        pygame.display.update()

    if not finished_3:
        physarum_1.draw()
        physarum_2.draw()
        physarum_1.neighbors_1 = physarum_1.probability_of_motion(field)
        physarum_2.neighbors_2 = physarum_2.probability_of_motion(field)

    #расстановка еды
    while not finished_3:

        if (len(physarum_1.mass) == 0) or (len(physarum_2.mass) == 0):
            finished_3 = True
            finished_4 = False
            pygame.mixer.music.stop()
            return [physarum_1, physarum_2]
        
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
        field[choice_hex_number].choice(finished_1, finished_2, move)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished_3 = True
            else:

                #еду ставит 1 игрок
                if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (move == 1):
                    new_food = Food(screen, field[choice_hex_number].x - field[choice_hex_number].a / 2.5,
                                    field[choice_hex_number].y, field[choice_hex_number].a, RED )
                    field[choice_hex_number].food_1 += 1
                    hex_with_new_food = field[choice_hex_number]
                    feed_1 += [new_food]
                    move = 11
                    for i in field:
                        i.probability_1 = 0
                        i.probability_2 = 0
                    physarum_1.neighbors_1 = physarum_1.probability_of_motion(field)
                    physarum_2.neighbors_2 = physarum_2.probability_of_motion(field)

                #он может передумать и забрать еду
                elif (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (move == 11) and (field[choice_hex_number] == hex_with_new_food):
                    hex_with_new_food.food_1 += -1
                    hex_with_new_food = 0
                    feed_1.pop(-1)
                    move = 1
                    for i in field:
                        i.probability_1 = 0
                        i.probability_2 = 0
                    physarum_1.neighbors_1 = physarum_1.probability_of_motion(field)
                    physarum_2.neighbors_2 = physarum_2.probability_of_motion(field)

                #1 игрок поддтвержает свой ход
                elif (event.type == pygame.KEYDOWN) and (move == 11) and (event.key == pygame.K_RIGHT):
                    hex_with_new_food = 0
                    move = -2
                    physarum_1.rise()

                        
                    physarum_2.eating(physarum_1)
                    for j in physarum_2.mass:
                        if j.color != GREEN_1:
                            physarum_2.mass.remove(j)
                    
                        
                    for i in field:
                        i.probability_1 = 0
                        i.probability_2 = 0
                    physarum_1.neighbors_1 = physarum_1.probability_of_motion(field)
                    physarum_2.neighbors_2 = physarum_2.probability_of_motion(field)
                    
                    
                    

                #еду ставит 2 игрок
                elif (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (move == -2):
                    new_food = Food(screen, field[choice_hex_number].x + field[choice_hex_number].a / 2.5,
                                    field[choice_hex_number].y, field[choice_hex_number].a, BLUE)
                    field[choice_hex_number].food_2 += 1
                    feed_2 += [new_food]
                    hex_with_new_food = field[choice_hex_number]
                    move = -22
                    for i in field:
                        i.probability_1 = 0
                        i.probability_2 = 0
                    physarum_1.neighbors_1 = physarum_1.probability_of_motion(field)
                    physarum_2.neighbors_2 = physarum_2.probability_of_motion(field)
                    
                #он может передумать и забрать еду
                elif (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (move == -22) and (field[choice_hex_number] == hex_with_new_food):
                    hex_with_new_food.food_2 += -1
                    hex_with_new_food = 0
                    feed_2.pop(-1)
                    move = -2
                    for i in field:
                        i.probability_1 = 0
                        i.probability_2 = 0
                    physarum_1.neighbors_1 = physarum_1.probability_of_motion(field)
                    physarum_2.neighbors_2 = physarum_2.probability_of_motion(field)

                    
                #2 игрок поддтвержает свой ход
                elif (event.type == pygame.KEYDOWN) and (move == -22) and (event.key == pygame.K_RIGHT):
                    hex_with_new_food = 0
                    move = 1
                    physarum_2.rise()

                    
                    physarum_1.eating(physarum_2)
                    for j in physarum_1.mass:
                        if j.color != YELLOW_1:
                            physarum_1.mass.remove(j)
                    
                    for i in field:
                        i.probability_1 = 0
                        i.probability_2 = 0
                    physarum_1.neighbors_1 = physarum_1.probability_of_motion(field)
                    physarum_2.neighbors_2 = physarum_2.probability_of_motion(field)

                    remainder_of_moves += -1
                    if remainder_of_moves <= 0:
                        finished_3 = True
                        finished_4 = False
                        pygame.mixer.music.stop()
                        return [physarum_1, physarum_2] 


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        surface = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        surface = False

                if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                    music_off = not music_off
                    if music_off:
                         pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()

        pygame.display.update()

    return [1]           
