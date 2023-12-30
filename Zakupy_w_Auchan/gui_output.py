import matplotlib.pyplot as plt
from struktury_danych import Product
from random import randint
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import matplotlib

matplotlib.use('TkAgg')
def show_points(LZ: list[Product], best_sol, ax) -> ([list[int], list[int]]):
    x_coords = []
    y_coords = []
    NLZ = []
    for i in best_sol:
        NLZ.append(LZ[i])
    for product in NLZ:
        x_coords.append(product.coords[0])
        y_coords.append(product.coords[1])
    ax.plot(x_coords, y_coords, linewidth=5, alpha=0.7)
    img = plt.imread("Zakupy_w_Auchan\wymiary.png")
    ax.scatter(x_coords, y_coords)
    ax.imshow(img)
    ax.set_title("Route of the best ant")
    return x_coords, y_coords

def annotate_axes(ax, text, fontsize=18):
    ax.text(0.5, 0.5, text, transform=ax.transAxes,
            ha="center", va="center", fontsize=fontsize, color="darkgrey")
    
def plot_DestFunc_FM_Map_Summary(best_ant_arr, FM, LZ, best_sol, text, animation = 0):
    fig, axd = plt.subplot_mosaic([['upper left', 'upper left', 'right'],
                               ['lower left1', 'lower left2', 'right']],
                              figsize=(12, 6), layout="constrained")
    plot_dest_func(best_ant_arr, axd["upper left"])
    plot_FM(FM, axd["lower left2"])
    plot_summary_text(text, axd['lower left1'])
    show_points(LZ, best_sol, axd["right"])
    if (animation == 1):
        animate_best_ants(LZ, best_ant_arr, axd["right"], 50)
    fig.suptitle('Summary')
    #plt.show()
    return fig

# def animate(i):
#     pt = randint(1,9) # grab a random integer to be the next y-value in the animation
#     x.append(i)
#     y.append(pt)

#     ax.clear()
#     ax.plot(x, y)
#     ax.set_xlim([0,20])
#     ax.set_ylim([0,10])
    

def plot_dest_func(best_ant_arr, ax):
    dest_func_arr = []
    idx_arr = []
    for idx, ant in enumerate(best_ant_arr):
        dest_func_arr.append(ant.dest_fun)
        idx_arr.append(idx)
    ax.plot(idx_arr, dest_func_arr)
    ax.set_title("Desination function in each iterartion")
    ax.grid()
    return None


def plot_FM(FM,ax):
    ax.imshow(FM)
    ax.set_title("Feromone Matrix")
    return None


def plot_summary_text(text, ax):
    ax.text(0,1, text,
                ha='left', va='top', size=8,
                bbox=dict(facecolor='none', edgecolor='black', pad=5.0))
    ax.axis("off")
    return None


def show_best_ants(LZ, AL):
    AL = AL[0:]
    a = 0.0
    a_incr = 0.1
    img = plt.imread("Zakupy_w_Auchan\wymiary.png")
    for ant in AL:
        x_coords = []
        y_coords = []
        NLZ = []
        for i in ant.visited:
            NLZ.append(LZ[i])
        for product in NLZ:
            x_coords.append(product.coords[0])
            y_coords.append(product.coords[1])
        if (a >= (1 - a_incr)):
            a = 1
        else:
            a = a + a_incr
            plt.plot(x_coords, y_coords, "b", alpha = a)
    plt.scatter(x_coords, y_coords)
    plt.imshow(img)
    plt.plot(x_coords, y_coords, "k-")
    return None


def get_ant_route(ant, LZ):
    x_coords = []
    y_coords = []
    NLZ = []
    for i in ant.visited:
        NLZ.append(LZ[i])
    for product in NLZ:
            x_coords.append(product.coords[0])
            y_coords.append(product.coords[1])
    return x_coords, y_coords

#delat: if delta == 10 every 10. iteration will be animated on plot
def animate_best_ants(LZ, best_ant_arr, ax, delta = 1):
    alpha = 1/len(LZ)
    for idx, ant in enumerate(best_ant_arr):
        if (idx % delta == 0):
            x_coords, y_coords = get_ant_route(ant, LZ)
            ax.plot(x_coords, y_coords, "k", alpha = alpha)
            plt.pause(0.25)
    plt.show()
    return None

##### integration woith pysimplegui #####
def draw_figure(canvas, figure):
   figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
   figure_canvas_agg.draw()
   figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
   return figure_canvas_agg


layout_output = [[sg.Text('Plot test')],
   [sg.Canvas(key='-CANVAS-')],
   [sg.Button('Ok')]]