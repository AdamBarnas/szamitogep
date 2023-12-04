import matplotlib.pyplot as plt
from struktury_danych import Product

def show_points(LZ: list[Product]) -> None:
    x_coords = []
    y_coords = []
    for product in LZ:
        x_coords.append(product.coords[0])
        y_coords.append(product.coords[1])
    img = plt.imread("Zakupy_w_Auchan\wymiary.png")
    plt.scatter(x_coords, y_coords)
    plt.imshow(img)
    plt.show()
    return None