# write your code here
def is_impossible(cells):
    x_num = cells.count("X")
    o_num = cells.count("O")
    diff = abs(x_num - o_num)
    if diff > 1:
        return True
    elif is_x_win(cells) and is_o_win(cells):
        return True
    else:
        return False


def is_x_win(cells):
    if (("X" == cells[0] == cells[1] == cells[2])
            or ("X" == cells[3] == cells[4] == cells[5])
            or ("X" == cells[6] == cells[7] == cells[8])
            or ("X" == cells[0] == cells[3] == cells[6])
            or ("X" == cells[1] == cells[4] == cells[7])
            or ("X" == cells[2] == cells[5] == cells[8])
            or ("X" == cells[0] == cells[4] == cells[8])
            or ("X" == cells[2] == cells[4] == cells[6])):
        return True
    else:
        return False


def is_o_win(cells):
    if (("O" == cells[0] == cells[1] == cells[2])
            or ("O" == cells[3] == cells[4] == cells[5])
            or ("O" == cells[6] == cells[7] == cells[8])
            or ("O" == cells[0] == cells[3] == cells[6])
            or ("O" == cells[1] == cells[4] == cells[7])
            or ("O" == cells[2] == cells[5] == cells[8])
            or ("O" == cells[0] == cells[4] == cells[8])
            or ("O" == cells[2] == cells[4] == cells[6])):
        return True
    else:
        return False


def is_finished(cells):
    x_num = cells.count("X")
    o_num = cells.count("O")
    total = x_num + o_num
    return total == 9


def is_draw(cells):
    if is_finished(cells) and not is_x_win(cells) and not is_o_win(cells):
        return True
    else:
        return False


def has_space(coordinates):
    return coordinates.find(' ') > -1


def are_numbers(coordinates):
    if not has_space(coordinates):
        return False
    first_string = coordinates.split(" ")[0]
    second_string = coordinates.split(" ")[1]
    try:
        first_number = int(first_string)
        second_number = int(second_string)
        return [first_number, second_number]
    except ValueError:
        return False


def are_one_to_three(numbers):
    return 1 <= numbers[0] <= 3 and 1 <= numbers[1] <= 3


def to_cell_index(numbers):
    if numbers == [1, 1]:
        return 6
    elif numbers == [1, 2]:
        return 3
    elif numbers == [1, 3]:
        return 0
    elif numbers == [2, 1]:
        return 7
    elif numbers == [2, 2]:
        return 4
    elif numbers == [2, 3]:
        return 1
    elif numbers == [3, 1]:
        return 8
    elif numbers == [3, 2]:
        return 5
    elif numbers == [3, 3]:
        return 2
    else:
        return False


def print_cells(cells):
    print("---------")
    print("| %s %s %s |" % (cells[0], cells[1], cells[2]))
    print("| %s %s %s |" % (cells[3], cells[4], cells[5]))
    print("| %s %s %s |" % (cells[6], cells[7], cells[8]))
    print("---------")


def require_input(cells, x_turn):
    while True:
        coordinates_input = input("Enter the coordinates: ")
        if not are_numbers(coordinates_input):
            print("You should enter numbers!")
        else:
            numbers_input = are_numbers(coordinates_input)
            if not are_one_to_three(numbers_input):
                print("Coordinates should be from 1 to 3!")
            else:
                index = to_cell_index(numbers_input)
                if cells[index] == "X" or cells[index] == "O":
                    print("This cell is occupied! Choose another one!")
                else:
                    if x_turn:
                        cells = cells[:index] + "X" + cells[(index + 1):]
                    else:
                        cells = cells[:index] + "O" + cells[(index + 1):]
                    break
    return cells


def change_turn(turn):
    return not turn


def judge(cells):
    print_cells(cells)
    if is_impossible(cells):
        print("Impossible")
        return True
    elif is_x_win(cells):
        print("X wins")
        return True
    elif is_o_win(cells):
        print("O wins")
        return True
    elif is_draw(cells):
        print("Draw")
        return True
    elif not is_finished(cells):
        return False
    else:
        print("Error")
        return False


cells_input = "_________"
is_x_turn = True

while True:
    if judge(cells_input):
        break
    else:
        cells_input = require_input(cells_input, is_x_turn)
        is_x_turn = change_turn(is_x_turn)
