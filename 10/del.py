cycles_of_interest = [20, 60, 100, 140, 180, 220]

for i in range(1000):
    if i + 1 in cycles_of_interest:
        print(i + 1)