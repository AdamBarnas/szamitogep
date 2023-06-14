from redukcja import reduction

class Podproblem:
    def init(self, macierz, ograniczenie, typ, LB=float("inf"), parent=None, children=[]):
        self.M = macierz
        self.ograniczenie = ograniczenie
        self.LB = LB
        self.parent = parent
        self.pochodne = children
        self.typ = typ

def krok3(P: Podproblem, old_LB, best):
    if P.typ:
        for i in range(len(P.M)):
            P.M[P.ograniczenie[0]][i] = float("inf")
        for i in range(len(P.M)):
            P.M[i][P.ograniczenie[1]] = float("inf")
        P.M[P.ograniczenie[1]][P.ograniczenie[0]] = float("inf")
        zredukowana, LB = reduction(P.M)
    else:
        P.M[P.ograniczenie[1]][P.ograniczenie[0]] = float("inf")

    # sprawdzenie dolnego ograniczenia
    return "PP"    #"""kolejny problem"""


def little(M):
    best = float("inf") # najlepsze znalezione rozwiazanie do tej pory
    zredukowana, LB = reduction(M)
    LP = []  # listapodproblemow
    #optymistyczne wyznaczanie odcinka
    odcinek = None   # wyznaczanie(zredukowana)
    LP.append(Podproblem(zredukowana, odcinek, False, LB))
    LP.append(Podproblem(zredukowana, odcinek, True, LB))
    while len(LP) > 0:
        podproblem = LP.pop()
        PP = krok3(podproblem, LB, best)
        LP.append(PP)

    return best

