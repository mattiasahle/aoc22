head_pos = [0, 0]
tail_pos = [0, 0]
tail_visited = set()


def read_input():
    with open("input.txt", "r") as f:
        return f.readlines()


def parse_input(input):
    parsed_input = [line.rstrip('\n') for line in input]

    return parsed_input


def get_diffs():
    x_diff = head_pos[0] - tail_pos[0]
    y_diff = head_pos[1] - tail_pos[1]

    return x_diff, y_diff


def is_head_touching(x_diff, y_diff):
    if -1 <= x_diff <= 1 and -1 <= y_diff <= 1:
        return True
    else:
        return False


def convert_int_list_to_string(int_list):
    s = str(int_list[0])
    s += ','
    s += str(int_list[1])

    return s


def save_tail_pos():
    tail_visited.add(convert_int_list_to_string(tail_pos))


def move_one_step(move):
    if move == 'R':
        head_pos[0] += 1
        x_diff, y_diff = get_diffs()
        if not is_head_touching(x_diff, y_diff):
            tail_pos[0] += 1
            tail_pos[1] = head_pos[1]

    elif move == 'L':
        head_pos[0] -= 1
        x_diff, y_diff = get_diffs()
        if not is_head_touching(x_diff, y_diff):
            tail_pos[0] -= 1
            tail_pos[1] = head_pos[1]

    elif move == 'U':
        head_pos[1] += 1
        x_diff, y_diff = get_diffs()
        if not is_head_touching(x_diff, y_diff):
            tail_pos[1] += 1
            tail_pos[0] = head_pos[0]

    elif move == 'D':
        head_pos[1] -= 1
        x_diff, y_diff = get_diffs()
        if not is_head_touching(x_diff, y_diff):
            tail_pos[1] -= 1
            tail_pos[0] = head_pos[0]

    save_tail_pos()


def move(line):
    move = line.split(' ')[0]
    steps = int(line.split(' ')[1])

    for _ in range(steps):
        move_one_step(move)


def main():
    input = parse_input(read_input())

    for line in input:
        move(line)

    print(len(tail_visited))


if __name__ == '__main__':
    main()
