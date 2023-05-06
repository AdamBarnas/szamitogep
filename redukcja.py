from typing import List
from main import macierz


# funkcja jako parametr przyjmuje macierz, którą będzie redukować
def reduction(matrix: List[List[int]]):
    row_subtraction = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    # przygotowanie miejsca na macierz po redukcji wierszy
    total_reduction = 0  # dolne ograniczenie wartości funkcji celu
    for row in range(len(matrix)):  # przejście po wierszach
        min_val = min(matrix[row])  # najmniejszy element w wierszu
        for col in range(len(matrix)):  # przejście po kolejnych elementach wiersza
            row_subtraction[row][col] = matrix[row][col] - min_val
            # nowa macierz po redukcji wierszy
        total_reduction += min_val  # dodanie minimalnego elementu do sumarycznej redukcji

    col_subtraction = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    # przygotowanie miejsca na macierz po redukcji kolumn

    for col in range(len(matrix)):  # przejście po kolumnach
        col_vals = [row_subtraction[row][col] for row in range(len(matrix))]
        # uzyskanie kolumny
        min_val = min(col_vals)  # najmniejszy element w kolumnie
        for row in range(len(matrix)):  # przejście po kolejnych elementach kolumny
            col_subtraction[row][col] = row_subtraction[row][col] - min_val
            # nowa macierz po redukcji kolumn
        total_reduction += min_val  # dodanie minimalnego elementu do sumarycznej redukcji

    return col_subtraction, total_reduction
    # zwraca macierz po obu redukcjach i dolne ograniczenie wartości funkcji celu

# col_subtraction, total_reduction = reduction(macierz)
# print(col_subtraction, total_reduction)
