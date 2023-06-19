from redukcja import reduction


def zabranianie(matrix, LB):
    # lista dla minimów z wierszy
    min_vals_from_rows = []
    # poszukiwanie minimów w wierszach
    for row in range(len(matrix)):
        amount_of_zeros = 0  # zmienna do zliczania zer w wierszu
        min_val = float("inf")
        for col in range(len(matrix[row])):
            if matrix[row][col] < min_val:
                if matrix[row][col] == 0:
                    amount_of_zeros += 1
                    # jeżeli jest 2 lub więcej zer w wierszu to minimum to 0
                    if amount_of_zeros >= 2:
                        min_val = matrix[row][col]
                else:
                    min_val = matrix[row][col]
        # dodajemy minimum do listy z minimami z wierszy
        min_vals_from_rows.append(min_val)
    # lista dla minimów z kolumn
    min_vals_from_cols = []
    for col in range(len(matrix)):
        amount_of_zeros = 0 # zmienna do zliczania zer w kolumnie
        min_val = float("inf")
        # poszukiwanie minimów w wierszach
        for row in range(len(matrix)):
            if matrix[row][col] < min_val:
                if matrix[row][col] == 0:
                    amount_of_zeros += 1
                    # jeżeli jest 2 lub więcej zer w kolumnie to minimum to 0
                    if amount_of_zeros >= 2:
                        min_val = matrix[row][col]
                else:
                    min_val = matrix[row][col]
        # dodajemy minimum do listy z minimami z kolumn
        min_vals_from_cols.append(min_val)
    first_PP = matrix
    second_PP = matrix
    LB_1 = LB
    LB_2 = LB
    max_elem_from_rows = max(min_vals_from_rows)  # maksimum z minimów z wierszy
    max_elem_from_cols = max(min_vals_from_cols)  # maksimum z minimów z kolumn
    # pierwszy PP (wykreślamy, zabraniamy podcyklu, do LB dodajemy wyznaczone maksimum z minimów)
    if max_elem_from_rows >= max_elem_from_cols:
        id_row = max(enumerate(min_vals_from_rows), key=lambda x: x[1])[0]  # id maksimum z wierszy
        for col in range(len(first_PP[id_row])):
            # poszukiwania 0 dla danego wiersza
            if first_PP[row][col] == 0:
                id_col_with_0 = col
                break
        # wykreślanie i*-wiersza i j*-kolumny
        for col in range(len(first_PP[id_row])):
            first_PP[id_row][col] = float("inf")
        for row in range(len(first_PP[id_col_with_0])):
            first_PP[row][id_col_with_0] = float("inf")
        first_PP[id_col_with_0][id_row] = float("inf")  # zabraniamy <i*j*>
        LB_1 += reduction(first_PP)[1]  # uaktualnienie LB
        # drugi PP (zabraniamy <i*j*>, redukcja, LB)
        second_PP[id_col_with_0][id_row] = float("inf")
        LB_2 += reduction(second_PP)[1]
    else:
        id_col = max(enumerate(min_vals_from_cols), key=lambda x: x[1])[0]  # id maksimum z kolumn
        for row in range(len(first_PP)):
            # poszukiwania 0 dla danej kolumny
            if first_PP[row][id_col] == 0:
                id_row_with_0 = row
                break
        # wykreślanie i*-wiersza i j*-kolumny
        for row in range(len(first_PP)):
            first_PP[row][id_col] = float("inf")
        for col in range(len(first_PP)):
            first_PP[id_row_with_0][col] = float("inf")
        first_PP[id_col][id_row_with_0] = float("inf")  # zabraniamy <i*j*>
        LB_1 += reduction(first_PP)[1]  # uaktualnienie LB
        # drugi PP (zabraniamy <i*j*>, redukcja, LB)
        second_PP[id_col][id_row_with_0] = float("inf")
        LB_2 += reduction(second_PP)[1]
    # print(first_PP)
    return LB_1, LB_2

# matrix = [[float("inf"), 9, 0, 42, 3],
#           [75, float("inf"), 87, 18, 0],
#           [0, 51, float("inf"), 18, 93],
#           [6, 0, 2, float("inf"), 28],
#           [1, 96, 1, 0, float("inf")]]
#
# print(zabranianie(matrix, 19))

