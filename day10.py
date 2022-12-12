import sys
from collections import defaultdict
infile = sys.argv[1] if len(sys.argv) > 1 else 'day10.txt'
data = open(infile).read().strip()
lines = [x for x in data.split('\n')]
resultat = 0
value = 0
indexCycle = 0
total = 0
cycle = 0
steps = [20, 60, 100, 140, 180, 220, 9999]
op = ''
CRT = ''
spritePosition = '###.......................'
resultatTest = '##..##..##..##..##..##..##..##..##..##..###...###...###...###...###...###...###.####....####....####....####....####....#####.....#####.....#####.....#####.....######......######......######......###########.......#######.......#######.....'
# for i in range(240):   CRT += '.'


def printSpritePosition(c):
    global spritePosition, cycle, total, line, infile
    #print(spritePosition, ' total=', total, '\tcycle=', cycle,  '  \t', line, ' ', sep='')
    print(spritePosition[0:(cycle % 40)] + (c if (spritePosition[cycle % 40] == '#') else '!') +
          spritePosition[(cycle % 40)+1:40], ' total=', total, '\tcycle=', cycle,  '  \t', line, ' ', sep='')


print('0123456789012345678901234567890123456789')
for line in lines:
    spritePosition = ''
    for i in range(40):
        spritePosition += '.'
    try:
        op, value = line.split(' ')
        value = int(value)

        if cycle >= steps[indexCycle]:
            resultat += total * steps[indexCycle]
            # print(indexCycle, steps[indexCycle], ',', cycle)
            indexCycle += 1
        # calcul de spritePosition

        spritePosition = spritePosition[0:total if total > 0 else 0] + \
            '###' + spritePosition[1+(total if total >= 0 else 0):len(spritePosition)]
        CRT = CRT+spritePosition[cycle % 40]
        printSpritePosition('1')
        cycle += 1
        CRT = CRT+spritePosition[cycle % 40]
        printSpritePosition('2')
        cycle += 1
    except:
        spritePosition = spritePosition[0:total if total > 0 else 0] + \
            '###' + spritePosition[1+(total if total >= 0 else 0):len(spritePosition)]
        CRT = CRT+spritePosition[cycle % 40]
        printSpritePosition('x')
        cycle += 1
        value = 0
    total += value
    if (CRT != resultatTest[:len(CRT)] and infile == 'day10a.txt'):
        print()
        print(CRT+'<')
        print(resultatTest[:len(CRT)])
        print('---------')
        break

print('1:', resultat)
for i in range(0, 240, 40):
    print(CRT[i:i+40])
