def main():
    input = parse_input(read_input())
    crt = [['.' for _ in range(40)] for _ in range(6)]
    x_reg = 1
    q = get_q(input)

    for i, value in enumerate(q):
        row = i // 40
        col = i % 40

        if x_reg == col or x_reg == col - 1 or x_reg == col + 1:
            crt[row][col] = '#'

        x_reg += value

    print_crt(crt)


def get_q(input):
    q = []

    for line in input:
        q.append(0)
        if 'addx' in line:
            q.append(int(line.split(' ')[1]))

    return q


def print_crt(crt):
    for row in crt:
        for pixel in row:
            print(pixel, end = '')
        print()


def read_input():
    with open("input.txt", "r") as f:
        return f.readlines()


def parse_input(input):
    parsed_input = [line.rstrip('\n') for line in input]

    return parsed_input


if __name__ == '__main__':
    main()
