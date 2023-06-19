
def zabranianie(matrix):
    min_vals_from_rows = []
    for row in range(len(matrix)):  # przejście po wierszach
        amount_of_zeros = 0
        min_val = float("inf")
        for col in range(len(matrix[row])):
            if matrix[row][col] < min_val:
                if matrix[row][col] == 0:
                    amount_of_zeros += 1
                    if amount_of_zeros >= 2:
                        min_val = matrix[row][col]
                else:
                    min_val = matrix[row][col]

        min_vals_from_rows.append(min_val)

    min_vals_from_cols = []
    for col in range(len(matrix)):  # przejście po wierszach
        amount_of_zeros = 0
        min_val = float("inf")
        for row in range(len(matrix)):
            if matrix[row][col] < min_val:
                if matrix[row][col] == 0:
                    amount_of_zeros += 1
                    if amount_of_zeros >= 2:
                        min_val = matrix[row][col]
                else:
                    min_val = matrix[row][col]

        min_vals_from_cols.append(min_val)

    max_elem_from_rows = max(min_vals_from_rows)
    max_elem_from_cols = max(min_vals_from_cols)
    if max_elem_from_rows >= max_elem_from_cols:
        id_row = max(enumerate(min_vals_from_rows), key=lambda x: x[1])[0]
        for col in range(len(matrix[id_row])):
            if matrix[row][col] == 0:
                id_col_with_0 = col
                break
        for col in range(len(matrix[id_row])):
            matrix[id_row][col] = float("inf")
        for row in range(len(matrix[id_col_with_0])):
            matrix[row][id_col_with_0] = float("inf")

    else:
        id_col = max(enumerate(min_vals_from_cols), key=lambda x: x[1])[0]
        for row in range(len(matrix)):
            if matrix[row][col] == 0:
                id_row_with_0 = row
                break
        for row in range(len(matrix)):
            matrix[row][id_col] = float("inf")
        for col in range(len(matrix)):
            matrix[id_row_with_0][col] = float("inf")

    return matrix

matrix = [[float("inf"), 9, 0, 42, 3],
          [75, float("inf"), 87, 18, 0],
          [0, 51, float("inf"), 18, 93],
          [6, 0, 2, float("inf"), 28],
          [1, 96, 1, 0, float("inf")]]

print(zabranianie(matrix))

