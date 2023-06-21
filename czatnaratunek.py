import numpy as np
from math import inf


def reduce_row(mat):
    fi = 0
    for i in range(len(mat)):
        min_val = np.min(mat[i])
        fi += min_val
        mat[i] -= min_val
    return mat, fi


def reduce_col(mat):
    list_min = []
    fi = 0
    for i in range(len(mat[0])):
        min_val = inf
        for j in range(len(mat)):
            if mat[j][i] < min_val:
                min_val = mat[j][i]
        list_min.append(min_val)
        fi += min_val

    for i in range(len(mat[0])):
        for j in range(len(mat)):
            try:
                mat[j][i] -= list_min[i]
            except:
                pass
    return mat, fi


def reduce_matrix(mat):
    n = len(mat)
    m = len(mat[0])

    print(f'\nInitial Matrix:\n{mat}')

    mat1, fi1 = reduce_row(mat)
    mat2, fi2 = reduce_col(mat1)
    print(f'\nMatrix after column reduction:\n{mat2}')

    return mat2, fi1 + fi2


def choose_path(mat, lista, rozw, lr=None, lc=None):
    if lr is None:
        lr = list(range(1, len(mat) + 1))
    if lc is None:
        lc = list(range(1, len(mat[0]) + 1))

    d = dict()
    dk = dict()

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                row_vals = [mat[i][jj] for jj in range(len(mat[i])) if jj != j]
                min_row = min(row_vals)

                col_vals = [mat[ii][j] for ii in range(len(mat)) if ii != i]
                min_col = min(col_vals)

                d[(i, j)] = max(min_row, min_col)
                dk[(lr[i], lc[j])] = max(min_row, min_col)

    max_edge = None
    maxi = -inf
    for k, v in d.items():
        if v > maxi:
            maxi = v
            max_edge = k

    h = None
    maxi = -inf
    for k, v in dk.items():
        if v > maxi:
            maxi = v
            h = k

    if len(mat) <= 2:
        rozw.append(list(dk.keys())[1])
    lista.append(max_edge)
    rozw.append(h)

    return max_edge, h, lr, lc, lista, rozw


def update_matrix(mat, e, hh, cost, lista, rozw, lr=None, lc=None):
    r = len(mat)
    c = len(mat[0])

    row_vals = [mat[e[0]][jj] for jj in range(len(mat[e[0]])) if jj != e[0]]
    min_row = min(row_vals)

    col_vals = [mat[ii][e[1]] for ii in range(len(mat)) if ii != e[1]]
    min_col = min(col_vals)

    h = max(min_row, min_col)
    print(f'Cost of not selecting: {cost + h}')

    if lr is None:
        lr = list(range(1, len(mat) + 1))
    if lc is None:
        lc = list(range(1, len(mat[0]) + 1))

    mat = np.delete(mat, e[0], axis=0)
    lr.pop(e[0])

    mat = np.delete(mat, e[1], axis=1)
    lc.pop(e[1])

    print(f'New matrix:\n{mat}')

    if len(mat) > 2:
        e, hh, lr, lc, lista, rozw = choose_path(mat, lista, rozw, lr, lc)
        return update_matrix(mat, e, hh, cost + h, lista, rozw, lr, lc)

    return mat, lista, rozw


# Main algorithm
def hungarian_algorithm(cost_matrix):
    matrix = np.array(cost_matrix)

    matrix, fi = reduce_matrix(matrix)
    print(f'\nReduced Matrix:\n{matrix}')

    e, hh, lr, lc, lista, rozw = choose_path(matrix, [], [], list(range(1, len(matrix) + 1)),
                                             list(range(1, len(matrix[0]) + 1)))
    print(f'Initial edge: {e}')

    matrix, lista, rozw = update_matrix(matrix, e, hh, 0, lista, rozw, lr, lc)
    print('\nFinal Result:')
    for elem in rozw:
        print(f'Agent {elem[0]} assigned to Task {elem[1]}')

    print(f'Total Cost: {fi + sum(matrix.flatten())}')


# Sample cost matrix
matrix = np.array([
    [inf, 1, 5, 3, 1, 4, 2, 3, 7],
    [2, inf, 3, 3, 3, 1, 4, 1, 2],
    [4, 3, inf, 5, 2, 4, 2, 2, 6],
    [6, 5, 5, inf, 1, 9, 6, 1, 2],
    [5, 7, 1, 3, inf, 8, 7, 2, 4],
    [4, 3, 7, 3, 9, inf, 2, 6, 2],
    [1, 5, 6, 1, 3, 7, inf, 8, 5],
    [7, 2, 6, 1, 6, 7, 3, inf, 2],
    [7, 2, 6, 1, 6, 1, 3, 2, inf]
])

hungarian_algorithm(matrix)
