import matplotlib.pyplot as plt
from struktury_danych import Product
from random import randint
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import matplotlib
import numpy as np

np.set_printoptions(precision=0, floatmode="maxprec")


matplotlib.use('TkAgg')
def show_points(LZ: list[Product], best_sol, ax, safe_path = None) -> ([list[int], list[int]]):
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
    
def plot_DestFunc_FM_Map_Summary(best_ant_arr, best_ant_in_iter_arr, FM, LZ, best_sol, text, animation = 0, show = 0, safe_path = None):
    fig, axd = plt.subplot_mosaic([['upper left', 'upper left', 'right'],
                                   ['upper left2', 'upper left2', 'right'],
                               ['lower left1', 'lower left2', 'right']],
                              figsize=(12, 6), layout="constrained")
    plot_dest_func(best_ant_arr, axd["upper left"], "ant_dest123.png")
    plot_dest_func_iter(best_ant_in_iter_arr, axd["upper left2"] )
    plot_FM(FM, axd["lower left2"])
    plot_summary_text(text, axd['lower left1'])
    show_points(LZ, best_sol, axd["right"])
    if (animation == 1):
        animate_best_ants(LZ, best_ant_arr, axd["right"], 50)
    fig.suptitle('Summary')
    if safe_path != None:
        if isinstance(safe_path, str):
            fig.savefig(safe_path + r"_fig_all.png")
            ex_ul = axd["upper left"].get_window_extent().transformed(fig.dpi_scale_trans.inverted())
            fig.savefig(safe_path + r"_fig_dest_fnc.png" , bbox_inches=ex_ul.expanded(1.1, 1.5))
            ex_ul2 = axd["upper left2"].get_window_extent().transformed(fig.dpi_scale_trans.inverted())
            fig.savefig(safe_path + r"_fig_dest_fnc_iter.png" , bbox_inches=ex_ul2.expanded(1.1, 1.5))
            ex_r = axd["right"].get_window_extent().transformed(fig.dpi_scale_trans.inverted())
            fig.savefig(safe_path + r"_fig_best_route.png" , bbox_inches=ex_r.expanded(1.4, 1.3))
            ex_lr2 = axd["lower left2"].get_window_extent().transformed(fig.dpi_scale_trans.inverted())
            fig.savefig(safe_path + r"_fig_last_FM.png" , bbox_inches=ex_lr2.expanded(3.0, 1.5))


        else:
            print("FILE PATH NOT A STRING")
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
    

def plot_dest_func(best_ant_arr, ax, safe_path = None):
    dest_func_arr = []
    idx_arr = []
    for idx, ant in enumerate(best_ant_arr):
        dest_func_arr.append(ant.dest_fun)
        idx_arr.append(idx)
    ax.plot(idx_arr, dest_func_arr)
    ax.set_title("Desination function (Best so far)")
    ax.grid()
    return None


def plot_dest_func_iter(best_ant_in_iter_arr, ax, safe_path = None):
    dest_func_arr = []
    idx_arr = []
    for idx, ant in enumerate(best_ant_in_iter_arr):
        dest_func_arr.append(ant.dest_fun)
        idx_arr.append(idx)
    ax.plot(idx_arr, dest_func_arr)
    ax.set_title("Desination function (Best in iteration)")
    ax.grid()
    return None


def plot_FM(FM,ax, safe_path = None):
    ax.imshow(FM)
    ax.set_title("Feromone Matrix (last iteration)")

    return None


def plot_summary_text(text, ax, safe_path = None):
    ax.text(0,1, text,
                ha='left', va='top', size=8,
                bbox=dict(facecolor='none', edgecolor='black', pad=5.0))
    ax.axis("off")
    return None


def show_best_ants(LZ, AL, safe_path = None):
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
    if safe_path != None:
        if isinstance(safe_path, str):
            plt.savefig(f"{safe_path}")
        else:
            print("FILE PATH NOT A STRING")
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
    #plt.show()
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