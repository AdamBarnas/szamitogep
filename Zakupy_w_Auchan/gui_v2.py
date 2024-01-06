import PySimpleGUI as sg


#------- Parse default inputs from file -------------
def parse_inputs(file = "Zakupy_w_Auchan/defautl_values.txt" ):
    default_dict = {}
    f = open(file, "r")
    for line in f:
        line = line.rstrip()
        line_sp = line.split("=")
        try:
            default_dict[line_sp[0]] = int(line_sp[1])
        except:
            default_dict[line_sp[0]] = float(line_sp[1])
    return default_dict #zwróci słownik wartości z pliku

const_dict = parse_inputs("Zakupy_w_Auchan/defautl_values.txt")

#-------- Layouts -----------

layout_general_settings = [[sg.Text('General Settings (1/4)')],
                           [sg.Text('Number of product on list: '), sg.Input(key='nr_of_item', default_text=const_dict['nr_of_item'])],
                           [sg.Text('Mass of empty basket: '), sg.Input(key='M0', default_text=const_dict['M0'])],
                           [sg.Text('Destination function distance constant: '), sg.Input(key='c_l', default_text=const_dict['c_l'])],
                           [sg.Text('Destination function fatigue constant: '), sg.Input(key='c_f',default_text=const_dict['c_f'])],
                           [sg.Text('Distance to shop: '), sg.Input(key='L0', default_text=const_dict['L0'])],
                           [sg.Text('Fatigue of getting to shop: '), sg.Input(key='F0',default_text=const_dict['F0'])],
                           [sg.Radio(text='Max-Min Ant System ', group_id=0,key="MMAS_ver", default=const_dict['MMAS_ver'])]]

layout_feromones = [[sg.Text('Feromones settings (2/4)')],
                    [sg.Radio(text = 'All ants leave feromones', group_id=1,key='all_leave_fero',default=const_dict['all_leave_fero'])],
                    [sg.Radio(text = 'Best ant in iter. ants leaves feromones', group_id=1,key='best_in_iter_leave_fero',default=const_dict['best_in_iter_leave_fero'])],
                    [sg.Text('Feromone evaporation constant (between 0 and 1): '), sg.Input(key='Evap', default_text=const_dict['Evap'])],
                    [sg.Text('Amount of feromones left by ant: '), sg.Input(key='Fero_amount', default_text=const_dict['Fero_amount'])],
                    [sg.Text('Way of leaving feromones: ')],
                    [sg.Radio(text = 'Quantity: ', group_id=2,key='fero_ant_quantity',default=const_dict['fero_ant_quantity'])],
                    [sg.Radio(text = 'Density: ', group_id=2,key='fero_ant_density',default=const_dict['fero_ant_density'])]]

layout_stop_criterion = [[sg.Text('Stop criteion settings (3/4) ')],
                         [sg.Text('Max. iterations (obligatory): '), sg.Input(key="Iter", default_text=const_dict["Iter"])],
                         [sg.Radio(text='Stop after max. iterations', group_id=3, key = 'Stop_max_it', default=const_dict['Stop_max_it'])],
                         [sg.Radio(text='Stop when improvement less then epsilon for N iter.', group_id=3, key = 'Stop_eps', default=const_dict['Stop_eps'])],
                         [sg.Text("N: "), sg.Input(key = "N", default_text=const_dict['N']), sg.Text("Eps: "), sg.Input(key = "eps", default_text=const_dict['eps'])],
                         [sg.Radio(text='Stop when dest. fund. less then threshold', group_id=3, key = 'Stop_threshold', default=const_dict['Stop_threshold']), sg.Text("Threshold: "), sg.Input(key = "threshold", default_text=const_dict["threshold"])]]


