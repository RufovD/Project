from functions_1 import *
from for_1_player_1 import *
from for_2_players_1 import *

class Game:
    """Тип данный, описывающих саму игру"""
    
    def __init__(self):
        self.border_x = 1198
        """икс граница экрана"""
        
        self.border_y = 700
        """игрек граница экрана"""
        
        self.screen = start(self.border_x, self.border_y)
        """создание экрана с границами"""
        
        self.rule = 0
        """параметр отображения правил"""
        
        self.a = 20
        """длина стороны гекса"""
        
        self.x0 = 0
        """координата перого центра гекса по икс"""
        
        self.y0 = self.a
        """координата первого гекса по игрек"""
        
        self.remainder_of_moves = 100
        """всего ходов на партию (остаток ходов)"""
        
        self.players = 0
        """количество игроков"""
        
        self.win = -1
        """номер победившего игрока"""
        
        self.physarums = [1]
        """здесь будут конечные данные о грибах"""
        
        self.field = []
        """здесь будут храниться данные о игровом поле"""
        
        self.feed_1 = []
        """здесь будут храниться даннее о еде первого гриба"""
        
        self.feed_2 = []
        """здесь будут храниться данные о еде второго игрока"""
        
        self.flag_1 = False
        """некоторый флаг для финального меню"""
        
        self.flag_2 = False
        """еще один флаг для финального меню"""
        
        self.finished_0 = False
        """некоторый параметр окончания"""
        
        self.finished_1 = True
        """некоторый параметр окончания"""

        self.finished_2 = True
        """некоторый параметр окончания"""
        
        self.finished_3 = True
        """некоторый параметр окончания"""

        while not self.finished_0:
            """запуск меню"""
            if self.rule == 0:
                menu(self.screen, self.border_x, self.border_y)
            elif self.rule != 0:
                rules(self.screen)
            pygame.display.update()
            [self.finished_0, self.finished_1, self.rule, self.players] = menu_processing(pygame.event.get(),
                                                                                          self.finished_0,
                                                                                          self.finished_1,
                                                                                          self.rule,
                                                                                          self.players)

    def play(self):
        """начало игрового процесса. По выбранному количеству игроков **self.players**
        оздает игровую сессию на 1 или 2 игроков"""
        if self.players == 1:
            [self.physarums, self.remainder_of_moves, self.field, self.feed_1, self.feed_2] = play_1(self.physarums, self.finished_1, self.finished_2,
                                                                                                     self.finished_3, self.screen,
                                                                                                     self.remainder_of_moves, self.field,
                                                                                                     self.feed_1, self.feed_2, self.x0, self.y0, self.a)
        elif self.players == 2:
            [self.physarums, self.remainder_of_moves, self.field, self.feed_1, self.feed_2] = play_2(self.physarums, self.finished_1, self.finished_2,
                                                                                                     self.finished_3, self.screen,
                                                                                                     self.remainder_of_moves, self.field,
                                                                                                     self.feed_1, self.feed_2, self.x0, self.y0, self.a)

    def ended_menu(self):
        """запуск финального меню. Если данные о грибах **self.physarum** заполнены,
        то определяется победитель и выводится результат игры. Так же можно посмттреть
        финальную ситуацию на игрвовом поле """
        if len(self.physarums) == 2:
            self.win = determining_the_winner(self.physarums)
            while self.remainder_of_moves == 0:
                ended_menu_view(self.screen, self.flag_1, self.flag_2, self.field,
                                self.feed_1, self.feed_2, self.win, self.physarums)
                [self.flag_1, self.flag_2, self.remainder_of_moves] = ended_menu_processing(pygame.event.get(),
                                                                                            self.flag_1, self.flag_2,
                                                                                            self.remainder_of_moves)
        pygame.quit()
                
if __name__ == "__main__":
    print("Этот модуль не заупускает игру! Запустите файл main!")

    
