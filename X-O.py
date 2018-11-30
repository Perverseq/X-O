import random
#import time


def print_field(game_field):
    first_line = '|'.join(game_field[0:3])
    second_line = '|'.join(game_field[3:6])
    third_line = '|'.join(game_field[6:9])
    print(first_line)
    print(second_line)
    print(third_line)


def choose_symbol():
    print("Choose your destiny (x/o)")
    player = str(input())
    if player == 'x' or 'X':
        player = '_X_'
        comp = '_O_'
    elif player == 'o' or 'O':
        player = '_O_'
        comp = '_X_'
    else:
        print("Вы ввели неверное значение")
        choose_symbol()
    return player, comp


def move(game_field, player, comp, moves_list):
    print("Выберите, куда сходить")
    #print_field(game_field)
    choosen_cell = int(input())
    try:
        game_field[choosen_cell - 1] = player
        moves_list.remove(choosen_cell)
        #time.sleep(1)
        if moves_list:
            comp_move = random.choice(moves_list)
            game_field[comp_move - 1] = comp
            moves_list.remove(comp_move)
        else:
            pass
    except:
        print("Ход уже совершен. Выберите другое место.")
        move(game_field, player, comp, moves_list)


def check_winner(game_field, game, player, moves_list):
    try:
        for i in range(0, 6, 3):
            if game_field[i] == game_field[i + 1] == game_field [i + 2]:
                game = False
                if game_field[i] == player:
                    print("Вы победили!")
                else:
                    print("Вы проиграли!")
        for i in range(3):
            if game_field[i] == game_field[i + 3] == game_field[i + 6]:
                game = False
                if game_field[i] == player:
                    print("Вы победили!")
                else:
                    print("Вы проиграли!")
        if game_field[0] == game_field[4] == game_field[8]:
            game = False
            if game_field[0] == player:
             print("Вы победили!")
            else:
             print("Вы проиграли!")
        if game_field[2] == game_field[4] == game_field[6]:
            game = False
            if game_field[2] == player:
             print("Вы победили!")
            else:
                print("Вы проиграли!")
    except:
        if not moves_list:
            game = False
            print("Ничья!")
    return game


def main():
    game_field = ['_1_', '_2_', '_3_', '_4_', '_5_', '_6_', '_7_', '_8_', '_9_']
    moves_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    player, comp = choose_symbol()
    print_field(game_field)
    game = True
    while game:
        move(game_field, player, comp, moves_list)
        print_field(game_field)
        game = check_winner(game_field, game, player, moves_list)


if __name__ == '__main__':
    main()
