from typing import List

from redukcja import reduction
import optymistyczne_wyznaczenie_odc as owo
from zabranianie_podcykli import zabranianie
from kryteria_zamykania import rozmiar, kryteria_zamykania
import numpy as np

class Podproblem:
    def init(self, macierz: list[list[int]], LB=float("inf"), wybrane=[], zabronione=[], typ=True):
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
    else:
        P.M[P.zabronione[-1][1]][P.zabronione[-1][0]] = float("inf")
    P.M, P.LB = reduction(P.M)
    return P    # zmienione parametry podproblemu



def little(M):
    best = float("inf")  # najlepsze znalezione rozwiazanie do tej pory
    zredukowana, LB = reduction(M)
    LP = []  # listapodproblemow
    #optymistyczne wyznaczanie odcinka
    odcinek, koszt = owo.optymistyczne_wyznaczanie_odc(zredukowana)
    LP.append(Podproblem(zredukowana, LB, wybrane=[odcinek], typ=True))
    LP.append(Podproblem(zredukowana, LB, zabronione=[odcinek], typ=False))
    while len(LP) > 0:
        podproblem = LP.pop(0)
        podproblem = krok3(podproblem)
        KZ = kryteria_zamykania(podproblem.M, LB, podproblem.LB)
        if KZ == "KZ0":
            odcinek, koszt = owo.optymistyczne_wyznaczanie_odc(podproblem.M)
            wybrane = podproblem.wybrane
            zabronione = podproblem.zabronione
            LP.append(Podproblem(podproblem.M, LB, wybrane + [odcinek], zabronione, typ=True))
            LP.append(Podproblem(podproblem.M, LB, wybrane, zabronione + [odcinek], typ=False))
        elif KZ == "KZ2":
            pass
        elif KZ == "KZ3":
            pass
        else:
            print("error")
            break

        # LP.append(PP)

    return best

#test
mat1 = [[float("inf"),1,0,2,2],
       [3,float("inf"),2,0,1],
       [1,2,float("inf"),2,0],
       [4,0,3,float("inf"),4],
       [0,2,7,0,float("inf")]]
print(np.array(mat1))
print(little(mat1))