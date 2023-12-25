import PySimpleGUI as sg

sg.theme('LightBlue2')   # Add a touch of color

def parse_inputs(file):
    default_dict = {}
    f = open(file, "r")
    for line in f:
        line = line.rstrip()
        line_sp = line.split("=")
        default_dict[line_sp[0]] = float(line_sp[1])
    return default_dict #zwróci słownik wartości z pliku


#def input_constants( GUION = 1 ,mo_default = 0.5, c_l_default = 1, c_f_default = 0, L0_default = 500, F0_default = 100, Ad_default = 1, Afer_default = 4, Evap_default = 0.5, Fero_amount_default = 1000, Iter_default = 10):
def input_constants( GUION = 1 , default_file = "Zakupy_w_Auchan/defautl_values.txt"):
    #inputs: constants for algorithm, returns dict with given constants or default values
    const_dict = parse_inputs(default_file)
    print(const_dict)
    layout = [  [sg.Text('Enter constants: ')],
                [sg.Text(f'Mass of empty basket [kg] :'), sg.Input(default_text=const_dict["mo"], key="mo")],
                [sg.Text(f'Destination function distance constant:'), sg.Input(default_text=const_dict["c_l"], key="c_l")],
                [sg.Text(f'Destination function fatigue constant:'), sg.Input(default_text=const_dict["c_f"], key="c_f")],
                [sg.Text(f'Distance constant:'), sg.Input(default_text=const_dict["Ad"], key="Ad")],
                [sg.Text(f'Feromone constant:'), sg.Input(default_text=const_dict["Afer"], key="Afer")],
                [sg.Text(f'Feromone evaporation constant:'), sg.Input(default_text=const_dict["Evap"], key="Evap")],
                [sg.Text(f'Feromon amount:'), sg.Input(default_text=const_dict["Fero_amount"], key="Fero_amount")],
                [sg.Text(f'Distance to shop:'),  sg.Input(default_text=const_dict["L0"], key="L0")],
                [sg.Text(f'Fatigue of getting to the shop:'), sg.Input(default_text=const_dict["F0"], key="F0")],
                [sg.Text(f'Iterations:'), sg.Input(default_text=const_dict["Iter"], key="Iter")],
                [sg.Text(f'Stop criterion:'),  sg.Radio('Max. iterations', 0, key = "Stop_max_it"), sg.Radio('Imrovement less then epislon', 0, key = "Stop_eps"), sg.Radio('Dest. function less then threshold', 0, key = "Stop_threshold") ],
                [sg.Text(f'Espilon:'), sg.Input(default_text=const_dict["eps"], key="eps")],
                [sg.Text(f'Threshold:'), sg.Input(default_text=const_dict["threshold"], key="threshold")],
                [sg.Button("Submit"), sg.Exit()]
                ]
    if (GUION == 1):
        window = sg.Window("Zakupy w Auchan", layout)
        
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == "Submit":
                const_dict = {k: float(values[k])  for (k, v) in values.items()}
                break

        window.close()
    return const_dict


##################################################################################


# def show_points(LZ: list[Product]) -> None:
#     x_coords = []
#     y_coords = []
#     for product in LZ:
#         x_coords.append(product.coords[0])
#         y_coords.append(product.coords[1])
#     img = plt.imread("Zakupy_w_Auchan\wymiary.png")
#     plt.scatter(x_coords, y_coords)
#     plt.imshow(img)
#     plt.show()
#     return None

# TEST: You can call the function with your default value


