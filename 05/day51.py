def read_input():
    with open("input.txt", "r") as f:
        return f.readlines()


def parse_input(input):
    parsed_input = [line.replace('\n', '') for line in input]

    return parsed_input


def get_stacks(input):
    stacks = [[] for _ in range(9)]

    for i in reversed(range(9)):
        for j in range(len(input[i])):
            if input[i][j].isupper():
                stacks[j//4].append(input[i][j])

    return stacks


def main():
    input = parse_input(read_input())
    stacks = get_stacks(input)

    for stack in stacks:
        print(stack)
    


if __name__ == '__main__':
    main()
