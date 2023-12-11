import matplotlib.pyplot as plt
from struktury_danych import Product

def show_points(LZ: list[Product], best_sol) -> None:
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
    return None