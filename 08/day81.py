import numpy as np


def read_input():
    with open("input.txt", "r") as f:
        return f.readlines()


def parse_input(input):
    parsed_input = [line.rstrip('\n') for line in input]
    parsed_input = np.array([[char for char in line]
                            for line in parsed_input], np.int8)

    return parsed_input


def is_visible_north(input, row, column):
    tree_height = input[row][column]

    while row >= 1:
        row -= 1
        if input[row][column] >= tree_height:
            return False

    return True


def is_visible_south(input, row, column):
    tree_height = input[row][column]

    while row <= 97:
        row += 1
        if input[row][column] >= tree_height:
            return False

    return True


def is_visible_west(input, row, column):
    tree_height = input[row][column]

    while column >= 1:
        column -= 1
        if input[row][column] >= tree_height:
            return False

    return True


def is_visible_east(input, row, column):
    tree_height = input[row][column]

    while column <= 97:
        column += 1
        if input[row][column] >= tree_height:
            return False

    return True


def get_num_visible_trees(input):
    visible_trees = input.shape[0] * 4 - 4  # Add outer trees

    for row in range(1, len(input[:-1])):
        for column in range(1, len(input[row][:-1])):
            if is_visible_north(input, row, column):
                visible_trees += 1
            elif is_visible_south(input, row, column):
                visible_trees += 1
            elif is_visible_west(input, row, column):
                visible_trees += 1
            elif is_visible_east(input, row, column):
                visible_trees += 1

    return visible_trees


def main():
    input = parse_input(read_input())
    print(get_num_visible_trees(input))


if __name__ == '__main__':
    main()
