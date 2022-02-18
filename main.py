import sys

string_cells = '         '
first_line = string_cells[:3]
second_line = string_cells[3:6]
third_line = string_cells[6:9]
cells = [list(first_line), list(second_line), list(third_line)]
print(f"""---------
| {cells[0][0]} {cells[0][1]} {cells[0][2]} |
| {cells[1][0]} {cells[1][1]} {cells[1][2]} |
| {cells[2][0]} {cells[2][1]} {cells[2][2]} |
---------""")


def game_state(table):
    number_of_x = 0
    number_of_o = 0
    for x in table:
        if x == 'X':
            number_of_x += 1
        elif x == 'O':
            number_of_o += 1

    if table[0][0] == table[1][1] == table[2][2] == 'X' or \
            table[0][2] == table[1][1] == table[2][0] == 'X' or \
            table[0][0] == table[1][0] == table[2][0] == 'X' or \
            table[0][1] == table[1][1] == table[2][1] == 'x' or \
            table[0][2] == table[1][2] == table[2][2] == 'X' or \
            table[0][0] == table[0][1] == table[0][2] == 'X' or \
            table[1][0] == table[1][1] == table[1][2] == 'X' or \
            table[2][0] == table[2][1] == table[2][2] == 'X':
        print("X wins")
        sys.exit()
    elif table[0][0] == table[1][1] == table[2][2] == 'O' or \
            table[0][2] == table[1][1] == table[2][0] == 'O' or \
            table[0][0] == table[1][0] == table[2][0] == 'O' or \
            table[0][1] == table[1][1] == table[2][1] == 'O' or \
            table[0][2] == table[1][2] == table[2][2] == 'O' or \
            table[0][0] == table[0][1] == table[0][2] == 'O' or \
            table[1][0] == table[1][1] == table[1][2] == 'O' or \
            table[2][0] == table[2][1] == table[2][2] == 'O':
        print("O wins")
        sys.exit()
    elif string_cells.find(' ') == -1:
        print("Draw")
        sys.exit()
    elif any([cell == ' ' for tables in table for cell in tables]):
        move()
    else:
        print('Draw')
        sys.exit()


def not_num():
    print("You should enter numbers!")
    move()


turn = 0


def move():
    global turn
    coordinates = [eval(x) if x.isdigit() else not_num() for x in input('Enter the coordinates :').strip().split()]
    if len(coordinates) != 2:
        print('You should enter 2 numbers')
        move()
    elif abs(coordinates[0]) > 3 or abs(coordinates[1]) > 3 or coordinates[0] == 0 or coordinates[1] == 0:
        print('Coordinates should be from 1 to 3!')
        move()
    elif cells[coordinates[0] - 1][coordinates[1] - 1] != ' ':
        print('This cell is occupied! Choose another one!')
        move()
    else:
        cells[coordinates[0] - 1][coordinates[1] - 1] = 'X' if turn % 2 == 0 else 'O'
        turn += 1
        print(f"""---------
| {cells[0][0]} {cells[0][1]} {cells[0][2]} |
| {cells[1][0]} {cells[1][1]} {cells[1][2]} |
| {cells[2][0]} {cells[2][1]} {cells[2][2]} |
---------""")
        game_state(cells)


game_state(cells)
