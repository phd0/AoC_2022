import sys
from collections import defaultdict
infile = sys.argv[1] if len(sys.argv) > 1 else 'day09a.txt'
data = open(infile).read().strip()
lines = [x for x in data.split('\n')]
memory = []
posH = [0, 0]
posT = [0, 0]

moves = [line.split(' ') for line in lines]


def T(dir, n):
    # move the Tail
    global posH, posT, memory
    if (posH[0]-posT[0] > 1):
        posT[0] = posH[0]-1
        posT[1] = posH[1]
    elif (posH[0]-posT[0] < -1):
        posT[0] = posH[0]+1
        posT[1] = posH[1]
    if (posH[1]-posT[1] > 1):
        posT[0] = posH[0]
        posT[1] = posH[1]-1
    elif (posH[1]-posT[1] < -1):
        posT[0] = posH[0]
        posT[1] = posH[1]+1
    if (posT not in memory):
            memory.append(posT)

def move(dir, n):
    global posH, posT, memory
    if (dir == 'R'):
        moveH = [n, 0]
    elif (dir == 'L'):
        moveH = [-n, 0]
    elif (dir == 'U'):
        moveH = [0, n]
    elif (dir == 'D'):
        moveH = [0, -n]
    else:
        moveH = [0, 0]

    posH[0] += moveH[0]
    posH[1] += moveH[1]
    print(abs(posH[0]-posT[0]), abs(posH[1]-posT[1]), end=' ')
    if (abs(posH[0]-posT[0]) > 1 or abs(posH[1]-posT[1]) > 1):
        for nn in range(1, n):
            T(dir, 1)
    else:
        # the Tail don't move
        pass
    # show line like : 
    # RxRy    moveH    Head  Tail 
    # 1 0 R2,[2, 0]   [2, 2][1, 2]
    print(dir, n, ',', moveH, '\t', posH, posT, sep='')
    pass

memory.append(posT)
print('RxRy    moveH    Head  Tail')
for dir, step in moves:
    move(dir, int(step))

print('1:', len(memory))
