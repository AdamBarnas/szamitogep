macierz = [[0, 1, 0, 1, 0, 1],
           [1, 0, 1, 0, 1, 0],
           [0, 1, 1, 1, 1, 1],
           [1, 0, 1, 1, 1, 1],
           [0, 1, 1, 1, 1, 1],
           [1, 0, 1, 1, 1, 1]]

macierz2 = [[1, 1, 0, 1, 0, 1],
            [1, 1, 1, 0, 1, 0],
            [0, 1, 1, 1, 1, 1],
            [1, 0, 1, 1, 1, 1],
            [0, 1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1, 1]]


def zera(macierz):
    rozmiar = len(macierz[0])
    pomocnicza = [[0 for _ in range(rozmiar)] for _ in range(rozmiar)]
    row = [0 for _ in range(rozmiar)]
    col = [0 for _ in range(rozmiar)]
    for i in range(rozmiar):
        for j in range(rozmiar):
            if macierz[i][j] == 0:
                pomocnicza[i][j] = 1
                row[i] += 1
                col[j] += 1
    idx = [-1, -1]
    wybrane = [set(), set()]
    niezalezne = []
    for _ in range(rozmiar):
        minimum = rozmiar * 2
        changed = False
        for i in range(rozmiar):
            for j in range(rozmiar):
                if pomocnicza[i][j] == 1 and row[i] + col[j] < minimum and i not in wybrane[0] and j not in wybrane[1]:
                    minimum = row[i] + col[j]
                    idx = [i, j]
                    changed = True
        if not changed:
            break
        wybrane[0].add(idx[0])
        wybrane[1].add(idx[1])
        niezalezne.append(idx)
    return niezalezne


print(zera(macierz))
print(zera(macierz2))
