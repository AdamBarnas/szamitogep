import PySimpleGUI as sg

sg.theme('LightBlue2')   # Add a touch of color

######constants######
timeout_c = 1000
#####################

def parse_inputs(file):
    default_dict = {}
    f = open(file, "r")
    for line in f:
        line = line.rstrip()
        line_sp = line.split("=")
        default_dict[line_sp[0]] = float(line_sp[1])
    return default_dict #zwróci słownik wartości z pliku


def input_constants( GUION = 1 , default_file = "Zakupy_w_Auchan/defautl_values.txt"):
    #inputs: constants for algorithm, returns dict with given constants or default values
    const_dict = parse_inputs(default_file)
    print(const_dict)
    layout = [  
                [sg.Text('Enter constants an options: '),],#, sg.Image("Zakupy_w_Auchan/ant_photo.jpg", key="ant_photo")],
                [sg.Text(f'Mass of empty basket [kg] :'), sg.Input(default_text=const_dict["mo"], key="mo", s=(10,10))],
                [sg.Text(f'Destination function distance constant:'), sg.Input(default_text=const_dict["c_l"], key="c_l", s=(10,10))],
                [sg.Text(f'Destination function fatigue constant:'), sg.Input(default_text=const_dict["c_f"], key="c_f",s=(10,10))],
                [sg.Text(f'Distance constant:'), sg.Input(default_text=const_dict["Ad"], key="Ad", s=(10,10))],
                [sg.Text(f'Feromone constant:'), sg.Input(default_text=const_dict["Afer"], key="Afer", s=(10,10)),\
                sg.Text(f'Feromone evaporation constant:'), sg.Input(default_text=const_dict["Evap"], key="Evap", s=(10,10)),\
                sg.Text(f'Feromon amount:'), sg.Input(default_text=const_dict["Fero_amount"], key="Fero_amount", s=(10,10))],
                [sg.Text(f'Distance to shop:'),  sg.Input(default_text=const_dict["L0"], key="L0", s=(10,10))],
                [sg.Text(f'Fatigue of getting to the shop:'), sg.Input(default_text=const_dict["F0"], key="F0", s=(10,10))],
                [sg.Text(f'Stop criterion:'),  sg.Radio('Max. iterations', 0, key = "Stop_max_it", default=1), sg.Radio('Imrovement less then epislon', 0, key = "Stop_eps"), sg.Radio('Dest. function less then threshold', 0, key = "Stop_threshold") ],
                [sg.Text(f'Parameters for stop criteria:')],
                [sg.Text(f'Iterations:'), sg.Input(default_text=const_dict["Iter"], key="Iter", s=(10,10)),\
                sg.Text(f'Espilon:'), sg.Input(default_text=const_dict["eps"], key="eps", s=(10,10)),\
                sg.Text(f'Threshold:'), sg.Input(default_text=const_dict["threshold"], key="threshold", s=(10,10))],
                [sg.Text(f'Choosing next product:'),  sg.Radio('Version 1', 1, key = "next_prod_1", default=1), sg.Radio('Version 2 (Dorigo)', 1, key = "next_prod_dorigo"), sg.Radio('Version 3 (Mass)', 1, key = "next_prod_mass"), sg.Radio('Version 4 (Dorigo, Mass incl.)', 1, key = "next_prod_dorigo_mass")],
                [sg.Text(f'Parameters for Dorigo implementation: ')],
                [sg.Text(f'a: '),sg.Input(default_text=const_dict["a_derigo"], key="a_derigo", s=(10,10)), sg.Text(f'b: '), sg.Input(default_text=const_dict["b_derigo"], key="b_derigo", s=(10,10))],
                [sg.Text(f'Leaving feromones:'),  sg.Radio('Ant quantity', 2, key = "fero_ant_quantity", default=1), sg.Radio('Ant density', 2, key = "fero_ant_density")],
                [sg.Text(f'MMAS Implementation:'), sg.Radio('YES',3, key="MMAS_ver", default=0)],
                [sg.Button("Submit"), sg.Exit()]
                ]
    if (GUION == 1):
        window = sg.Window("Zakupy w Auchan", layout)
        
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == "Exit":
                break
            elif event == "Submit":
                const_dict = {k: float(values[k])  for (k, v) in values.items()}
                break

        window.close()
    return const_dict

