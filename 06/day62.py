MARKER_LENGTH = 14


def read_input():
    with open("input.txt", "r") as f:
        return f.readlines()


def parse_input(input):
    parsed_input = [line.rstrip('\n') for line in input]

    return parsed_input[0]


def find_number_of_chars(input):
    for i in range(len(input)):
        l = input[i:i+MARKER_LENGTH]

        if len(set(l)) == MARKER_LENGTH:
            return i+MARKER_LENGTH

    return None


def main():
    input = parse_input(read_input())

    print(find_number_of_chars(input))


if __name__ == '__main__':
    main()
