import sys
from collections import defaultdict

infile = sys.argv[1] if len(sys.argv) > 1 else 'day08a.txt'
data = open(infile).read().strip()
lines = [x for x in data.split('\n')]

# print('0:', 2*len(lines)+2*len(lines[0])-4) # uniquement les bords
result = 0
memory = []
# partie 1
for y in range(len(lines)-1, 0, -1):
    max = -1
    for x in range(0, len(lines[0])-1):
        if (int(lines[y][x]) > max):
            max = int(lines[y][x])
            if ([y, x] not in memory):
                result += 1
                memory.append([y, x])

for y in range(0, len(lines)-1):
    max = -1
    for x in range(len(lines[0])-1, 0, -1):
        if (int(lines[y][x]) > max):
            max = int(lines[y][x])
            if ([y, x] not in memory):
                result += 1
                memory.append([y, x])

for x in range(0, len(lines[0])-1):
    max = -1
    for y in range(0, len(lines)-1):
        if (int(lines[y][x]) > max):
            max = int(lines[y][x])
            if ([y, x] not in memory):
                result += 1
                memory.append([y, x])

for x in range(len(lines[0])-1, 0, -1):
    max = -1
    for y in range(len(lines)-1, 0, -1):
        if (int(lines[y][x]) > max):
            max = int(lines[y][x])
            if ([y, x] not in memory):
                result += 1
                memory.append([y, x])

print('1:', result)
# partie 2
result = 0
memory = []
for y in range(len(lines)-1, 0, -1):
    for x in range(0, len(lines[0])):
        max = 1
        cc = 1
        for yy in range(len(lines[y])-1, y, -1):
            if lines[yy][x] < lines[y][x]:
                cc = 1
                break
            else:
                cc += 1
                #print(cc, '/', x, ',', yy, '< ', lines[yy][x], sep='')
        max *= cc
        for yy in range(y-1, -1, -1):
            if lines[yy][x] < lines[y][x]:
                cc = 1
                break
            else:
                cc += 1
                #print(cc, '/', x, ',', yy, '> ', lines[yy][x], sep='')
        max *= cc
        for xx in range(len(lines[x])-1, x, -1):
            if lines[y][xx] < lines[y][x]:
                cc = 1
                break
            else:
                cc += 1
                #print(cc, '/', xx, ',', y, '< ', lines[y][xx], sep='')
        max *= cc
        for xx in range(x-1, -1, -1):
            if lines[y][xx] < lines[y][x]:
                cc = 1
                break
            else:
                cc += 1
                #print(cc, '/', xx, ',', y, '> ', lines[y][xx], sep='')
        max *= cc
    if (max > result):
        result = max

print('2:', result)
