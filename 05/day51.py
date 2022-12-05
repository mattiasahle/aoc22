import re


def read_input():
    with open("input.txt", "r") as f:
        return f.readlines()


def parse_input(input):
    parsed_input = [line.rstrip('\n') for line in input]

    return parsed_input


def get_stacks(input):
    stacks = [[] for _ in range(9)]

    for i in reversed(range(9)):
        for j in range(len(input[i])):
            if input[i][j].isupper():
                stacks[j//4].append(input[i][j])

    return stacks


def get_moves(input):
    moves = []

    for i in range(10, len(input)):
        moves.append(re.findall('\d+', input[i]))

    return moves


def make_move(move, stacks):
    number_of_pops = int(move[0])
    move_from = int(move[1])
    move_to = int(move[2])

    for _ in range(number_of_pops):
        popped = stacks[move_from - 1].pop()
        stacks[move_to - 1].append(popped)

    return stacks


def get_top_crates(stacks):
    top_crates = ''
    
    for stack in stacks:
        top_crates += stack[-1]

    return top_crates
    

def main():
    input = parse_input(read_input())
    stacks = get_stacks(input)
    moves = get_moves(input)

    for move in moves:
        stacks = make_move(move, stacks)

    print(get_top_crates(stacks))


if __name__ == '__main__':
    main()
