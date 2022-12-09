# knots = [[2, 2], [0, 1], [0, 0]]
knots = [[-2, -2], [-1, 0], [0, 0]]


def is_head_touching(x_diff, y_diff):
    if -1 <= x_diff <= 1 and -1 <= y_diff <= 1:
        return True
    else:
        return False


def get_diffs(knot1, knot2):
    x_diff = knot1[0] - knot2[0]
    y_diff = knot1[1] - knot2[1]

    return x_diff, y_diff


def move_tail_knot(head, tail, x_diff, y_diff):
    x_move = min(1, abs(x_diff))
    y_move = min(1, abs(y_diff))
    print(f'{x_move=}, {y_move=}')

    if x_diff > 1:
        tail[0] += x_move
        tail[1] += y_move


def move_tail():
    for i in range(len(knots) - 1):
        # for i in range(1):
        head, tail = knots[i], knots[i + 1]
        # print(f'{i=}, {head=}, {tail=}')
        x_diff, y_diff = get_diffs(head, tail)
        # print(f'{x_diff=}, {y_diff=}')

        if not is_head_touching(x_diff, y_diff):
            move_tail_knot(head, tail, x_diff, y_diff)


move_tail()
