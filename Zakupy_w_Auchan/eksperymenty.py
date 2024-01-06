import numpy as np
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
GUI_ON = 0
PARSE_ON = 0
PLOT_ON = 0

os.remove("Zakupy_w_Auchan/tests/number_of_call.txt")
f = open("Zakupy_w_Auchan/tests/number_of_call.txt", "w")
f.write("0")
f.close()

def experiment(folder, number) -> None:

    db = Database()
    
    shop_entry = sd.Product(sd.entry_ID, sd.M0, sd.entry_coords1, "Entry")
    shop_exit = sd.Product(sd.exit_ID, 0, sd.exit_coords1, "Exit")

    CD = {key:float(value) for (key,value) in const_dict.items()}
    fp = open("shared.pkl", "w")
    LZ = [sd.shop_entry]
    for i in range(int(CD["nr_of_item"])):                          # prarametr ilości produktów
        LZ.append(db.get_productinfo(i+1))
    LZ.append(sd.shop_exit)
    best_sol, best_ant_arr, best_ant_in_iter_arr, FM, iter, text = sd.ant_algorithm(LZ, CD, folder)
    fig = plot_DestFunc_FM_Map_Summary(best_ant_arr, best_ant_in_iter_arr, FM, LZ, best_sol, text, animation=0, show = 0, safe_path="Zakupy_w_Auchan/" + folder + "/pictures" + number)
    if PARSE_ON == 1:
        base_path = os.path.abspath(os.path.dirname(__file__))
        filename_parse = os.path.join(base_path, 'tests', 'file6.txt')
        a = sd.parse(filename_parse)
        print(a[2]['best_ant_dest_fun'])
    return None


for i in range(10):
     experiment("experiments/method_4_best", str(i))

# import csv

# #eksperyment czyli zmieniamy 1 parametr
# #1. Dla 

# ##### STAŁE #####
# file1 = 'Zakupy_w_Auchan/dane_do_eksp.csv'

# ##### FUNKJE #####
# def form_csv_to_dict(file):
#     with open(file) as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=",")
#         dict_arr= []
#         data = list(csv_reader)
#         col_names = data[0]
#         data = data[1:]
#         for line in data:
#             dict_tmp = dict(map(lambda i,j : (i,j), col_names, line))
#             dict_arr.append(dict_tmp)
#             print(f'Dict:\n {dict_tmp}')



# form_csv_to_dict(file1)