import os

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

print(f'Disk read. Fragmenting...')

while '.' in disk:
    try:
        firstEmpty = disk.index('.')
        disk[firstEmpty] = disk.pop()
    except: pass

    if disk.count('.') % 100 == 0:
        print(f'{disk.count('.')} empty blocks remaining...')

print(f'Fragmentation complete. Calculating checksum...')

checksum = 0

for i, v in enumerate(disk):
    checksum += i * v

print(checksum)

pass

# just realised this isn't defrag at all
# it's a fragmentation algorithm lmao