layout_v1_v3 = [[sg.Radio(text="Version 1", key='next_prod_1', default=const_dict['next_prod_1'], group_id=4)],
                [sg.Radio(text="Version 3 (incl. mass)", key='next_prod_3',default=const_dict['next_prod_3'], group_id=4)],
                [sg.Text('Feromone constant: '), sg.Input(key='A_fer', default_text=const_dict['A_fer'])],
                [sg.Text('Distance constant: '), sg.Input(key='A_dist', default_text=const_dict['A_dist'])],
                [sg.Radio(text="Version 2 (Dorigo)", key='next_prod_2',default=const_dict['next_prod_2'], group_id=4)],
                [sg.Radio(text="Version 3 (Dorigo, incl. mass)", key='next_prod_4',default=const_dict['next_prod_4'], group_id=4)],
                [sg.Text('Beta: '), sg.Input(key='beta', default_text=const_dict['beta'])],
                [sg.Text('Alpha: '), sg.Input(key='alpha', default_text=const_dict['alpha'])]]

# layout_v2_v4 = [[sg.Radio(text="Version 2 (Dorigo)", key='next_prod_2',default=const_dict['next_prod_2'], group_id=4)],
#                 [sg.Radio(text="Version 3 (Dorigo, incl. mass)", key='next_prod_4',default=const_dict['next_prod_4'], group_id=4)],
#                 [sg.Text('Beta: '), sg.Input(key='beta', default_text=const_dict['beta'])],
#                 [sg.Text('Alpha: '), sg.Input(key='alpha', default_text=const_dict['alpha'])]]


layout_calculate =[[sg.Button('RUN', font=('Helvetica', 16))]]

layout_choosing_next_prod = [[sg.Text('Choosing next product [Ver1 or Ver2 or Ver3 or Ver4] (4/4)')],
                             [sg.Column(layout_v1_v3, key='col_v1_v3'), sg.VerticalSeparator(pad=None)], \
                              [sg.Column(layout_calculate, key='calculate', vertical_alignment='right', justification='right')]]

layout_bottom = [[sg.Button('Back'), sg.Button('Next'), sg.Button('Exit')]]
#-----------Main layout ----------
# layout = [[sg.Column(layout_general_settings, key='-COL1-'), \
#            sg.Column(layout_stop_criterion, key='-COL2-', visible=False), \
#            sg.Column(layout_feromones, key='-COL3-', visible=False), 
#            sg.Column(layout_choosing_next_prod, key='-COL4-', visible=False)],
#            [sg.Frame(layout=layout_bottom, title = " ",vertical_alignment='bottom')]]


cols = [[sg.Column(layout_general_settings, key='-COL1-'), \
           sg.Column(layout_stop_criterion, key='-COL2-', visible=False), \
           sg.Column(layout_feromones, key='-COL3-', visible=False), 
           sg.Column(layout_choosing_next_prod, key='-COL4-', visible=False)]]

layout = [[sg.Frame(layout= cols, title=" ", size=(480,320))],
           [sg.Frame(layout=layout_bottom, title = " ", vertical_alignment='bottom')]]
#--------------------------------
# def gui_v2(LZ):
#     global CD 
#     window = sg.Window('Test window', layout)
#     layout_nr = 1

#     while True:
#         event, values = window.read()
#         if event in (None, 'Exit'):
#             break
#         if event == 'Next':
#             print(layout_nr)
#             window[f'-COL{layout_nr}-'].update(visible=False)
#             if layout_nr < 4:
#                 layout_nr += 1
#                 window[f'-COL{layout_nr}-'].update(visible=True)
#             else:
#                 window[f'-COL{layout_nr}-'].update(visible=True)
#         elif event == 'Back':
#             print(layout_nr)
#             window[f'-COL{layout_nr}-'].update(visible=False)
#             if layout_nr > 1:
#                 layout_nr -= 1
#                 window[f'-COL{layout_nr}-'].update(visible=True)
#             else:
#                 window[f'-COL{layout_nr}-'].update(visible=True)
#         elif event == 'RUN':
#             print("RUUUUUUUUUUUUN")
#             CD = values
#             best_sol, best_ant_arr, best_ant_in_iter_arr, FM, iter, text = sd.ant_algorithm(LZ)

#     window.close()
#     return None
  
  #----------------------------------------



