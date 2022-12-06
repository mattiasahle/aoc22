import re
s = 'adfsoijnf7fdsaljh323hfjdk983fhdkj8fewr32'
print([int(n) for n in re.findall('\d+', s)])