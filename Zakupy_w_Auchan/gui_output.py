import matplotlib.pyplot as plt
from struktury_danych import Product
from random import randint
from matplotlib.animation import FuncAnimation

def show_points(LZ: list[Product], best_sol) -> ([list[int], list[int]]):
    x_coords = []
    y_coords = []
    NLZ = []
    for i in best_sol:
        NLZ.append(LZ[i])
    for product in NLZ:
        x_coords.append(product.coords[0])
        y_coords.append(product.coords[1])
    plt.plot(x_coords, y_coords)
    img = plt.imread("Zakupy_w_Auchan\wymiary.png")
    plt.scatter(x_coords, y_coords)
    plt.imshow(img)
    plt.show()
    return x_coords, y_coords

def show_graphs():
    fig, axs = plt.subplots(ncols=2, nrows=2, figsize=(5.5, 3.5),
                        layout="constrained")
    # add an artist, in this case a nice label in the middle...
    # for row in range(2):
    #     for col in range(2):
    #         axs[row, col].annotate(f'axs[{row}, {col}]', (0.5, 0.5),
    #                             transform=axs[row, col].transAxes,
    #                             ha='center', va='center', fontsize=18,
    #                             color='darkgrey')
    # fig.suptitle('plt.subplots()')
    plt.show()

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
    plt.show()
    return None



x = []
y = []

# create the figure and axes objects
fig, ax = plt.subplots()

# def animate(i):
#     pt = randint(1,9) # grab a random integer to be the next y-value in the animation
#     x.append(i)
#     y.append(pt)

#     ax.clear()
#     ax.plot(x, y)
#     ax.set_xlim([0,20])
#     ax.set_ylim([0,10])
    
def ani_plot(LZ, best_ant_arr):
    ani = FuncAnimation(fig, show_best_ants(LZ, best_ant_arr), frames=60, interval=100, repeat=False)

    plt.show()
    
    return None
