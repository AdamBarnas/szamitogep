import typing
import numpy as np
import matplotlib.pyplot as plt
from random import random

# types
coords_t = tuple[float, float]

# constants
m0 = 0 # 0.5  # empty basket mass
c_dist = 1   # destination function distance constant
c_fat = 1   # destination function fatigue constant
a_dist = 1   # distance constant
a_fer = 1   # feromone constant
evoporation = 0.5 # feromone evaporation constant
feromone_amount = 10 # feromone amount left on whole trail
L0 = 0 # 500  # distance to the shop
F0 = 0 # 100  # fatigue of getting to the shop

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
        ret_val = self.L * c_dist + self.F * c_fat
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

    def goto_next_product(self, p: Product) -> None:
        self.visited.append(p.ID)
        self.coords = p.coords
        return None

    def choose_next_product(self, AM: np.ndarray, FM: np.ndarray) -> int:
        last_p_id = self.visited[-1]
        sum_cost = 0.0
        cost_list = []
        for id in range(AM.size):
            if id in self.visited:
                cost_list.append(0)
            else:
                val = 1/(a_dist*AM[last_p_id, id] + a_fer*FM[last_p_id, id])
                cost_list.append(val + sum_cost)
                sum_cost += val
        rand_val = random() * sum_cost

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
    
    def calculate_destination_function(self, LZ: list[Product]) -> float:
        self.arrange_visited()
        N = len(LZ)
        distance_walked = L0
        fatigue =  F0
        for i in range(len(self.visited) - 1):
            if self.visited[id] == N:
                #end
                pass
            else:
                pass

    def leave_feromone_trail(self, FM: np.ndarray) -> None:
        pass

                
        
    def __str__(self) -> str:
        return "Ant: " + str(self.ID) + "\nVisited: " + str(self.visited) + "\nPosition: " + str(self.coords)

def create_ant_list(LZ: list[Product]) -> list[Ant]:
    AL = []
    for product in LZ:
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
        for j in range(N):
            AM[i, j] = calculate_distance(LZ[i], LZ[j])

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
    