def read_input():
    with open("input.txt", "r") as f:
        return f.readlines()


def parse_input(input):
    parsed_input = [line.rstrip('\n') for line in input]

    return parsed_input


def main():
    input = parse_input(read_input())


if __name__ == '__main__':
    main()
