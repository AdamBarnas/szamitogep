import numpy as np
from baza import Database
import struktury_danych as sd
from gui_output import show_points
from random import random

np.set_printoptions(precision=0, floatmode="maxprec")

def ant_algorithm(LZ: list[sd.Product], I: int) -> list[sd.Ant]:
    N = len(LZ)
    AM = sd.calculate_adjacency_matrix(LZ)
    FM = sd.create_feromone_matrix(LZ)
    best_sol = float("inf")
    best_ant = None
    i = 0
    while i < I:
        AL = sd.create_ant_list(LZ)
        for iter in range(N-1): # number of passes to do single pass through whole shop

            for ant in AL: # all ants move once
                id = ant.choose_next_product(AM, FM, random())
                if id != None:
                    ant.goto_next_product(LZ[id])
                else:
                    break
        
        FM = FM * sd.Evap
        
        for ant in AL:
            ant.calculate_destination_function(LZ, AM)
            # print(ant.ID, ": ", ant.dest_fun)
            if ant.dest_fun < best_sol:
                best_sol = ant.dest_fun
                best_ant = ant
            ant.leave_feromone_trail(FM)
        
        i += 1
    

    print("best\n", best_sol) 
    print("Ant: ", best_ant.ID, "   ", best_ant.visited) 
    # print("AM:\n", AM)  
    # print("FM:\n", FM)
    return AL

def main() -> None:
    db = Database()

    # shop_entry = sd.Product(sd.entry_ID, sd.M0, sd.entry_coords1, entry_name)
    # shop_exit = sd.Product(sd.exit_ID, 0, sd.exit_coords1, exit_name)

    LZ = [sd.shop_entry]
    for i in range(15):
        LZ.append(db.get_productinfo(i+1))
    LZ.append(sd.shop_exit)
    # for product in LZ:
    #     print(product)

    # AM = sd.calculate_adjacency_matrix(LZ)
    # print(AM)

    AL = ant_algorithm(LZ, 500)


    show_points(LZ)
    return None

main()