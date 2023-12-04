import numpy as np
from baza import Database
import struktury_danych as sd

def ant_algorithm(LZ: list[sd.Product]) -> list[sd.Ant]:
    N = len(LZ)
    AM = sd.calculate_adjacency_matrix(LZ)
    FM = sd.create_feromone_matrix(LZ)
    AL = sd.create_ant_list(LZ)

    for ant in AL: #single iteration over all ants
        pass

    return AL

def main() -> None:
    db = Database()

    shop_entry = sd.Product(0, sd.m0, sd.entry_coords1, "ENTER")
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

    # sd.show_points(LZ)
    return None

main()