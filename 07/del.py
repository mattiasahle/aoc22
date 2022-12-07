line = 'dir sfqq'
line = '203559 nnch'
split_line = line.split(' ')[0]
print(split_line)

if split_line.isdigit():
    print(int(split_line))