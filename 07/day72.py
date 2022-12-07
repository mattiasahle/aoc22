TOTAL_SPACE = 70000000
REQUIRED_FREE_SPACE = 30000000


def read_input():
    with open("input.txt", "r") as f:
        return f.readlines()


def parse_input(input):
    parsed_input = [line.rstrip('\n') for line in input]

    return parsed_input


def get_used_space(input):
    used_space = 0

    for line in input:
        s = line.split(' ')[0]

        if s.isdigit():
            used_space += int(s)

    return used_space


def calculate_missing_free_space(input):
    used_space = get_used_space(input)
    free_space = TOTAL_SPACE - used_space
    
    return REQUIRED_FREE_SPACE - free_space


def find_candidate(candidates, missing_free_space):
    candidates.sort()

    for candidate in candidates:
        if candidate >= missing_free_space:
            return candidate
        else:
            return None


def find_remove_folder(input, missing_free_space):
    folder_sizes = []
    candidates = []

    for line in input:
        if '$ ls' in line or 'dir ' in line:
            continue
        elif '$ cd ..' in line:
            if folder_sizes[-1] >= missing_free_space:
                candidates.append(folder_sizes[-1])
            folder_sizes[-2] += folder_sizes[-1]
            folder_sizes.pop()
        elif '$ cd ' in line:
            folder_sizes.append(0)
        else:
            folder_sizes[-1] += int(line.split(' ')[0])

    return find_candidate(candidates, missing_free_space)    


def main():
    input = parse_input(read_input())
    missing_free_space = calculate_missing_free_space(input)
    
    print(find_remove_folder(input, missing_free_space))


if __name__ == '__main__':
    main()
