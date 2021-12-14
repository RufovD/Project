from functions_1 import *
from for_1_player_1 import *
from for_2_players_1 import *


class Game:
    def __init__(self):
        self.border_x = 1198
        self.border_y = 700
        self.screen = start(self.border_x, self.border_y)
        self.rule = 0
        self.a = 20 
        self.x0 = 0
        self.y0 = self.a
        self.remainder_of_moves = 4 #всего ходов на партию (остаток ходов)
        self.players = 0 #количество игроков
        self.win = -1 #номер победившего игрока
        self.physarums = [1] #здесь будут конечные данные о грибах
        self.field = []
        self.feed_1 = []
        self.feed_2 = []
        self.flag_1 = False
        self.flag_2 = False
        self.finished_0 = False 
        self.finished_1 = True
        self.finished_2 = True
        self.finished_3 = True

        #запуск меню (одиночная игра с ИИ, игра с другом, правила)
        while not self.finished_0:          
            #отображение самого меню
            if self.rule == 0:
                menu(self.screen, self.border_x, self.border_y)
            #отображение правил
            elif self.rule != 0:
                rules(self.screen)
            pygame.display.update()
            #обработка событий в меню
            [self.finished_0, self.finished_1, self.rule, self.players] = menu_processing(pygame.event.get(),
                                                                                          self.finished_0,
                                                                                          self.finished_1,
                                                                                          self.rule,
                                                                                          self.players)

    def play(self):
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
        if len(self.physarums) == 2:
            self.win = determining_the_winner(self.physarums)
            while self.remainder_of_moves == 0:
                ended_menu_view(self.screen, self.flag_1, self.flag_2, self.field, self.feed_1, self.feed_2, self.win, self.physarums)
                [self.flag_1, self.flag_2, self.remainder_of_moves] = ended_menu_processing(pygame.event.get(), self.flag_1, self.flag_2, self.remainder_of_moves)
        pygame.quit()
                
