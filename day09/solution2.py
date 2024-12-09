import os
from itertools import groupby
from operator import itemgetter

currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))

filename = os.path.join(currentPath, "input.txt")

with open(filename, "r") as f:
    lines = f.readlines()
    line = [line.strip() for line in lines][0]

disk = []
id = 0

print(f'Reading disk...')
for i in range(0, len(line), 2):
    j = i + 1

    for _ in range(int(line[i])): disk.append(id)
    try:
        for _ in range(int(line[j])): disk.append('.')
    except: pass

    id += 1

print(f'Disk read. Compacting...')

for fileID in range(sorted([_ for _ in disk if _ != '.'])[-1], 0, -1):
    print(f'\nFile {fileID}: ', end='')

    emptyIndices = [i for i, x in enumerate(disk) if x == "."]
    emptySections = []
    for k, g in groupby(enumerate(emptyIndices), lambda ix : ix[0] - ix[1]):
        a = list(map(itemgetter(1), g))
        emptySections.append({'start': a[0], 'length': len(a)})

    print(f'generated empty sections... ', end='')

    thisFile = [i for i, x in enumerate(disk) if x == fileID]
    thisFileIndex = thisFile[0]
    thisFileLength = len(thisFile)

    print(f'found file... ', end='')

    for emptySection in emptySections:
        if thisFileLength <= emptySection['length'] and thisFileIndex > emptySection['start']:
            disk[emptySection['start'] : emptySection['start'] + thisFileLength] = [fileID] * thisFileLength
            disk[thisFileIndex : thisFileIndex + thisFileLength] = '.' * thisFileLength
            print('moved file forward. ', end='')
            break
    else:
        print('couldn\'t move file. ', end='')

    # print()
    # for block in disk:
    #     print(block, end='')
    print()
    # print(f'{disk.count('.')} empty blocks remaining...')

print(f'Fragmentation complete. Calculating checksum...')

checksum = 0

for i, v in enumerate(disk):
    if v != '.':
        checksum += i * v

print()
for block in disk:
    print(block, end='')
print()
print(checksum)

pass

# just realised this isn't defrag at all
# it's a fragmentation algorithm lmao