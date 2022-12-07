def read_input():
    with open("input.txt", "r") as f:
        return f.readlines()


def parse_input(input):
    parsed_input = [line.rstrip('\n') for line in input]

    return parsed_input


def get_used_disk_space(input):
    used_disk_space = 0

    for line in input:
        split_line = line.split(' ')

        if split_line[0].isdigit():
            used_disk_space += int(split_line[0])

    return used_disk_space


def get_remove_folder(input, need_to_free):
    folder_sizes = []
    candidate_folders = []

    for line in input:
        if '$ ls' in line or 'dir ' in line:
            continue
        elif '$ cd ..' in line:
            if folder_sizes[-1] >= need_to_free:
                candidate_folders.append(folder_sizes[-1])
            folder_sizes[-2] += folder_sizes[-1]
            folder_sizes.pop()
        elif '$ cd ' in line:
            folder_sizes.append(0)
        else:
            folder_sizes[-1] += int(line.split(' ')[0])

    candidate_folders.sort()

    for candidate in candidate_folders:
        if candidate >= need_to_free:
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
    remove = get_remove_folder(input, need_to_free)
    print(f'{remove=}')


if __name__ == '__main__':
    main()
