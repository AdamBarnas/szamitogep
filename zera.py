macierz = [[0, 1, 1, 1],
           [1, 1, 0, 1],
           [1, 0, 1, 1],
           [1, 1, 1, 0]]
def zera(macierz):
    rozmiar = len(macierz[0])
    pomocnicza = [[0 for _ in range(rozmiar)]for _ in range(rozmiar)]
    row = [0 for _ in range(rozmiar)]
    col = [0 for _ in range(rozmiar)]
    for i in range(rozmiar):
        for j in range(rozmiar):
            if macierz[i][j] == 0:
                pomocnicza[i][j] = 1
                row[i] += 1
                col[j] += 1
    minimum = rozmiar*2
    idx = [-1, -1]
    wybrane = [set(), set()]
    niezalezne = []
    for _ in range(rozmiar):
        changed = False
        for i in range(rozmiar):
            for j in range(rozmiar):
                if row[i] + col[j] < minimum and i not in wybrane[0] and j not in wybrane[1]:
                    idx = [i, j]
                    changed = True
        if not changed:
            break
        wybrane[0].add(idx[0])
        wybrane[1].add(idx[1])
        niezalezne.append(idx)
    print(niezalezne)

zera(macierz)


