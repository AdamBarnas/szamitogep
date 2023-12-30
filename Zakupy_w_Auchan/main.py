import numpy as np
from baza import Database
import struktury_danych as sd
from gui_output import show_points, show_best_ants, plot_dest_func, plot_FM, plot_DestFunc_FM_Map_Summary, animate_best_ants, layout_output, draw_figure
from gui_input import input_constants
import matplotlib.pyplot as plt
from random import random
import random as r
import PySimpleGUI as sg


# r.seed(19216812)

# np.set_printoptions(precision=0, floatmode="maxprec")


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

    best_sol, best_ant_arr, FM, iter, text = sd.ant_algorithm(LZ)
    #TO OSTATECZNA FUNKCJA: 
    fig = plot_DestFunc_FM_Map_Summary(best_ant_arr, FM, LZ, best_sol, text, animation=1)
    #show_best_ants(LZ, best_ant_arr)

    #### show output ####
    window = sg.Window('Matplotlib In PySimpleGUI', layout_output, size=(715, 500), finalize=True, element_justification='center', font='Helvetica 18')
    tkcanvas = draw_figure(window['-CANVAS-'].TKCanvas, fig)
    event, values = window.read()
    window.close()

    return None

main()