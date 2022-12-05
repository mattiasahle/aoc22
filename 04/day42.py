def read_input():
    with open("input.txt", "r") as f:
        return f.readlines()


def parse_input(input: list):
    input = [line.replace('\n', '') for line in input]
    input = [line.split(',') for line in input]

    return input


def is_in_range(number: int, range_low: int, range_high: int):
    return range_low <= number <= range_high


def get_first_low(assigment: list):
    return int(assigment[0].split('-')[0])


def get_first_high(assigment: list):
    return int(assigment[0].split('-')[1])


def get_second_low(assigment: list):
    return int(assigment[1].split('-')[0])


def get_second_high(assigment: list):
    return int(assigment[1].split('-')[1])


def is_in_full_range(a):
    if (is_in_range(get_first_low(a), get_second_low(a), get_second_high(a)) or 
        is_in_range(get_first_high(a), get_second_low(a), get_second_high(a))):
        return True
    elif (is_in_range(get_second_low(a), get_first_low(a), get_first_high(a)) or 
        is_in_range(get_second_high(a), get_first_low(a), get_first_high(a))):
        return True
    else:
        return False


def main():
    number_of_assignments = 0
    assignments = parse_input(read_input())
    
    for assignment in assignments:
        if(is_in_full_range(assignment)):
            number_of_assignments += 1

    print(number_of_assignments)


if __name__ == '__main__':
    main()
