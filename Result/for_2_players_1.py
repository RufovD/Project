from functions_1 import *

def play_2(physarums, finished_1, finished_2, finished_3, screen,
           remainder_of_moves, field, feed_1, feed_2, x0, y0, a):
    """игра против друга. Возвращает данные о полученных грибах **physarum**
    остаток ходов **remainder_of_moves**, данные о игровом поле **field** и данные
    о расставленной еде каждго типа **feed_1**, **feed_2**. Принимает **physarums** -
    еще не заполненный список грибов, переменные окончания **finished_1**,
    **finished_2**, **finished_3**, игровой экран **screen**, количество ходов на
    игру **remainder_of_moves**, данные о игровом поле **field**, данные о еде каждого
    типа **feed_1**, **feed_2**, координаты центра первого гекса **x0**, **y0**,
    длину его стороны **a**"""
    move = 1
    field = field_creation(field, x0, y0, a, screen)
    [physarum_1, finished_1, finished_2, move] = new_mushroom(finished_1, finished_2, screen, field, move, (210, 200, 100))
    if physarum_1 != 0:
        physarum_1.draw()
        [physarum_2, finished_2, finished_3, move] = new_mushroom(finished_2, finished_3, screen, field, move, (120, 200, 125))
        if physarum_2 != 0:
            physarum_2.draw()
            [physarum_1, physarum_2, field] = draw_and_count(physarum_1, physarum_2, finished_3, field)
            while remainder_of_moves != 0:
                [field, finished_3, feed_1, feed_2, physarum_1, physarum_2,
                remainder_of_moves, move] = person_move(screen, field, finished_3, feed_1,
                feed_2, physarum_1, physarum_2, remainder_of_moves, move)
            physarums = [physarum_1, physarum_2]
            if finished_3 == True:
                physarums = [0]
    return [physarums, remainder_of_moves, field, feed_1, feed_2]

if __name__ == "__main__":
    print("Этот модуль не заупускает игру! Запустите файл main!")

    
