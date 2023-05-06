def proba(macierz, w_wier, w_kol):
    poprzedni = [-1, -1]
    krotnosc = 0
    for i in range(len(macierz)):
        if i in w_wier:
            pass
        else:
            for j in range(len(macierz)):
                if j not in w_kol:
                    if poprzedni == [-1, -1] or macierz[poprzedni[0]][poprzedni[1]] > macierz[i][j]:
                        poprzedni = [i, j]
                        krotnosc = 1
                    elif macierz[poprzedni[0]][poprzedni[1]] == macierz[i][j]:
                        krotnosc += 1

    najmniejszy = macierz[poprzedni[0]][poprzedni[1]]
    for i in range(len(macierz)):
        for j in range(len(macierz)):
            if i not in w_wier and j not in w_kol:
                macierz[i][j] -= najmniejszy
            elif i in w_wier and j in w_kol:
                macierz[i][j] += najmniejszy
    koszt = krotnosc*najmniejszy
    # print(macierz, koszt)
    return macierz, koszt
