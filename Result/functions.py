import pygame 
from pygame.draw import *
from objects import *
pygame.init()

def sign(a):
    """возвращает знак чмсла **a** по данному значению числа **a** """
    if a > 0: 
        return 1
    elif a == 0:
        return 0
    else:
        return -1

def search(click, field):
    """возвращает номер гекса **m**, в котором сейчас находиться курсор мыши по
    данным положожнению курсора мыши **click** и параметров поля **field**"""
    minimum = 100000000000
    m = -1
    for i in range(0, len(field)):
        if (field[i].x - click[0])**2 + (field[i].y - click[1])**2 < minimum**2:
            minimum = ((field[i].x - click[0])**2 + (field[i].y - click[1])**2)**0.5
            m = i 
    return m

def winner(win, screen, physarum_1, physarum_2):
    """выводит на экран **screen** победителя, взяв номер победившего игрока
    **win** и количество захваченных грибами клеток по параметрам каждого гриба:
    **physarum_1** и **physarum_2**"""
    text01 = f_01.render('Нажмите стрелочку вверх, чтобы вернуться к полю,', True,
                    (255, 255, 255))
    screen.blit(text01, (20, 150))
    text02 = f_02.render('затем зажмите пробел, чтобы посмотреть вероятности', True,
                    (255, 255, 255))
    screen.blit(text02, (20, 200))
    text03 = f_03.render('Чтобы вернуться к результату, нажмите стрелочку вниз', True,
                    (255, 255, 255))
    screen.blit(text03, (20, 250))
    text05 = f_05.render('жёлтый гриб захватил клеток: ' + str(len(physarum_1.mass)) + ',   зелёный гриб захватил: ' + str(len(physarum_2.mass)), True,
                    (255, 255, 255))
    screen.blit(text05, (20, 500))
    
    if win == 1:
        text = f.render('Победил желтый гриб!', True,
                        (250, 165, 10))
        screen.blit(text, (20, 20))
    elif win == 2:
        text = f.render('Победил зеленый гриб!', True,
                        (0, 255, 0))
        screen.blit(text, (20, 20))
    else:
        text = f.render('Ничья!', True,
                        (255, 255, 255))
        screen.blit(text, (20, 20))
        
def rules(screen):
    """выводит правила игры на экран **screen**"""
    screen.fill((0, 0, 0))
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

def field_creation(field, x0, y0, a, screen):
    """возвращает параметры игрового поля **field** в заданную переменную **field**,
    создавая поле гексов на экране **screen** с начальным центром **x0** и **y0**
    каждый со стороной **a**"""
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
    return field

def menu(screen, border_x, border_y):    
    """отображает на экране **screen** с границами **border_x** и **border_y**
    правила и картинку с грибом"""
    screen.fill((0, 0, 0))
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

    grib_surf = pygame.image.load('grib.png')

    grib_rect = grib_surf.get_rect(
    bottomright=(border_x, border_y + 20))
    screen.blit(grib_surf, grib_rect)

def determining_the_winner(physarums):
    """возрвращает номер победившего игрока или ноль в слычае ничьи по конечным
    параметрам грибов - списка **physarums**"""
    if len(physarums[0].mass) > len(physarums[1].mass):
        return 1
    elif len(physarums[0].mass) < len(physarums[1].mass):
        return 2
    else:
        return 0

def menu_processing(events, finished_0, finished_1, rule, players):
    """обрабатывает действия игрока в меню, по заданным событиям в пайгейме **events**
    берет **finished_0**, **finished_1** - два параметра окончания, **rule**, который
    показывает, отображать ли правила и количество игроков **players**, возвращает
    пересчитанные значения **finished_0**, **finished_1**, **rule** и **players**"""
    for event in events:
        if event.type == pygame.QUIT:
            finished_0 = True
        else:
            if (event.type == pygame.KEYDOWN) and (rule == 0):
                if event.key == pygame.K_1:
                    finished_0 = True
                    players = 1
                    finished_1 = False
                elif event.key == pygame.K_2:
                    finished_0 = True
                    players = 2
                    finished_1 = False
                elif event.key == pygame.K_3:
                    rule = 1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_4:
                    rule = 0
    return [finished_0, finished_1, rule, players]

def start(border_x, border_y):
    """начало игроввой сессии, по заданным границам экрана **border_x** и **border_y**
    создает и возвращает залитый черным экран **screen**"""
    screen = pygame.display.set_mode((border_x, border_y))        
    screen.fill((0, 0, 0))
    return screen

