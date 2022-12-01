# Read input
with open("input.txt", "r") as f:
    input = f.readlines()

my_sum = 0
sums = []

for line in input:
    if line == '\n' or '\n' not in line:
        if line != '\n':
            my_sum += int(line)
        sums.append(my_sum)
        my_sum = 0
    else:
        my_sum += int(line)

sums.sort(reverse=True)

print(sum(sums[0:3]))