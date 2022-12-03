def read_input():
    with open("input.txt", "r") as f:
        return f.readlines()


def parse_input(input):
    parsed_input = [line.replace('\n', '') for line in input]

    return parsed_input


def print_input(input):
    for line in range(len(input)):
        print(input[line])


def calculate_priority(char):
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 38


def split_content(content):
    compartment1 = content[0:len(content)//2]
    compartment2 = content[len(content)//2:len(content)]

    return compartment1, compartment2


def get_common_item(compartment1, compartment2):
    for item in compartment1:
        if item in compartment2:
            return item


def get_priority(content):
    compartment1, compartment2 = split_content(content)
    common_item = get_common_item(compartment1, compartment2)

    return calculate_priority(common_item)


def main():
    sum_of_priorities = 0
    contents = parse_input(read_input())

    for content in contents:
        sum_of_priorities += get_priority(content)

    print(sum_of_priorities)


if __name__ == '__main__':
    main()
