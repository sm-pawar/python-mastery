input_file = './Data/portfolio.dat'

cost = 0

with open(input_file, 'r') as f:
    lines = f.readlines()
    for line in lines:
        items = line.split()
        cost += int(items[1]) * float(items[2])


print(f'Total cost: {cost}')