numlist = []

try:
    liste1 = open("day01.txt", "r")
except:
    print("fichier introuvable")
    exit(1)
else:
    summ = 0
    for calories in liste1:
        try:
            summ = summ + int(calories)
        except:
            numlist.append(summ)
            summ = 0

    print(numlist.__len__(), "Elfs")
    print("part 1:", max(numlist))
    numlist.sort()
    if (numlist.__len__() > 3):
        print("part 2:", numlist[-3]+numlist[-2]+numlist[-1])
