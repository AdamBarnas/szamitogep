from zera import zera
from redukcja import reduction
from wykreslanie import wykreslanie
macierz = [[1, 5, 1, 8, 1, 3],
           [4, 3, 7, 3, 6, 3],
           [2, 4, 7, 8, 4, 5],
           [4, 3, 6, 7, 6, 5],
           [4, 7, 5, 6, 6, 9],
           [7, 2, 4, 3, 5, 9]]

# TODO redukcja macierzy

# TODO wyznaczamy zera niezależne i niezależne
#  a jeśli jest ich n to mamy rozwiązanie optymalne

# TODO sprawdzenie liczby zer zależnych

# TODO wykreślanie jeśli n zer niezależnych to koniec

# TODO powiekszanie zbioeu libcz niezależnych

def algorytm(macierz):
    size = len(macierz)
    zredukowana, koszt = reduction(macierz)
    niezalezne, wszystkie, wiersze, kolumny = zera(zredukowana)
    if len(niezalezne) == size:
        return niezalezne, koszt
    w_wiersze, w_kolumny = wykreslanie(zredukowana, wszystkie, wiersze, kolumny)

algorytm(macierz)



