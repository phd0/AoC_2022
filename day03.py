import sys

infile = sys.argv[1] if len(sys.argv) > 1 else 'day03.txt'
with open(infile) as file:
    map = file.readlines()
    map = [line.strip() for line in map]
total1 = 0
total2 = 0
car = ''

for ligne in map:
    ll = int(len(ligne)/2)
    maxi = 999
    for i in range(ll):
        car = ligne[i]
        for j in range(ll, ll*2):
            if (ord(ligne[i]) == ord(ligne[j])):
                pass
                if (ord(car) > 64 and ord(car) < 91):
                    #print(ligne, i, j, car, ord(car)-38)
                    if (ord(car)-38 < maxi):
                        maxi = ord(car)-38
                else:
                    #print(ligne, i, j, car, ord(car)-96)
                    if (ord(car)-96 < maxi):
                        maxi = ord(car)-96
    #print('maxi :', maxi)
    total1 += maxi

# partie N°2
for i in range(0, len(map), 3):
    X1 = []
    X2 = []
    X3 = []
    for j in map[i+0]:
        X1.append(j)
    for j in map[i+1]:
        X2.append(j)
    for j in map[i+2]:
        X3.append(j)
    pass
    for k1 in X1:
        if k1 in X2:
            if k1 in X3:
                if (ord(k1) > 64 and ord(k1) < 91):
                    total2 += ord(k1)-38
                else:
                    total2 += ord(k1)-96
                break

print("resultat 1:", total1)
print("resultat 2:", total2)
