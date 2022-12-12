import re


class Monkey:
    def __init__(self,
        starting_items: list[int],
        operation: list[str],
        test: int,
        if_test_true: int,
        if_test_false: int) -> None:
        self.starting_items = starting_items # List[int...]
        self.operation = operation # ['*' or '+', 'old' or '5']
        self.test = test # int
        self.if_test_true = if_test_true # int
        self.if_test_false = if_test_false # int
        self.new_item = 0 # int
        self.inspected_items = 0 # int

    def __get_operand(self, operand: str) -> int:
        if operand.isdigit():
            return int(operand)
        elif operand == 'old':
            return self.starting_items[0]

    def do_operation(self) -> None:
        operand = self.__get_operand(self.operation[1])
        old_item = self.starting_items.pop(0)
        operator = self.operation[0]

        if operator == '*':
            self.new_item = old_item * operand
        elif operator == '+':
            self.new_item = old_item + operand

        self.new_item //= 3

    def get_monkey_to_throw_to(self) -> int:
        if self.new_item % self.test == 0:
            return self.if_test_true
        else:
            return self.if_test_false

    def __str__(self) -> str:
        return f'Monkey:\n\
            {self.starting_items=}\n\
            {self.operation=}\n\
            {self.test=}\n\
            {self.if_test_true=}\n\
            {self.if_test_false=}\n\
            {self.new_item=}\n\
            {self.inspected_items=}'


def main():
    monkeys = parse_input(read_input())

    for _ in range(20):
        for monkey in monkeys:
            while len(monkey.starting_items) > 0:
                monkey.inspected_items += 1
                monkey.do_operation()
                monkey_to_throw_to = monkey.get_monkey_to_throw_to()
                monkeys[monkey_to_throw_to].starting_items.append(monkey.new_item)

    for i, monkey in enumerate(monkeys):
        print(f'{i}: {monkey}')

    # monkeys.sort(key=lambda , reverse=True)
    print(232 * 276)


def parse_input(input):
    parsed_input = [line.rstrip('\n') for line in input]
    monkeys = get_monkeys(parsed_input, 8)
    
    return monkeys


def get_monkeys(input, n):
    monkeys = []

    for i in range(n):
        monkeys.append(get_monkey(input, i))

    return monkeys


def get_monkey(input, i):
    for j, line in enumerate(input):
        if f'Monkey {i}:' in line:
            return Monkey(
                starting_items = [int(item) for item in re.findall('\d+', input[j + 1])],
                operation = input[j + 2].split(' ')[-2:],
                test = int(re.findall('\d+', input[j + 3])[0]),
                if_test_true = int(re.findall('\d+', input[j + 4])[0]),
                if_test_false = int(re.findall('\d+', input[j + 5])[0])
            )


def read_input():
    with open("input.txt", "r") as f:
        return f.readlines()


if __name__ == '__main__':
    main()
