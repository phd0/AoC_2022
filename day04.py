import sys

infile = sys.argv[1] if len(sys.argv) > 1 else 'day04.txt'
with open(infile) as file:
    map = file.readlines()
    map = [line.strip() for line in map]
total1 = 0
total2 = 0

for ligne in map:
    X1, X2 = ligne.split(',')
    xa, xb = X1.split('-')
    ya, yb = X2.split('-')
    if (int(xa) >= int(ya) and int(xb) <= int(yb)
            or int(ya) >= int(xa) and int(yb) <= int(xb)):
        total1 += 1
#        print(X1, X2)
    if (int(xa) >= int(ya) and int(xa) <= int(yb)
            or int(ya) >= int(xa) and int(ya) <= int(xb)
            or int(xb) >= int(ya) and int(xb) <= int(ya)
            or int(yb) >= int(xa) and int(yb) <= int(xb)
        ):
        total2 += 1
        # print(X1, X2)


print("resultat 1:", total1)
print("resultat 2:", total2)
