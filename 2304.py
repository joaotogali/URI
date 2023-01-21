# Ler I (quantia de dinheiro inicial de todos participantes)
# Ler o numero de operações realizadas durante o jogo
from typing import Type

i: Type[int]
o: Type[int]
i, o = int, input().split()

D = i
E = i
F = i

x = []*4
while o != 0:
    o: type[int]
    o -= 1
    x.append(input().split())
    x[2] = int(x[2])
    x[3] = int(x[3])

    if x[0] == 'C':
        if x[1] == 'D':
            D -= x[2]
        if x[1] == 'E':
            E -= x[2]
        if x[1] == 'F':
            F -= x[2]

    elif x[0] == "V":

        if x[1] == "D":
            D += x[2]
        if x[1] == "E":
            E += x[2]
        if x[1] == "F":
            F += x[2]

    elif x[1] == "D":

        if x[2] == "E":
            D += x[3]
            E -= x[3]
        if x[2] == "F":
            D += x[3]
            F -= x[3]

    elif x[1] == "E":

        if x[2] == "D":
            E += x[3]
            D -= x[3]
        if x[2] == "F":
            E += x[3]
            F -= x[3]

    elif x[1] == "F":

        if x[2] == "E":
            F += x[3]
            E -= x[3]
        if x[2] == "D":
            D -= x[3]
            F += x[3]

    print(D, E, F)


