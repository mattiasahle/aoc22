# Read input
with open("input.txt", "r") as f:
    input = f.readlines()

sum = 0
max_sum = 0

for line in input:
    if line == '\n' or '\n' not in line:
        if sum > max_sum:
            max_sum = sum
        sum = 0
        continue
    else:
        sum += int(line)

print(max_sum)