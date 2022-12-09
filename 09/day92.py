knots = [[0, 0] for _ in range(10)]
tail_visited = set()


def read_input():
    with open("del_input.txt", "r") as f:
        return f.readlines()


def parse_input(input):
    parsed_input = [line.rstrip('\n') for line in input]

    return parsed_input


def get_diffs(knot1, knot2):
    x_diff = knot1[0] - knot2[0]
    y_diff = knot1[1] - knot2[1]

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
    tail_visited.add(convert_int_list_to_string(knots[-1]))
    # tail_visited.add(convert_int_list_to_string(knots[1]))


def move_tail_knot(head, tail, x_diff, y_diff):
    x_move = max(0, abs(x_diff) - 1)
    y_move = max(0, abs(y_diff) - 1)

    if x_diff > 1:
        tail[0] += x_move
        tail[1] = head[1]
    elif x_diff < 1:
        tail[0] -= x_move
        tail[1] = head[1]

    if y_diff > 1:
        tail[1] += y_move
        tail[0] = head[0]
    elif y_diff < 1:
        tail[1] -= y_move
        tail[0] = head[0]


def move_head(move):
    print('MOVE HEAD')
    if move == 'R':
        knots[0][0] += 1
    elif move == 'L':
        knots[0][0] -= 1
    elif move == 'U':
        knots[0][1] += 1
    elif move == 'D':
        knots[0][1] -= 1


def move_tail():
    for i in range(len(knots) - 1):
        # for i in range(1):
        head, tail = knots[i], knots[i + 1]
        # print(f'{i=}, {head=}, {tail=}')
        x_diff, y_diff = get_diffs(head, tail)
        # print(f'{x_diff=}, {y_diff=}')

        if not is_head_touching(x_diff, y_diff):
            move_tail_knot(head, tail, x_diff, y_diff)

        # print(f'{i=}, {knots=}')
        # print()

    # print()
    save_tail_pos()


def move(line):
    move = line.split(' ')[0]
    steps = int(line.split(' ')[1])

    for _ in range(steps):
        move_head(move)
        print(f'{knots=}')
        move_tail()
        print(f'{knots=}')
        print()


def main():
    global grid, head_pos, tail_pos
    input = parse_input(read_input())

    for line in input[:1]:
        move(line)

    print(knots)
    print(len(tail_visited))


if __name__ == '__main__':
    main()

# Too high: 2706