def ended_menu_view(screen, flag_1, flag_2, field, feed_1, feed_2, win, physarums):
    """отображает финальное меню. На заданном экране **screen** отображает финальное игровое
    положение на заданном поле **field** , если заданная переменная **flag_1** = True, при
    заданной **flag_2** равной True отображаются вероятности распространения грибов при False
    отображается расположение еды **food_1** и **food_2**, при **flag_1** = False отображается
    победитель по его заданному номеру **win** и масса захваченных грибами клеток по данному
    **physarum**"""
    screen.fill((0, 0, 0))
    if flag_1:
        for i in field:
            i.draw()
        if flag_2:
            for j in field:
                j.show_probability()
        else:
            for j in field:
                j.show_food()
            for j in feed_1:
                j.drawf()
            for j in feed_2:
                j.drawf()
    else:
        winner(win, screen, physarums[0], physarums[1])

def ended_menu_processing(events, flag_1, flag_2, remainder_of_moves):
    """обработка событий в финальном меню. По заданным событиям из пайгейма **events**
    и пересчитываются значения **flag_1**, **flag_2** и **remainder_of_moves** они же и
    возвращаются"""
    for event in events:
        if event.type == pygame.QUIT:
            remainder_of_moves = -1
        else:
            if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            flag_1 = True
                        elif event.key == pygame.K_DOWN:
                            flag_1 = False
                        elif event.key == pygame.K_SPACE:
                            flag_2 = True
            if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        flag_2 = False
    pygame.display.update()
    return [flag_1, flag_2, remainder_of_moves]

def new_mushroom(finished_1, finished_2, screen, field, move, color):
    """игрок ставит новый гриб. Пересчитываются значения по данным **finihsed_1** и
    **finished_2**, на заданном экране **screen** создается и возвращается гриб
    **physarum** заданного цвета **color** в одной из клетки заданного поля **field**.
    По заданному move возвращается **move**, передавая очередь хода."""
    while not finished_1:
        screen.fill((0, 0, 0))
        for i in field:
            i.draw()
        click_position = pygame.mouse.get_pos()
        choice_hex_number = search(click_position, field)
        field[choice_hex_number].choice(move)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished_1 = True
                physarum = 0
            else:
                if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (field[choice_hex_number].color == (255, 255, 255)):
                    physarum = Physarum(screen, field[choice_hex_number], color) 
                    finished_1 = True
                    finished_2 = False
                    move = move * (-1)
        pygame.display.update()
    return [physarum, finished_1, finished_2, move]

def computer_new_mushroom(screen, field, move):
    """на заданном экране **screen** в заданном игровом поле **field** компьютер
    устанавливает гриб. Возвращаются данные о грибе **physarum**, пересчитаннная
    по заданной очередность хода **move**, созданный объект **computer** и значения
    True и False"""
    computer = Artificial_intelligence()
    d = 0
    move = 1
    while d == 0:
        d = computer.beginning(field)
        if field[d].color == (255, 255, 255):
            physarum = Physarum(screen, field[d], (120, 200, 125))
        else:
            d = 0
    print(len(physarum.mass))
    return [physarum, move, True, False, computer]

def draw_and_count(physarum_1, physarum_2, finished_3, field):
    """по заданным **physarum_1** и **physarum_2**, **field** и *finished_3**
    рисует на гексах грибы и пересчитывает соседей грибов. Возвращает **physarum_1**,
    **physarum_2** и **field**"""
    if not finished_3:
        for i in field:
            i.probability_1 = 0
            i.probability_2 = 0
        physarum_1.draw()
        physarum_2.draw()    
        physarum_1.neighbors = physarum_1.probability_of_motion(field)
        physarum_2.neighbors = physarum_2.probability_of_motion(field)
    return [physarum_1, physarum_2, field]

def early_victory(physarum_1, physarum_2, remainder_of_moves):
    """функция определяет, произошла ли досрочная победа. Принимает **physarum_1**
    и **physarum_2** и **remainder_of_moves** и возвращает то же количесто
    **remainder_of_moves**, если множество клеток, принадлежащих каждому из грибов
    не пусто, или возвращает **remainder_of_moves** = 0 в противном случае"""
    if (len(physarum_1.mass) == 0) or (len(physarum_2.mass) == 0):
        remainder_of_moves = 0
    return remainder_of_moves

