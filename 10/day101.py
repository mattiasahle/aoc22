CYCLES_OF_INTEREST = [20, 60, 100, 140, 180, 220]


def main():
    input = parse_input(read_input())
    sum_signal_strengths = 0
    x_register = 1
    q = get_q(input)

    for i, value in enumerate(q, start=1):
        if i in CYCLES_OF_INTEREST:
            sum_signal_strengths += i * x_register
        x_register += value

    print(sum_signal_strengths)


def get_q(input):
    q = []

    for line in input:
        q.append(0)
        if 'addx' in line:
            q.append(int(line.split(' ')[1]))

    return q


def read_input():
    with open("input.txt", "r") as f:
        return f.readlines()


def parse_input(input):
    parsed_input = [line.rstrip('\n') for line in input]

    return parsed_input


if __name__ == '__main__':
    main()
