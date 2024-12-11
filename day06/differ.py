import os
currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))
# foo = open(os.path.join(currentPath, "old.txt"), 'r')
with open(os.path.join(currentPath, "new-u.txt"), 'r') as fnu: new_u = fnu.readlines()
with open(os.path.join(currentPath, "new-o.txt"), 'r') as fno: new_o = fno.readlines()

# old_o = foo.readline()



for y in range(len(new_u)):
    for x in range(len(new_u[y])):
        match new_o[y][x]:
            case '.':
                c = '.' if new_u[y][x] == '0' else '#'
            case '0':
                c = '+' if new_u[y][x] == '0' else 'X'
            case '1':
                c = 'X' if new_u[y][x] == '0' else '*'
        print(c, end='')
    print()