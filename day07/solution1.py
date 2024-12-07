import os

currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))

filename = os.path.join(currentPath, "input.txt")

with open(filename, "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

total = 0

for line in lines:
    result, components = line.split(': ')
    result = int(result)
    components = [int(i) for i in components.split(' ')]
    pass

    for i in range(2 ** (len(components) - 1)):
        b = str(bin(i))[2:]
        b = '0' * (len(components) - len(b) - 1) + b
        ops = [('+', '*')[int(j)] for j in b]
        ops.append(None)
        combination = [item for pair in list(zip(components, ops + [None])) for item in pair if item is not None]
        evalString = ''
        for item in combination:
            if isinstance(item, str):
                evalString += item
            else:
                evalString += str(item) + ')'
                evalString = f'({evalString}'
        if eval(evalString) == result:
            total += result
            break
        else:
            continue

print(total)