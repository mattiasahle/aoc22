def read_input():
    with open("input.txt", "r") as f:
        return f.readlines()


def parse_input(input):
    parsed_input = [line.rstrip('\n') for line in input]

    return parsed_input[0]


def find_number_of_chars(input):
    l = []

    for i in range(len(input)):
        l.append(input[i])

        if len(set(l)) == 14:
            return i+1

        if len(l) == 14:
            l = l[1:]

    return None


def main():
    input = parse_input(read_input())

    print(find_number_of_chars(input))


if __name__ == '__main__':
    main()
