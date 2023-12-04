import numpy as np
from baza import Database
import struktury_danych as sd
from gui_output import show_points

def ant_algorithm(LZ: list[sd.Product]) -> list[sd.Ant]:
    N = len(LZ)
    AM = sd.calculate_adjacency_matrix(LZ)
    FM = sd.create_feromone_matrix(LZ)
    AL = sd.create_ant_list(LZ)

    for iter in range(N-1): # number of passes to do single pass through whole shop

        for ant in AL: # all ants move once
            ID = ant.choose_next_product
            ant.goto_next_product(LZ[ID])
    

    return AL

def main() -> None:
    db = Database()

    shop_entry = sd.Product(0, sd.M0, sd.entry_coords1, "ENTER")
    shop_exit = sd.Product(-1, 0, sd.exit_coords1, "EXIT")

    LZ = [shop_entry]
    for i in range(50):
        LZ.append(db.get_productinfo(i+1))
    LZ.append(shop_exit)
    # for product in LZ:
    #     print(product)

    # AM = sd.calculate_adjacency_matrix(LZ)
    # print(AM)

    FM = sd.create_feromone_matrix(LZ)
    print(FM.shape[0])

    cost_list = np.ones([5,])
    print(cost_list/2)

    # show_points(LZ)
    return None

main()