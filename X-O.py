GAME_FIELD = ('_1_', '_2_', '_3_', '_4_', '_5_', '_6_', '_7_', '_8_', '_9_')
MOVES_LIST = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def print_field(game_field):
    first_line = '|'.join(game_field[0:3])
    second_line = '|'.join(game_field[3:6])
    third_line = '|'.join(game_field[6:9])
    print(first_line)
    print(second_line)
    print(third_line)

