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
    number_of_crates_to_move = int(move[0])
    move_from = int(move[1])-1
    move_to = int(move[2])-1
    temp_stack = stacks[move_from][-number_of_crates_to_move:]
    stacks[move_from] = stacks[move_from][:len(stacks[move_from])-number_of_crates_to_move]

    for crate in temp_stack:
        stacks[move_to].append(crate)

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
