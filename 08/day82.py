import numpy as np


def read_input():
    with open("input.txt", "r") as f:
        return f.readlines()


def parse_input(input):
    parsed_input = [line.rstrip('\n') for line in input]
    parsed_input = np.array([[char for char in line]
                            for line in parsed_input], np.int8)

    return parsed_input


def get_viewing_distance_north(input, row, column):
    viewing_distance = 0
    tree_height = input[row][column]

    while row > 0:
        row -= 1
        if input[row][column] >= tree_height:
            viewing_distance += 1
            break
        else:
            viewing_distance += 1

    return viewing_distance


def get_viewing_distance_south(input, row, column):
    viewing_distance = 0
    tree_height = input[row][column]

    while row < input.shape[1] - 1:
        row += 1
        if input[row][column] >= tree_height:
            viewing_distance += 1
            break
        else:
            viewing_distance += 1

    return viewing_distance


def get_viewing_distance_west(input, row, column):
    viewing_distance = 0
    tree_height = input[row][column]

    while column > 0:
        column -= 1
        if input[row][column] >= tree_height:
            viewing_distance += 1
            break
        else:
            viewing_distance += 1

    return viewing_distance


def get_viewing_distance_east(input, row, column):
    viewing_distance = 0
    tree_height = input[row][column]

    while column < input.shape[0] - 1:
        column += 1
        if input[row][column] >= tree_height:
            viewing_distance += 1
            break
        else:
            viewing_distance += 1

    return viewing_distance


def get_highest_scenic_score(input):
    highest_scenic_score = 0

    for row in range(0, len(input)):
        for column in range(0, len(input[row])):
            viewing_distances = []

            viewing_distances.append(
                get_viewing_distance_north(input, row, column))
            viewing_distances.append(
                get_viewing_distance_south(input, row, column))
            viewing_distances.append(
                get_viewing_distance_west(input, row, column))
            viewing_distances.append(
                get_viewing_distance_east(input, row, column))

            highest_scenic_score = max(
                highest_scenic_score, np.prod(viewing_distances))

    return highest_scenic_score


def main():
    input = parse_input(read_input())
    print(get_highest_scenic_score(input))


if __name__ == '__main__':
    main()
