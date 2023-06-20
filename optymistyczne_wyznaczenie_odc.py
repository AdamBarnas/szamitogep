#pomocnicza funkcja by wyłuskać kolumnę
def column(matrix, i):
    return [r[i] for r in matrix]

#pomocnicza funkcja by utworzyć listę zer
def find_zeros(macierz_zredukowana):
    zeros_list = []
    for i, row in enumerate(macierz_zredukowana):
        for j, val in enumerate(row):
            if macierz_zredukowana[i][j] == 0:
                zeros_list.append((i,j))
    return zeros_list

#wyznaczanie odcinka o max. opt. koszcie yłączenia
#zwraca odcinek w postaci krotki (wiersz, kolumna)
def optymistyczne_wyznaczanie_odc(macierz_zredukowana):
    #utworzenie listy zer i inicjalizacja zmiennych
    zeros_list = find_zeros(macierz_zredukowana)
    zero_opt = (-1, -1)
    max_cost = 0
    for zero in zeros_list:
        min_in_row = float("inf")
        min_in_col = float("inf")
        #szukanie minimum w wierszu
        for i in macierz_zredukowana[zero[0]]:
            if i < min_in_row and i != 0:
                min_in_row = i
        col = column(macierz_zredukowana, zero[1])
        #szukanie minumum w kolumnie
        for j in col:
             if j < min_in_col and j != 0:
                min_in_col = j
        #szukany odcinek to max spośrów (min_in_col + min_in_row)
        if max_cost < (min_in_row+min_in_col) and (min_in_row+min_in_col) != float('inf'):
            max_cost = (min_in_row+min_in_col)
            zero_opt = zero         

    return zero_opt, max_cost

# #test
# import numpy as np
# mat1 = [[float("inf"),1,0,2,2],
#        [3,float("inf"),2,0,1],
#        [1,2,float("inf"),2,0],
#        [4,0,3,float("inf"),4],
#        [0,2,7,0,float("inf")]]
# print(np.array(mat1))
# print(optymistyczne_wyznaczanie_odc(mat1))