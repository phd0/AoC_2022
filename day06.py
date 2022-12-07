import sys

infile = sys.argv[1] if len(sys.argv) > 1 else 'day06.txt'
with open(infile) as file:
    ligne = file.readline().strip('\n')

print(ligne)
for i in range(3, len(ligne)):
    # print(i, ' ', end='')
    # print(ligne[i], ligne[i-1], ligne[i-2], ligne[i-3])
    if (ligne[i] not in [ligne[i-1], ligne[i-2], ligne[i-3]]
            and ligne[i-1] not in [ligne[i], ligne[i-2], ligne[i-3]]
            and ligne[i-2] not in [ligne[i-1], ligne[i], ligne[i-3]]
            and ligne[i-3] not in [ligne[i-1], ligne[i-2], ligne[i]]
            ):
        break
print(i+1)
