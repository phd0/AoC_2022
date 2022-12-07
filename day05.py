import queue
import sys
ligne = ""
i = 0
q = []
qq = []


def print_q(objet):
    for i in range(9):
        print(i, end=' ')
        if (not objet[i].empty()):
            print(objet[i].queue, end='')
        print()


def reverseQueue(q1src, q2dest):
    buffer = q1src.get()
    if (q1src.empty() == False):
        reverseQueue(q1src, q2dest)  # using recursion
    q2dest.put(buffer)
    return q2dest


def analyse(objet, _move,  _from, _to):
    for i in range(_move):
        objet[_to].put(objet[_from].get())


def charge1():
    infile = sys.argv[1] if len(sys.argv) > 1 else 'day05.txt'
    for i in range(9):
        q.append(queue.LifoQueue())
        qq.append(queue.Queue())

    with open(infile) as file:
        ligne = file.readline().strip('\n')
        i = 0
        while '[' in ligne:
            for j in range(0, len(ligne), 4):
                pass
                if (ligne[j+1] != ' '):
                    qq[int(j/4)].put(ligne[j+1])
            ligne = file.readline().strip('\n')
            i += 1
        # retournement des 9 piles
        for i in range(9):
            if (not qq[i].empty()):
                reverseQueue(qq[i], q[i])

        ligne = file.readline().strip('\n')  # ligne blanche
        ligne = file.readline().strip('\n')  # 1er ligne avec un 'move'
        while ('move' in ligne):
            _b0, _move, _b1, _from, _b2, _to = ligne.split(' ')
            analyse(q, int(_move), int(_from)-1, int(_to)-1)
            ligne = file.readline().strip('\n')


charge1()
for i in range(9):
    if (not q[i].empty()):
        print(q[i].get(), end='')
print()

# partie 2
q = []
qq = []
