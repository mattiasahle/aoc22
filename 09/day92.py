knot_positions = [[0, 0] for _ in range(10)]
tail_visited = set()


def main():
    input = parse_input(read_input())

    for line in input:
        move(line)

    print(len(tail_visited))


def read_input():
    with open("input.txt", "r") as f:
        return f.readlines()


def parse_input(input):
    parsed_input = [line.rstrip('\n') for line in input]

    return parsed_input


def move(line):
    move = line.split(' ')[0]
    steps = int(line.split(' ')[1])

    for _ in range(steps):
        move_head(move)
        move_tail()


def move_head(move):
    if move == 'R':
        knot_positions[0][0] += 1
    elif move == 'L':
        knot_positions[0][0] -= 1
    elif move == 'U':
        knot_positions[0][1] += 1
    elif move == 'D':
        knot_positions[0][1] -= 1


def move_tail():
    for i in range(len(knot_positions) - 1):
        head, tail = knot_positions[i], knot_positions[i + 1]
        x_diff, y_diff = get_diffs(head, tail)

        if not is_touching_head(x_diff, y_diff):
            move_tail_knot(tail, x_diff, y_diff)

    save_tail_pos()


def get_diffs(knot1, knot2):
    x_diff = knot1[0] - knot2[0]
    y_diff = knot1[1] - knot2[1]

    return x_diff, y_diff


def is_touching_head(x_diff, y_diff):
    if -1 <= x_diff <= 1 and -1 <= y_diff <= 1:
        return True
    else:
        return False


def move_tail_knot(tail, x_diff, y_diff):
    x_move = min(1, abs(x_diff))
    y_move = min(1, abs(y_diff))

    if x_move:
        if x_diff > 0:
            tail[0] += x_move
        else:
            tail[0] -= x_move

    if y_move:
        if y_diff > 0:
            tail[1] += y_move
        else:
            tail[1] -= y_move


def save_tail_pos():
    tail_visited.add(convert_int_coordinates_to_string(knot_positions[-1]))


def convert_int_coordinates_to_string(int_list):
    s = str(int_list[0])
    s += ','
    s += str(int_list[1])

    return s


if __name__ == '__main__':
    main()
