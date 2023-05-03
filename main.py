from zera import zera
from redukcja import reduction
from wykreslanie import wykreslanie
from proba import proba
macierz = [[1, 5, 1, 8, 1, 3],
           [4, 3, 7, 3, 6, 3],
           [2, 4, 7, 8, 4, 5],
           [4, 3, 6, 7, 6, 5],
           [4, 7, 5, 6, 6, 9],
           [7, 2, 4, 3, 5, 9]]

def algorytm(macierz):
    size = len(macierz)
    zredukowana, koszt = reduction(macierz)
    niezalezne, wszystkie, wiersze, kolumny = zera(zredukowana)
    if len(niezalezne) == size:
        return niezalezne, koszt
    else:
        while len(niezalezne) < size:
            w_wiersze, w_kolumny = wykreslanie(zredukowana, wszystkie, wiersze, kolumny)
            zredukowana, sigma = proba(zredukowana, w_wiersze, w_kolumny)
            koszt += sigma
            niezalezne, wszystkie, wiersze, kolumny = zera(zredukowana)
        return niezalezne, koszt

rozwiazanie, koszt = algorytm(macierz)
print(rozwiazanie)
print(koszt)