def put_food(screen, event, move, feed, physarum_1, physarum_2, finished_3, field, hex_with_new_food, choice_hex_number, d):
    """функция установки еды на поле игроком. Принимает **screnn**, на котором будет установлена еда,
    **event** - события из пайгейма, **move** - параметр, определяющий номер ходящего игрока, **feed** -
    исписок еды, который нужно заполнить новой едой, **physarum_1**, **physarum_2** - сведения о грибах,
    **finished_3** - параметр окончания, **field** - информация о поле, **hex_with_new_food** - номер гекса
    для установки еды, **choise_number** - выбранный мышкой гекс, **d** - параметр, определяющий, было ли
    совершено какое-либо действие в этот ход. Возвращает переходящий в фазу подтверждения хода **move**,
    **feed** с новой едой, пресчитанные данные о грибых **physarum_1** и **physarum_2**, о поле **field**,
    номере гекса с положенной едой **hex_with_new_food** и парамнетр совершения действия *d**"""
    if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and ((move == 1) or (move == -2)) and (d == 0):
        if move == 1:
            new_food = Food(screen, field[choice_hex_number].x - field[choice_hex_number].a / 2.5,
                            field[choice_hex_number].y, field[choice_hex_number].a, (255, 0, 0) )
            field[choice_hex_number].food_1 += 1
        elif move == -2:
            new_food = Food(screen, field[choice_hex_number].x + field[choice_hex_number].a / 2.5,
                                    field[choice_hex_number].y, field[choice_hex_number].a, (0, 0, 255))
            field[choice_hex_number].food_2 += 1
        hex_with_new_food = field[choice_hex_number]
        feed += [new_food]
        move = 11 * move
        [physarum_1, physarum_2, field] = draw_and_count(physarum_1, physarum_2, finished_3, field)
        d = 1
    return [move, feed, physarum_1, physarum_2, field, hex_with_new_food, d]

def food_back(event, move, hex_with_new_food, choice_hex_number, feed, physarum_1, physarum_2, finished_3, field, d):
    """позволяет забрать только что положенную еду. Принимает событие из пайгейма **event**, очередность хода
    **move**, гекс, в который была положена последняя еда **hex_with_new_food**, номер гекса, в котором находится
    курсор **choice_hex_number**, данные о еде **feed**, данные о грибах **physarum_1**, physarum_2**, параметр
    окончания **finished_3**, данные о поле **field**, параметр действия за ход **d**. Возвращает пересчитанные
    принимаемые параметры кроме **event**"""
    if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and ((move == 11) or (move == -22)) and (field[choice_hex_number] == hex_with_new_food) and (d == 0):
        if move == 11:
            move = 1
            hex_with_new_food.food_1 += -1
        elif move == -22:
            move = -2
            hex_with_new_food.food_2 += -1
        hex_with_new_food = -1
        feed.pop(-1)
        d = 1
        [physarum_1, physarum_2, field] = draw_and_count(physarum_1, physarum_2, finished_3, field)
    return [move, hex_with_new_food, feed, physarum_1, physarum_2, finished_3, field, d]

def verification(event, move, hex_with_new_food, physarum_1, physarum_2, field, finished_3, remainder_of_moves, d):
    """подтверждение хода. Принимает событие из пайгейма **event**, очередность хода **move**, гекс, в который
    была положена последняя еда **hex_with_new_food**, номер гекса, в котором находится, данные о грибах
    **physarum_1**, physarum_2**, параметр окончания **finished_3**, данные о поле **field**, остаток ходов до
    конца игры **remainder_of_moves**, параметр действия за ход **d**. Возвращает пересчитанные **move**,
    **hex_with_new_food**, **physarum_1**, **physarum_2**, **field**, **remainder_of_moves**, **d**"""
    if (event.type == pygame.KEYDOWN) and ((move == 11) or (move -22)) and (event.key == pygame.K_RIGHT) and (d == 0) and (hex_with_new_food != -1):
        hex_with_new_food = -1
        if move == 11:
            move = -2
            physarum_1.rise()             
            physarum_2.eating(physarum_1)
            for j in physarum_2.mass:
                if j.color != (120, 200, 125):
                    physarum_2.mass.remove(j)
        elif move == -22:
            move = 1
            physarum_2.rise()             
            physarum_1.eating(physarum_2)
            for j in physarum_1.mass:
                if j.color != (210, 200, 100):
                    physarum_2.mass.remove(j)
        draw_and_count(physarum_1, physarum_2, finished_3, field)
        remainder_of_moves += -1
        d = 1
    return [move, hex_with_new_food, physarum_1, physarum_2, field, remainder_of_moves, d]

