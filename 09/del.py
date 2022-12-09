knots = [[2, 0], [1, 0], [0, 0]]


def move_tail():
    for i in range(len(knots) - 1):
        # for i in range(1):
        print(f'{i=}')
        head, tail = knots[i], knots[i + 1]
        print(f'{head=}, {tail=}')

        print()


move_tail()
