def wykreslanie(G):
    G_size = len(G)
    idx_of_max = lambda list: list.index(max(list))

    zeros_in_rows = [0 for i in range(G_size)]
    zeros_in_cols = [0 for i in range(G_size)]
    crossed_rows = []
    crossed_cols = []
    zeros_list = []
    for i, row in enumerate(G):
        for j, elem in enumerate(row):
            if elem == 0:
                zeros_list.append((i,j))

    for zero in zeros_list:
        zeros_in_rows[zero[0]] += 1
        zeros_in_cols[zero[1]] += 1

    while(not (all(v == 0 for v in zeros_in_cols) & all(v == 0 for v in zeros_in_rows))):
        row_with_max_zeros = idx_of_max(zeros_in_rows)
        crossed_rows.append(row_with_max_zeros)
        zeros_in_rows[row_with_max_zeros] = 0

        for zero in zeros_list:
            if(zero[0] == row_with_max_zeros and zeros_in_cols[zero[1]]> 0):
                zeros_in_cols[zero[1]] -= 1
        if (not (all(v == 0 for v in zeros_in_cols))):
            col_with_max_zeros =  idx_of_max(zeros_in_cols)
            crossed_cols.append(col_with_max_zeros)
            zeros_in_cols[col_with_max_zeros] = 0

            for zero in zeros_list:
                if(zero[1] == col_with_max_zeros and zeros_in_rows[zero[0]]> 0):
                    zeros_in_rows[zero[0]] -= 1

    return (crossed_rows), (crossed_cols)