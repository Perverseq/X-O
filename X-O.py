import random
import time
GAME_FIELD = ['_1_', '_2_', '_3_', '_4_', '_5_', '_6_', '_7_', '_8_', '_9_']
MOVES_LIST = [0, 1, 2, 3, 4, 5, 6, 7, 8]


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
    choosen_cell = int(input())
    try:
        game_field[choosen_cell - 1] = player
        moves_list.pop(choosen_cell)
        time.sleep(1)
        comp_move = random.choice(moves_list)
        game_field[comp_move - 1] = comp
        moves_list.pop(comp_move)
    except:
        print("Ход уже совершен. Выберите другое место.")
        move(game_field, player, comp, moves_list)


def check_winner(game_field, game, player, moves_list):
    for i in range(0, 7, 3):
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

    if not moves_list:
        game = False
        print("Ничья!")
    return game


def main():
    player, comp = choose_symbol()
    print_field(GAME_FIELD)
    game = True
    while game:
        move(GAME_FIELD, player, comp, MOVES_LIST)
        print_field(GAME_FIELD)
        game = check_winner(GAME_FIELD, game, player, MOVES_LIST)


if __name__ == '__main__':
    main()