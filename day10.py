import sys
from collections import defaultdict
infile = sys.argv[1] if len(sys.argv) > 1 else 'day10.txt'
data = open(infile).read().strip()
lines = [x for x in data.split('\n')]
resultat = 0
value = 0
lastValue = 0
indexCycle = 0
total = 1
cycle = 0
cycles = [20, 60, 100, 140, 180, 220, 9999]
op = ''

for line in lines:
    try:
        op, value = line.split(' ')
        cycle += 2
    except:
        cycle += 1
        value = 0
    value = int(value)
    if (op != 'noop'):
        lastValue = value
    if cycle >= cycles[indexCycle]:
        resultat += total * cycles[indexCycle]
        #print(indexCycle, cycles[indexCycle], ',', cycle)
        indexCycle += 1
        pass
    total += value

print('1:', resultat)
