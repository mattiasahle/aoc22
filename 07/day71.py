import re


def read_input():
    with open("input.txt", "r") as f:
        return f.readlines()


def parse_input(input):
    parsed_input = [line.rstrip('\n') for line in input]

    return parsed_input


def get_total_disk_space(input):
    total_disk_space = 0
    folder_spaces = []

    for line in input:
        if '$ ls' in line:
            print('ls', end='\t')
            print(f'{folder_spaces}\t{total_disk_space}')
            continue
        elif '$ cd ..' in line:
            print('cd ..', end='\t')
            if folder_spaces[-1] <= 100000:
                total_disk_space += folder_spaces[-1]
            folder_spaces[-2] += folder_spaces[-1]
            folder_spaces.pop()
        elif '$ cd ' in line:
            print('cd', end='\t')
            folder_spaces.append(0)
        else:
            split_line = line.split(' ')
            print(split_line[0], end='\t')
            if split_line[0].isdigit():
                folder_spaces[-1] += int(split_line[0])

        print(f'{folder_spaces}\t{total_disk_space}')

    return total_disk_space


def main():
    input = parse_input(read_input())
    print(f'\n{get_total_disk_space(input)}')


if __name__ == '__main__':
    main()


# Wrong:
# 3092451
# 1574626
# 1200089
# 1278330
