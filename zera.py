macierz = [[0, 1, 0, 1, 0, 1],
           [1, 0, 1, 0, 1, 0],
           [0, 1, 1, 1, 1, 1],
           [1, 0, 1, 1, 1, 1],
           [0, 1, 1, 1, 1, 1],
           [1, 0, 1, 1, 1, 1]]

macierz2 = [[1, 1, 0, 1, 0, 1],
            [1, 1, 1, 0, 1, 0],
            [0, 1, 1, 1, 0, 1],
            [1, 0, 1, 1, 1, 1],
            [0, 1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1, 1]]


def zera(macierz):
    rozmiar = len(macierz[0])
    row = [0 for _ in range(rozmiar)]  # lista zliczająca zera w wierszach
    col = [0 for _ in range(rozmiar)]  # lista zliczająca zera w kolumnach
    wszystkie = set()  # zbiór współrzędnych zer
    for i in range(rozmiar):  # pętla znajdująca zera i uzupełniająca listy
        for j in range(rozmiar):
            if macierz[i][j] == 0:
                row[i] += 1
                col[j] += 1
                wszystkie.add((i, j))
    wiersze = row.copy()  # kopiowanie danch z list aby ich nie naruszyć dalszym działaniem algorytmu
    kolumny = col.copy()
    idx = (-1, -1)
    wybrane = [set(), set()]  # zbiory zawierajace numery wierszy i kolumn zer wybranych jako niezależne
    niezalezne = set()  # zbiór współrzędnych zer niezależnych
    for _ in range(rozmiar):  # pętla wywoływana n razy dla znalezienia n zer niezależnych
        minimum = rozmiar * 2
        changed = False
        for i in range(rozmiar):  # pętla znajdująca zero z minimalną sumą liczby innych zer w tej samej kolumnie lub wierszu
            for j in range(rozmiar):
                if macierz[i][j] == 0 and row[i] + col[j] < minimum and i not in wybrane[0] and j not in wybrane[1]:
                    minimum = row[i] + col[j]
                    idx = (i, j)
                    changed = True
        if not changed:  # ewentualne przerwanie pętli w przypadku nieznalezienia kolejnego zera
            break
        wybrane[0].add(idx[0])
        wybrane[1].add(idx[1])
        for j in range(rozmiar):   # aktualizacja informacji o liczebności zer w kolumnach
            if macierz[idx[0]][j] == 0:
                col[j] -= 1
        for i in range(rozmiar):   # aktualizacja informacji o liczebności zer w wierszach
            if macierz[i][idx[1]] == 0:
                row[i] -= 1
        row[idx[0]] = 0
        col[idx[1]] = 0
        niezalezne.add(idx)   # dodanie zera do zbioru zer niezależnych
        # zalezne = wszystkie - niezalezne
    return niezalezne, wszystkie, wiersze, kolumny


# print(zera(macierz)[0])
# print(zera(macierz)[1])
# print(zera(macierz2)[0])
# print(zera(macierz2)[1])
