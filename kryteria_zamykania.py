# funkcja pomocnicza sprawdzająca rozmiar macierzy, 
# zmiejszanie rozmiaru macierzy (wykreślanie wuerszy) realizowane poprzez wpisanie INF
def rozmiar(macierz):
    wymiar = 0
    row_inf = [float("inf") for i in range(len(macierz))]
    for row in macierz:
        if row != row_inf:
            wymiar += 1
    return wymiar 

# funkacja ma służyć próbie zamknięcia podroblemu w oparciu o odpowiednie kryteria: KZ1, KZ2, KZ3 
# i KZ0 czyli podział na kolejne podproblemy
def kryteria_zamykania(macierz_podrpoblem, LB_min, LB_podproblem):
    # domyślnie podproblem będzie podzielony na lewą (która dany łuk zawiera) i prawą gałąź (kótr go nie zwiera)
    KZ = "KZ0"
    # jeśli rozmiar macierzy = 2
    if rozmiar(macierz=macierz_podrpoblem) == 2:
        KZ = "KZ3"
    elif LB_min >= LB_podproblem:
        KZ = "KZ2"
    return KZ
        




# # do test   -c 
# m1 = [[float("inf"),float("inf"),float("inf"),float("inf")],
#       [1,2,float("inf"),4],
#       [1,2,float("inf"),4],
#       [0,0,float("inf"),float("inf")]]
# print(rozmiar(macierz=m1))
