total1 = 0
total2 = 0

with open('day02.txt') as file:
    map = file.readlines()

for ligne in map:
    #    analyse(ligne)
    ABC, XYZ = ligne.split()
    total1 += {"X": 1, "Y": 2, "Z": 3}[XYZ]
    total1 += {('A', 'X'): 3, ('A', 'Y'): 6, ('A', 'Z'): 0,
               ('B', 'X'): 0, ('B', 'Y'): 3, ('B', 'Z'): 6,
               ('C', 'X'): 6, ('C', 'Y'): 0, ('C', 'Z'): 3}[ABC, XYZ]

    total2 += {"X": 0, "Y": 3, "Z": 6}[XYZ]
    total2 += {('A', 'X'): 3, ('A', 'Y'): 1, ('A', 'Z'): 2,
               ('B', 'X'): 1, ('B', 'Y'): 2, ('B', 'Z'): 3,
               ('C', 'X'): 2, ('C', 'Y'): 3, ('C', 'Z'): 1}[ABC, XYZ]

print("etape 1:", total1)
print("etape 2:", total2)
