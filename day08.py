import sys
from collections import defaultdict

infile = sys.argv[1] if len(sys.argv) > 1 else 'day08a.txt'
data = open(infile).read().strip()
linesH = [x for x in data.split('\n')]
linesV = []
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def printresults():
    if (len(linesV) < 10):
        print(linesH, linesV)


for h in range(len(linesH)):
    linesV.append('')

# formation des lignes V
for h in range(len(linesH)):
    for i in range(len(linesH[0])):
        linesV[h] = linesV[h] + linesH[i][h]
        pass

print('0:', 2*len(linesH)+2*len(linesV)-4)
result = 0
printresults()

for cc in range(0, len(linesH)-1):
    max = -1
    for h in range(0, len(linesH[0])-1):
        if (linesH[cc][h] in numbers and int(linesH[cc][h]) > max):
            result += 1
            max = int(linesH[cc][h])
            linesH[cc] = linesH[cc][:h] + '>' + linesH[cc][h+1:]
            linesV[h] = linesV[h][:cc] + '>' + linesV[h][cc+1:]
    max = -1
    for h in range(len(linesH[0])-1, 0, -1):
        if (linesH[cc][h] in numbers and int(linesH[cc][h]) > max):
            result += 1
            max = int(linesH[cc][h])
            linesH[cc] = linesH[cc][:h] + '<' + linesH[cc][h+1:]
            linesV[h] = linesV[h][:cc] + '<' + linesV[h][cc+1:]

printresults()

for cc in range(0, len(linesV)-1):
    max = -1
    for v in range(0, len(linesV[0])-1):
        if (linesV[cc][v] in numbers and int(linesV[cc][v]) > max):
            result += 1
            max = int(linesV[cc][v])
            linesV[cc] = linesV[cc][:v] + 'v' + linesV[cc][v+1:]
            linesV[v] = linesV[v][:cc] + 'v' + linesV[v][cc+1:]
    max = -1
    for v in range(len(linesV[0])-1, 0, -1):
        if (linesV[cc][v] in numbers and int(linesV[cc][v]) > max):
            result += 1
            max = int(linesV[cc][v])
            linesV[cc] = linesV[cc][:v] + '^' + linesV[cc][v+1:]
            linesV[v] = linesV[v][:cc] + '^' + linesV[v][cc+1:]
printresults()
print('1:', result)
