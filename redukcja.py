from typing import List

def reduction(matrix: List[List[int]]):
    inf = 99999
    el_to_subtract = []
    row_subraction = matrix.copy()
    lower_reduction = 0
    for row in range(len(matrix)):
        min = inf
        for col in range(len(matrix)):
            if matrix[row][col] < min:
                min = matrix[row][col]
        el_to_subtract.append(min)

    for row in range(len(matrix)):
        for col in range(len(matrix)):
            row_subraction[row][col] -= el_to_subtract[row]
            lower_reduction += el_to_subtract[row]

    col_subtraction = row_subraction.copy()
    el_to_subtract.clear()

    for col in range(len(matrix)):
        min = inf
        for row in range(len(matrix)):
            if row_subraction[row][col] < min:
                min = row_subraction[row][col]
        el_to_subtract.append(min)

    for col in range(len(matrix)):
        for row in range(len(matrix)):
            col_subtraction[row][col] -= el_to_subtract[col]
            lower_reduction += el_to_subtract[col]