def person_move(screen, field, finished_3, feed_1, feed_2, physarum_1, physarum_2, remainder_of_moves, move):
    """полный ход игрока от установки еды до подтверждения хода. Принимает 'экран **screen**, информацию
    о игровом поле **field**, параметр окончания **finished_3**, данные о еде каждого вида **feed_1**,
    **feed_2**, данные о грибах **physarum_1**, **physarum_2**, остаток ходов до конца игры **remainder_of_moves**,
    очередность хода **move**. Возвращает пересчитанные **field**, **finished_3**, **feed_1**, **feed_2**,
    **physarum_1**, **physarum_2**, **remainder_of_moves** и **move** """
    m = move
    surface = False
    hex_with_new_food = -1
    while (sign(move) == sign(m)):
        d = 0
        screen.fill((0, 0, 0))
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
            if hex_with_new_food != -1:
                hex_with_new_food.unconfirmed_move()
            click_position = pygame.mouse.get_pos()
            choice_hex_number = search(click_position, field)
            field[choice_hex_number].choice(move)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished_3 = True
                move = move * (-1)
                remainder_of_moves = 0
            else:
                [move, feed_1, physarum_1, physarum_2, field, hex_with_new_food, d] = put_food(screen, event, move, feed_1, physarum_1, physarum_2, finished_3, field, hex_with_new_food, choice_hex_number, d)
                [move, feed_2, physarum_1, physarum_2, field, hex_with_new_food, d] = put_food(screen, event, move, feed_2, physarum_1, physarum_2, finished_3, field, hex_with_new_food, choice_hex_number, d)
                [move, hex_with_new_food, feed_1, physarum_1, physarum_2, finished_3, field, d] = food_back(event, move, hex_with_new_food, choice_hex_number, feed_1, physarum_1, physarum_2, finished_3, field, d)
                [move, hex_with_new_food, physarum_1, physarum_2, field, remainder_of_moves, d] = verification(event, move, hex_with_new_food, physarum_1, physarum_2, field, finished_3, remainder_of_moves, d)                
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        surface = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        surface = False
                
        pygame.display.update()                
    remainder_of_moves = early_victory(physarum_1, physarum_2, remainder_of_moves)
    return [field, finished_3, feed_1, feed_2, physarum_1, physarum_2, remainder_of_moves, move]

def computer_move(screen, field, finished_3, feed_2, physarum_1, physarum_2, computer, remainder_of_moves, move):
    """ход компьютера. Принимает игровой экран **screen**, данные о поле **field**, параметр окончания
    **finished_3**, данные о еде компьютера, **feed_2**, данные о грибах **physarum_1**, **physarum_2**,
    объект **computer**, остаток ходов **remainder_of_moves**, параметр очередности хода **move**. Возвращает
    пересчитанные **field**, **feed_2**, **physarum_1**, **physarum_2**, **remainder_of_moves**, **move**"""
    computer.search(field, physarum_2)
    new_food = Food(screen, field[computer.computer_choice].x + field[computer.computer_choice].a / 2.5,
                    field[computer.computer_choice].y, field[computer.computer_choice].a, (0, 0, 255))
    field[computer.computer_choice].food_2 += 1
    feed_2 += [new_food]
    move = 1
    [physarum_1, physarum_2, field] = draw_and_count(physarum_1, physarum_2, finished_3, field) 
    physarum_2.rise()
    physarum_1.eating(physarum_2)
    for j in physarum_1.mass:
        if j.color != (210, 200, 100):
            physarum_1.mass.remove(j)
    [physarum_1, physarum_2, field] = draw_and_count(physarum_1, physarum_2, finished_3, field)    
    remainder_of_moves += -1
    screen.fill((0, 0, 0))
    for i in field:
        i.draw()
    pygame.display.update()
    remainder_of_moves = early_victory(physarum_1, physarum_2, remainder_of_moves)
    return [field, feed_2, physarum_1, physarum_2, remainder_of_moves, move]

"""необходимые текстовые поля"""
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

if __name__ == "__main__":
    print("Этот модуль не заупускает игру! Запустите файл main!")

    
