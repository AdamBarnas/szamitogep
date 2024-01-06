import numpy as np
import settings
from baza import Database
import struktury_danych as sd
from gui_output import show_points, show_best_ants, plot_dest_func, plot_FM, plot_DestFunc_FM_Map_Summary, animate_best_ants, layout_output, draw_figure
from gui_input import input_constants
import matplotlib.pyplot as plt
from random import random
import random as r
import PySimpleGUI as sg
from gui_v2 import *
import os

# r.seed(19216812)

np.set_printoptions(precision=0, floatmode="maxprec")
CD = const_dict
GUI_ON = 1
PARSE_ON = 1
PLOT_ON = 1

def main() -> None:

    db = Database()
    
    shop_entry = sd.Product(sd.entry_ID, sd.M0, sd.entry_coords1, "Entry")
    shop_exit = sd.Product(sd.exit_ID, 0, sd.exit_coords1, "Exit")
    if GUI_ON == 1:
        gui_v2_fnc(db=db)
    else:
            CD = {key:float(value) for (key,value) in const_dict.items()}
            fp = open("shared.pkl", "w")
            LZ = [sd.shop_entry]
            for i in range(int(CD["nr_of_item"])):                          # prarametr ilości produktów
                LZ.append(db.get_productinfo(i+1))
            LZ.append(sd.shop_exit)
            best_sol, best_ant_arr, best_ant_in_iter_arr, FM, iter, text = sd.ant_algorithm(LZ, CD)
            fig = plot_DestFunc_FM_Map_Summary(best_ant_arr, best_ant_in_iter_arr, FM, LZ, best_sol, text, animation=1, show = 1)
            if PARSE_ON == 1:
                a = sd.parse('file.txt')
                print(a[3]['best_ant']['ID'])
                print(a[3]['best_ant_in_iter']['ID'])
                print(a[0]['ants'][9]['visited'])

    # for product in LZ:
    #     print(product)

    # AM = sd.calculate_adjacency_matrix(LZ)
    # print(AM)

    #TO OSTATECZNA FUNKCJA: 
    
    #show_best_ants(LZ, best_ant_arr)

    #### show output ####
    # window = sg.Window('Matplotlib In PySimpleGUI', layout_output, size=(715, 500), finalize=True, element_justification='center', font='Helvetica 18')
    # tkcanvas = draw_figure(window['-CANVAS-'].TKCanvas, fig)
    # event, values = window.read()
    # window.close()




    # a = sd.parse('file.txt')


    # for b in a:
    #     print(b)

    # show_points(LZ, best_sol)
    return None


###################################
def gui_v2_fnc(db):

    window = sg.Window('Test window', layout, size = (480,400))
    layout_nr = 1

    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        if event == 'Next':
            print(layout_nr)
            window[f'-COL{layout_nr}-'].update(visible=False)
            if layout_nr < 4:
                layout_nr += 1
                window[f'-COL{layout_nr}-'].update(visible=True)
            else:
                window[f'-COL{layout_nr}-'].update(visible=True)
        elif event == 'Back':
            print(layout_nr)
            window[f'-COL{layout_nr}-'].update(visible=False)
            if layout_nr > 1:
                layout_nr -= 1
                window[f'-COL{layout_nr}-'].update(visible=True)
            else:
                window[f'-COL{layout_nr}-'].update(visible=True)
        elif event == 'RUN':
            CD = {key:float(value) for (key,value) in values.items()}
            fp = open("shared.pkl", "w")
            LZ = [sd.shop_entry]
            for i in range(int(CD["nr_of_item"])):                          # prarametr ilości produktów
                LZ.append(db.get_productinfo(i+1))
            LZ.append(sd.shop_exit)
            best_sol, best_ant_arr, best_ant_in_iter_arr, FM, iter, text = sd.ant_algorithm(LZ, CD)
            fig = plot_DestFunc_FM_Map_Summary(best_ant_arr, best_ant_in_iter_arr, FM, LZ, best_sol, text, animation=1, show = 1, safe_path="pictures1")
            
            if PARSE_ON == 1:
                base_path = os.path.abspath(os.path.dirname(__file__))
                filename_parse = os.path.join(base_path, 'tests', 'file6.txt')
                a = sd.parse(filename_parse)
                print(a[2]['best_ant_dest_fun'])
                window.close()
    return None
###################################

main()