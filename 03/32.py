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


def get_common_item(grouped_content):
    s1 = grouped_content[0]
    s2 = grouped_content[1]
    s3 = grouped_content[2]
    common_item = ''.join(set(s1).intersection(s2).intersection(s3))

    return common_item


def get_priority(grouped_content):
    common_item = get_common_item(grouped_content)

    return calculate_priority(common_item)


def group_contents(contents):
    grouped_contents = []
    temp_list = []
    grouped_contents_i = 0

    for content_i in range(len(contents)):
        temp_list.append(contents[content_i])

        if (content_i + 1) % 3 == 0:
            grouped_contents.append(temp_list.copy())
            grouped_contents_i += 1
            temp_list.clear()

    return grouped_contents


def main():
    sum_of_priorities = 0
    contents = parse_input(read_input())
    grouped_contents = group_contents(contents)

    for grouped_content in grouped_contents:
        sum_of_priorities += get_priority(grouped_content)

    print(sum_of_priorities)


if __name__ == '__main__':
    main()
