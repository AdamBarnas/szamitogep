import typing
import numpy as np
import matplotlib.pyplot as plt
from random import random

# types
coords_t = tuple[float, float]

# constants
M0 = 0 # 0.5  # empty basket mass
C_dist = 1   # destination function distance constant
C_fat = 1   # destination function fatigue constant
A_dist = 1   # distance constant
A_fer = 1   # feromone constant
Evap = 0.5 # feromone evaporation constant
Fero_amount = 10 # feromone amount left on trail segment to be devided by destination function value
L0 = 0 # 500  # distance to the shop
F0 = 0 # 100  # fatigue of getting to the shop

entry_ID = 0
entry_coords1 = (7, 765)
entry_coords2 = (7, 38)

exit_ID = -1
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
            mass = M0
            for item in self.B:
                mass += item.mass
        self.mass = mass #mass of basket and items inside
        self.coords = coords #coordinates of a shopper
        self.x = self.coords[0] #coordinate x
        self.y = self.coords[1] #coordinate y
        self.L = L #distance walked
        self.F = F #fatigue
    
    def destination_function(self) -> float: #calculate how easy it was to do the shopping
        ret_val = self.L * C_dist + self.F * C_fat
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
    
class Ant:
    def __init__(self, item: Product) -> None:
        self.ID = item.ID
        self.visited = [item.ID] #items collected
        self.coords = item.coords
        self.dest_fun = None

    def goto_next_product(self, p: Product) -> None:
        self.visited.append(p.ID)
        if p.name == "EXIT":
            self.visited.append(entry_ID)
            self.coords = entry_coords1
        else:
            self.coords = p.coords
        return None

    def choose_next_product(self, AM: np.ndarray, FM: np.ndarray, rand: float =random()) -> int:
        last_p_id = self.visited[-1]
        sum_cost = 0.0
        cost_list = []
        for id in range(AM.shape[0]):
            if id in self.visited or id == entry_ID:
                cost_list.append(0)
            else:
                val = 1/(A_dist*AM[last_p_id, id] + A_fer*FM[last_p_id, id])
                cost_list.append(val + sum_cost)
                sum_cost += val
        rand_val = rand * sum_cost

        id = 0
        while cost_list[id] < rand_val:
            id += 1

        return id

    def arrange_visited(self) -> None:
        N = len(self.visited)
        count = 0

        while self.visited[count] != 0:
            count += 1

        arranged = []

        for i in range(count, N):
            arranged.append(self.visited[i])
        for i in range(count):
            arranged.append(self.visited[i])

        self.visited = arranged
        return None
    
    def calculate_destination_function(self, LZ: list[Product], AM: np.ndarray) -> None:
        self.arrange_visited()
        N = len(LZ)
        total_distance = 0
        total_fatigue = 0
        total_mass = 0
        for i in range(len(self.visited) - 1):
            total_mass += LZ[self.visited[i]].mass
            distance = AM[self.visited[i], self.visited[i+1]]
            total_distance += distance
            total_fatigue += calculate_fatigue(distance, total_mass)
        self.dest_fun = total_distance * C_dist + total_fatigue * C_fat
        return None

    def leave_feromone_trail(self, FM: np.ndarray) -> None:
        for i in range(len(self.visited) - 1):
            FM[self.visited[i], self.visited[i+1]] += Fero_amount / self.dest_fun
    

                
        
    def __str__(self) -> str:
        return "Ant: " + str(self.ID) + "\nVisited: " + str(self.visited) + "\nPosition: " + str(self.coords)

def create_ant_list(LZ: list[Product]) -> list[Ant]:
    AL = []
    for product in LZ:
        if product.ID == exit_ID:
            pass
        else:
            AL.append(Ant(product))
    return AL

def calculate_distance(p1: Product, p2: Product) -> float:
    if p2.name == "EXIT" and p1.coords[1] < 55:
        coords1 = p1.coords
        coords2 = exit_coords1
    elif p2.name == "EXIT" and p1.coords[1] > 610:
        coords1 = p1.coords
        coords2 = exit_coords2
    elif p2.name == "EXIT":
        coords1 = p1.coords
        coords2 = (exit_coords1[0], p1.coords[1])
    else:
        coords1 = p1.coords
        coords2 = p2.coords
    distance = 0
    for i in range(2):
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
    AM = np.zeros([N,N])
    
    for i in range(N):
        for j in range(i, N):
            if i != j:
                dist = calculate_distance(LZ[i], LZ[j])
                AM[i, j] = dist
                AM[j, i] = dist
            else:
                AM[i, j] = 0

    return np.array(AM)

def create_feromone_matrix(LZ: list[Product]):
    N = len(LZ)
    FM = np.ones([N,N])
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
    return None
