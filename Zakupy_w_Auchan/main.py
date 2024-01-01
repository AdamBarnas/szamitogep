import numpy as np
from baza import Database
import struktury_danych as sd
from gui_output import show_points
from gui_input import input_constants
import matplotlib.pyplot as plt
from random import random
import random as r

# r.seed(19216812)

np.set_printoptions(precision=0, floatmode="maxprec")



def main() -> None:
    db = Database()

    shop_entry = sd.Product(sd.entry_ID, sd.M0, sd.entry_coords1, "Makaron pełnoziarnisty świdry")
    shop_exit = sd.Product(sd.exit_ID, 0, sd.exit_coords1, "Majonez Winiary")

    LZ = [sd.shop_entry]
    for i in range(15):
        LZ.append(db.get_productinfo(i+1))
    LZ.append(sd.shop_exit)
    # for product in LZ:
    #     print(product)

    # AM = sd.calculate_adjacency_matrix(LZ)
    # print(AM)

    best_sol = sd.ant_algorithm(LZ)

    a = sd.parse('file.txt')
    print(a[0]['best_ant']['dest_fun'])
    # print(a[0]['ants'][9]['visited'])
    # for b in a:
    #     print(b)

    # show_points(LZ, best_sol)
    return None

main()