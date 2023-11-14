import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color

def input_constants(mo_default = 0.5, c_l_default = 1, c_f_default = 1, L0_default = 500, F0_default = 100):
    #inputs: constants for algorithm, returns dict with given constants or default values
    
    layout = [  [sg.Text('Enter constants: ')],
                [sg.Text(f'Mass of empty basket [kg] :'), sg.Input(default_text=mo_default, key="m0")],
                [sg.Text(f'Destination function distance constant:'), sg.Input(default_text=c_l_default, key="c_l")],
                [sg.Text(f'Destination function fatigue constant:'), sg.Input(default_text=c_f_default, key="c_f")],
                [sg.Text(f'Distance to shop:'),  sg.Input(default_text=L0_default, key="L0")],
                [sg.Text(f'Fatigue of getting to the shop:'), sg.Input(default_text=F0_default, key="F0")],
                [sg.Button("Submit")]
                ]

    window = sg.Window("Zakupy w Auchan", layout)
    m0, c_l, c_f, L0, F0 = mo_default, c_l_default, c_f_default, L0_default ,F0_default
    const_dict = {"m0": mo_default, "c_l": c_l_default, "c_f": c_f_default, "L0": L0_default , "F0": F0_default}
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == "Submit":
            const_dict = {k: float(values[k])  for (k, v) in values.items()}
            

    window.close()
    return const_dict


def outputs(LS, DL):
    layout = [  [sg.Text]

    ]

# TEST: You can call the function with your default value
cd = input_constants()
# print(cd)

