import re


def read_input():
    with open("input.txt", "r") as f:
        return f.readlines()


def parse_input(input):
    parsed_input = [line.rstrip('\n') for line in input]

    return parsed_input


def get_total_disk_space(input):
    total_disk_space = 0
    folder_sizes = []

    for line in input:
        if '$ ls' in line or 'dir' in line:
            continue
        elif '$ cd ..' in line:
            if folder_sizes[-1] <= 100000:
                total_disk_space += folder_sizes[-1]
            folder_sizes[-2] += folder_sizes[-1]
            folder_sizes.pop()
        elif '$ cd ' in line:
            folder_sizes.append(0)
        else:
            folder_sizes[-1] += int(line.split(' ')[0])

    return total_disk_space


def main():
    input = parse_input(read_input())
    print(get_total_disk_space(input))


if __name__ == '__main__':
    main()
