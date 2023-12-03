import typing
import numpy as np
import matplotlib.pyplot as plt

#types
coords_t = tuple[float, float]

#constans
m0 = 0.5  #empty basket mass
c_l = 1   #destination function distance constant
c_f = 1   #destination function fatigue constant
L0 = 500  #distance to the shop
F0 = 100  #fatigue of getting to the shop
entry_coords1 = (7, 765)
entry_coords2 = (7, 38)

exit_coords1 = (7, 55)
exit_coords2 = (7, 610)

# #shopping list
# LZ = []

# #state list
# LS = []

# #decision list
# DL = []

# #adjacency matrix
# AM = [[]]

# #feromone matrix
# FM = [[]]

class State:
    def __init__(self, B: list, mass: int, coords: coords_t, L: float, F: float) -> None:
        self.B = B #list of items in a basket
        if mass == 0:
            mass = m0
            for item in self.B:
                mass += item.mass
        self.mass = mass #mass of basket and items inside
        self.coords = coords #coordinates of a shopper
        self.x = self.coords[0] #coordinate x
        self.y = self.coords[1] #coordinate y
        self.L = L #distance walked
        self.F = F #fatigue
    
    def destination_function(self) -> float: #calculate how easy it was to do the shopping
        ret_val = self.L * c_l + self.F * c_f
        return ret_val

class Product:
    def __init__(self, ID: int, mass: float, coords: coords_t, name: str) -> None:
        self.ID = ID #product ID
        self.mass = mass #product mass
        self.coords = coords #product coordinates
        self.name = name #product name

    def __str__(self) -> str:
        napis = self.name + "\nID:" + str(self.ID) + "\nmass: " + str(self.mass) + "kg\n" + "coords: " + str(self.coords)
        return napis
    
# class Decision:
#     def __init__(self, item: Product) -> None:
#         self.ID = item.ID #selected product ID
#         self.mass = item.mass #selected product mass
#         self.coords = item.coords #selected product coordinates

class Ant:
    def __init__(self, item: Product) -> None:
        self.visited = [item] #items collected

    def choose_next_product(self, LZ) -> Product:
        pass

def calculate_distance(p1: Product, p2: Product) -> float:
    coords1 = p1.coords
    coords2 = p2.coords
    distance = 0
    for i in range(len(coords1)):
        distance += abs(coords1[i] - coords2[i])
    return distance

def calculate_fatigue(distance, mass) -> float:
    return distance * mass

def transfer_function(S: State, D: Product):
    B = S.B
    if D.ID not in B:
        B.append(D.ID)
    else:
        print("Item already in a basket")
        return None
    mass = S.mass + D.mass
    coords = D.coords
    distance = calculate_distance(S, D)
    L = S.L + distance
    F = S.F + calculate_fatigue(distance, S.mass)
    newstate = State(B, mass, coords, L, F)
    return newstate

def calculate_adjacency_matrix(LZ: list[Product]) -> list[list[float]]:
    N = len(LZ)
    AM = [[calculate_distance(LZ[i], LZ[j]) for i in range(N)] for j in range(N)]
    return np.array(AM)

def create_feromone_matrix(LZ: list[Product]):
    N = len(LZ)
    FM = np.ones(N,)
    return FM

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
    