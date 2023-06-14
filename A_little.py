from redukcja import reduction

class Podproblem:
    def init(self, macierz, ograniczenie, typ, LB=float("inf"), parent=None, children=[]):
        self.M = macierz
        self.ograniczenie = ograniczenie
        self.LB = LB
        self.parent = parent
        self.pochodne = children
        self.typ = typ

def krok3(P: Podproblem):
    if P.typ:
        P.M[P.ograniczenie[0]][P.ograniczenie[1]] = float("inf")
        zredukowana, LB = reduction(P.M)

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
        krok3(podproblem)

