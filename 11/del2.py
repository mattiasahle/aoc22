import re

s = '  Test: divisible by 11'

starting_items = int(re.findall('\d+', s)[0])
print(starting_items)