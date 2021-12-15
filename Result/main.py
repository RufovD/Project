from game_1 import *

def main():
    """создает игру, заускает игровую сессию и финальное меню"""
    new_game = Game()
    new_game.play()
    new_game.ended_menu()

if __name__ == "__main__":
    main()




