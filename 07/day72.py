import re


def read_input():
    with open("input.txt", "r") as f:
        return f.readlines()


def parse_input(input):
    parsed_input = [line.rstrip('\n') for line in input]

    return parsed_input


def get_used_disk_space(input):
    used_disk_space = 0
    folders = []

    for line in input:
        if '$ ls' in line or 'dir ' in line:
            continue
        elif '$ cd ..' in line:
            folders[-2] += folders[-1]
            folders.pop()
        elif '$ cd ' in line:
            folders.append(0)
        else:
            used_disk_space += int(line.split(' ')[0])

    return used_disk_space


def get_remove_folder(input, need_to_free):
    folders_less_than = []
    candidate_folders = []

    for line in input:
        if '$ ls' in line:
            continue
        elif '$ cd ..' in line:
            if folders_less_than[-1] <= need_to_free:
                candidate_folders.append(folders_less_than[-1])
            folders_less_than[-2] += folders_less_than[-1]
            folders_less_than.pop()
        elif '$ cd ' in line:
            folders_less_than.append(0)
        else:
            split_line = line.split(' ')
            if split_line[0].isdigit():
                folders_less_than[-1] += int(split_line[0])

    candidate_folders.sort(reverse=True)

    for candidate in candidate_folders:
        if candidate <= need_to_free:
            return candidate
        else:
            return None


def main():
    input = parse_input(read_input())
    used_disk_space = get_used_disk_space(input)
    print(f'\n{used_disk_space=}')
    free_disk_space = 70000000 - used_disk_space
    print(f'{free_disk_space=}')
    need_to_free = 30000000 - free_disk_space
    print(f'{need_to_free=}')

    print(get_remove_folder(input, need_to_free))


if __name__ == '__main__':
    main()


# Wrong:
# 4394509
