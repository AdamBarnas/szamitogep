from typing import List
import copy
from redukcja import reduction
import optymistyczne_wyznaczenie_odc as owo
# from zabranianie_podcykli import zabranianie
from zabranianie_V2 import zabranianie
from kryteria_zamykania import rozmiar, kryteria_zamykania
import numpy as np


class Podproblem:
    def __init__(self, macierz, LB, wybrane, zabronione, typ):
        self.M = macierz
        self.zabronione = zabronione
        self.LB = LB
        self.wybrane = wybrane
        self.typ = typ


def krok3(P: Podproblem):
    if P.typ:
        for i in range(len(P.M)):
            P.M[P.wybrane[-1][0]][i] = float("inf")
        for i in range(len(P.M)):
            P.M[i][P.wybrane[-1][1]] = float("inf")
        P.M[P.wybrane[-1][1]][P.wybrane[-1][0]] = float("inf")
        zabranianie(P.M, P.wybrane)
    else:
        P.M[P.zabronione[-1][1]][P.zabronione[-1][0]] = float("inf")
    P.M, LB = reduction(P.M)
    P.LB += LB
    return P  # zmienione parametry podproblemu


def little(M):
    best = float("inf")  # najlepsze znalezione rozwiazanie do tej pory
    zredukowana, LB = reduction(M)
    LP = []  # listapodproblemow
    # optymistyczne wyznaczanie odcinka
    odcinek1, koszt = owo.optymistyczne_wyznaczanie_odc(zredukowana)
    m1 = copy.deepcopy(zredukowana)
    m2 = copy.deepcopy(zredukowana)
    LP.append(Podproblem(m1, LB, [odcinek1], [], True))
    LP.append(Podproblem(m2, LB, [], [odcinek1], False))
    while len(LP) > 0:
        minlb = float('inf')
        for pp in LP:
            if pp.LB < minlb:
                minlb = pp.LB
                podproblem = pp
        LP.remove(podproblem)
        podproblem = krok3(podproblem)
        KZ = kryteria_zamykania(podproblem.M, best, podproblem.LB)
        # print()
        # print(owo.find_zeros(podproblem.M))
        # print(np.array(podproblem.M))
        # print(podproblem.wybrane)
        # print(podproblem.zabronione)
        # print()
        if KZ == "KZ0":
            odcinek, koszt = owo.optymistyczne_wyznaczanie_odc(podproblem.M)
            wybrane = podproblem.wybrane.copy()
            zabronione = podproblem.zabronione.copy()
            m1 = copy.deepcopy(podproblem.M)
            m2 = copy.deepcopy(podproblem.M)
            LP.insert(0, Podproblem(m1, LB, wybrane + [odcinek], zabronione, True))
            LP.append(Podproblem(m2, LB, wybrane, zabronione + [odcinek], False))
        elif KZ == "KZ3":
            wolnezera = owo.find_zeros(podproblem.M)
            for i in wolnezera:
                for j in wolnezera:
                    if all(i[k] != j[k] for k in range(len(i))):
                        if i not in podproblem.wybrane:
                            podproblem.wybrane.append(i)
                        if j not in podproblem.wybrane:
                            podproblem.wybrane.append(j)
            print()
            print(np.array(podproblem.M))
            print(zabranianie(podproblem.M, podproblem.wybrane))
            print(podproblem.wybrane)
            print(podproblem.zabronione)
            if best > podproblem.LB:
                best = podproblem.LB

        elif KZ == "KZ2":
            print("zamykamy KZ2")
        else:
            print("error")
            break

        # LP.append(PP)

    return best


# test
mat1 = [[float("inf"), 1, 0, 2, 2],
        [3, float("inf"), 2, 0, 1],
        [1, 2, float("inf"), 2, 0],
        [4, 0, 3, float("inf"), 4],
        [0, 2, 7, 0, float("inf")]]
# mat1 = np.array([
#     [float('inf'), 1, 5, 3, 1, 4, 2, 3, 7],
#     [2, float('inf'), 3, 3, 3, 1, 4, 1, 2],
#     [4, 3, float('inf'), 5, 2, 4, 2, 2, 6],
#     [6, 5, 5, float('inf'), 1, 9, 6, 1, 2],
#     [5, 7, 1, 3, float('inf'), 8, 7, 2, 4],
#     [4, 3, 7, 3, 9, float('inf'), 2, 6, 2],
#     [1, 5, 6, 1, 3, 7, float('inf'), 8, 5],
#     [7, 2, 6, 1, 6, 7, 3, float('inf'), 2],
#     [7, 2, 6, 1, 6, 1, 3, 2, float('inf')]
# ])
print(np.array(mat1))
print(little(mat1))
