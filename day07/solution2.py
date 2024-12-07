import os
import re

currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))

filename = os.path.join(currentPath, "input.txt")

with open(filename, "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

total = 0

def ternarise(decimal):
    if decimal == 0:
        return '0'
    ternary = ''
    while decimal > 0:
        remainder = decimal % 3
        ternary = str(remainder) + ternary
        decimal //= 3
    return ternary

a = 0
for line in lines:
    a += 1
    print(f'{a} of {len(lines)}... ', end='')
    result, components = line.split(': ')
    result = int(result)
    components = [int(i) for i in components.split(' ')]
    pass

    for i in range(3 ** (len(components) - 1)):
        b = ternarise(i)
        b = '0' * (len(components) - len(b) - 1) + b
        ops = [('+', '*', '?')[int(j)] for j in b]
        ops.append(None)
        combination = [item for pair in list(zip(components, ops + [None])) for item in pair if item is not None]

        evalString = ''
        for item in combination:
            evalString += item if isinstance(item, str) else str(item)

        while len(re.findall(r'[\+\*\?]', evalString)) > 0:
            firstEval = re.search(r'[0-9]*[\+\*\?][0-9]*', evalString).group()
            sep = re.search(r'[+*?]', firstEval).group()
            num1, num2 = firstEval.split(sep)

            match sep:
                case '+':
                    toInsert = str(int(num1) + int(num2))
                case '*':
                    toInsert = str(int(num1) * int(num2))
                case '?':
                    toInsert = num1 + num2

            evalString = evalString.replace(firstEval, toInsert, 1)
            pass

        final = int(evalString)
        if final == result:
            print('MATCH')
            total += final
            break

        pass

    if final != result: print('No match')

    pass

print(total)