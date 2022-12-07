import sys
from collections import defaultdict

infile = sys.argv[1] if len(sys.argv) > 1 else 'day07.txt'
data = open(infile).read().strip()
lines = [x for x in data.split('\n')]
SZ = defaultdict(int)
path = []

for line in lines:
    words = line.strip().split()
    if (len(words) > 0 and words[1] == 'cd'):
        if (words[2] == '..'):
            path.pop()
        else:
            path.append(words[2])
    elif (len(words) > 0 and words[1] == 'ls'):
        continue
    elif (len(words) > 0 and words[0] == 'dir'):
        continue
    else:
        sz = int(words[0])
        for i in range(len(path)+1):
            SZ['/'.join(path[:i])] += sz
            #print(path[:i], SZ['/'.join(path[:i])])

ans = 0
for k, v in SZ.items():
    if v < 100000:
        ans += v
freespace = 70000000-SZ['/']
requ = 30000000-freespace

print('1:', ans)
print('freespace', freespace)
print('requ', requ)

ans2 = 70000000
for k, v in SZ.items():
    if (v >= requ and v < ans2):
        ans2 = v
print('2:', ans2)
