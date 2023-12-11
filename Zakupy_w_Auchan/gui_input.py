import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color

def input_constants(mo_default = 0.5, c_l_default = 1, c_f_default = 0, L0_default = 500, F0_default = 100, Ad_default = 1, Afer_default = 1, Evap_default = 0.5, Fero_amount_default = 1000, Iter_default = 1000):
    #inputs: constants for algorithm, returns dict with given constants or default values
    
    layout = [  [sg.Text('Enter constants: ')],
                [sg.Text(f'Mass of empty basket [kg] :'), sg.Input(default_text=mo_default, key="m0")],
                [sg.Text(f'Destination function distance constant:'), sg.Input(default_text=c_l_default, key="c_l")],
                [sg.Text(f'Destination function fatigue constant:'), sg.Input(default_text=c_f_default, key="c_f")],
                [sg.Text(f'Distance constant:'), sg.Input(default_text=Ad_default, key="Ad")],
                [sg.Text(f'DFeromone constant:'), sg.Input(default_text=Afer_default, key="Afer")],
                [sg.Text(f'Feromone evaporation constant:'), sg.Input(default_text=Evap_default, key="Evap")],
                [sg.Text(f'Feromon amount:'), sg.Input(default_text=Fero_amount_default, key="Fero_amount")],
                [sg.Text(f'Distance to shop:'),  sg.Input(default_text=L0_default, key="L0")],
                [sg.Text(f'Fatigue of getting to the shop:'), sg.Input(default_text=F0_default, key="F0")],
                [sg.Text(f'Iterations:'), sg.Input(default_text=Iter_default, key="Iter")],
                [sg.Button("Submit")]
                ]

    window = sg.Window("Zakupy w Auchan", layout)
    const_dict = {"m0": mo_default, "c_l": c_l_default, "c_f": c_f_default, "L0": L0_default , "F0": F0_default, "Ad" : Ad_default, "Af" : Afer_default, "Evap" : Evap_default}
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == "Submit":
            const_dict = {k: float(values[k])  for (k, v) in values.items()}
            break

    window.close()
    return const_dict


def outputs(LS, DL):
    layout = [  [sg.Text]

    ]

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


