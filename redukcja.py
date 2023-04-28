from typing import List
from main import macierz


def reduction(matrix: List[List[int]]):
    el_to_subtract = []
    row_subtraction = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    lower_reduction = 0
    for row in range(len(matrix)):
        min_val = min(matrix[row])
        el_to_subtract.append(min_val)
        for col in range(len(matrix)):
            row_subtraction[row][col] = matrix[row][col] - min_val
        lower_reduction += min_val

    col_subtraction = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    el_to_subtract.clear()

    for col in range(len(matrix)):
        col_vals = [row_subtraction[row][col] for row in range(len(matrix))]
        min_val = min(col_vals)
        el_to_subtract.append(min_val)
        for row in range(len(matrix)):
            col_subtraction[row][col] = row_subtraction[row][col] - min_val
        lower_reduction += min_val

    return col_subtraction, lower_reduction


# col_subtraction, lower_reduction = reduction(macierz)
# print(col_subtraction, lower_reduction)
