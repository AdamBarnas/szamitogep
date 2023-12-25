import typing
import numpy as np
import matplotlib.pyplot as plt
from random import random
from gui_input import input_constants
import time
#################################################
###  TYPES  ###
#################################################

coords_t = tuple[float, float]

#################################################
###  CONSTANTS  ###
#################################################

#M0 = 0 # 0.5  # empty basket mass
CD = input_constants()
print(CD)
M0 = CD["mo"]
C_dist = CD["c_l"]   # destination function distance constant
C_fat = CD["c_f"]  # destination function fatigue constant
A_dist = CD["Ad"]   # distance constant
A_fer = CD["Afer"]   # feromone constant
Evap = CD["Evap"] #0.8 # feromone evaporation constant
Fero_amount = CD["Fero_amount"] #10000000 # feromone amount left on trail segment to be devided by destination function value
L0 = CD["L0"] # 500  # distance to the shop
F0 = CD["F0"] # 100  # fatigue of getting to the shop
Iter = CD["Iter"] #1000 #number of iterations
eps = CD["eps"]
threshold = CD["threshold"]


entry_ID = 0
entry_coords1 = (7, 765)
entry_coords2 = (7, 38)
entry_name = "ENTER"

exit_ID = -1
exit_coords1 = (7, 55)
exit_coords2 = (7, 610)
exit_name = "EXIT"

cartesian = "c"
pitagorean = "p"

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

#################################################
###  CLASSES  ###
#################################################

class Product:
    def __init__(self, ID: int, mass: float, coords: coords_t, name: str) -> None:
        self.ID = ID #product ID
        self.mass = 1 #product mass
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
        if p.name == exit_name:
            if entry_ID not in self.visited:
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
            if id in self.visited or id == entry_ID or (id == AM.shape[0] - 1 and -1 in self.visited) or (id == AM.shape[0] - 1 and self.visited[0] == 0 and len(self.visited) < AM.shape[0] -1):
                cost_list.append(-1)
            else:
                val = (1 + A_fer*FM[last_p_id, id])/(A_dist*AM[last_p_id, id])
                cost_list.append(val + sum_cost)
                sum_cost += val
        rand_val = rand * sum_cost

        if sum_cost == 0:
            return None
        
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

#################################################
###  FUNCTIONS  ###
#################################################

def create_ant_list(LZ: list[Product]) -> list[Ant]:
    AL = []
    for product in LZ:
        if product.ID == exit_ID:
            pass
        else:
            AL.append(Ant(product))
    return AL

def calculate_distance(p1: Product, p2: Product, method: str =pitagorean) -> float:
    if p2.name == exit_name and p1.coords[1] < 55:
        coords1 = p1.coords
        coords2 = exit_coords1
    elif p2.name == exit_name and p1.coords[1] > 610:
        coords1 = p1.coords
        coords2 = exit_coords2
    elif p2.name == exit_name:
        coords1 = p1.coords
        coords2 = (exit_coords1[0], p1.coords[1])
    else:
        coords1 = p1.coords
        coords2 = p2.coords
    distance = 0.0
    if method == cartesian:
        for i in range(2):
            distance += abs(coords1[i] - coords2[i])
    else:
        for i in range(2):
            distance += (coords1[i] - coords2[i])*(coords1[i] - coords2[i])
        distance = np.sqrt(distance)
    return distance

def calculate_fatigue(distance, mass) -> float:
    return distance * mass

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
    FM = np.ones([N,N]) - np.eye(N)
    return FM

#################################################
###  SPECIAL OBJECTS  ###
#################################################

shop_entry = Product(entry_ID, M0, entry_coords1, entry_name)
shop_exit = Product(exit_ID, 0, exit_coords1, exit_name)

#################################################
### MAIN FUNCTION ###
#################################################

#stop = 1: stop when improvement beteen iterations is less then eps
#stop = 2: stop if destination funct. is less then treshold: df_tresh 
def ant_algorithm(LZ: list[Product]) -> list[Ant]:
    I = Iter
    N = len(LZ)
    AM = calculate_adjacency_matrix(LZ)
    FM = create_feromone_matrix(LZ)
    better_list = []
    best_sol = float("inf")
    best_iter = 0
    best_ant_arr = []
    best_ant = None
    i = 0

    flag_continue = True
    #stop condition selection, if nothing is choosen it will stop after max iter I
    df_tresh = threshold

    try:
        file = open("file.txt", "a")

    except IOError:
            print("Error: The file could not be written.")

    start_ACO = time.time()
    while(flag_continue):
        AL = create_ant_list(LZ)
        for iter in range(N-1): # number of passes to do single pass through whole shop

            for ant in AL: # all ants move once
                id = ant.choose_next_product(AM, FM, random())
                if id != None:
                    ant.goto_next_product(LZ[id])
                else:
                    break
        
        FM = FM * Evap
        
        # best_ant = AL[0]
        for ant in AL:
            ant.calculate_destination_function(LZ, AM)
            # print(ant.ID, ": ", ant.dest_fun)
            if ant.dest_fun < best_sol:
                best_sol = ant.dest_fun
                best_ant = ant
                best_iter = i
                better_list.append((i, best_sol))
            ant.leave_feromone_trail(FM)
        
        file.write("Iteration:" + str(i) + "\n")
        for ant in AL:
            file.write("ID:" + str(ant.ID))
            file.write(";visited:" + str(ant.visited))
            file.write(";coords:" + str(ant.coords)) 
            file.write(";dest_fun:" + str(ant.dest_fun))
            file.write("\n")
        
        best_ant_arr.append(best_ant)
        file.write("best_ant:\n")      
        file.write("ID:" + str(best_ant.ID))
        file.write(";visited:" + str(best_ant.visited))
        file.write(";coords:" + str(best_ant.coords)) 
        file.write(";dest_fun:" + str(best_ant.dest_fun))
        file.write("\n")

        file.write("Feromone matrix:\n")
        file.write(str(FM) + "\n")

        i += 1
        #check for stop
        if (i > I):
            flag_continue = False
            stop_crierion = "Max. iterations"
        elif ((i > 2) & bool(CD["Stop_eps"])) :
            for i_bl in range(1,len(better_list)):
                if (better_list[-1][0] != better_list[-i_bl-1][0]):
                    if (abs(better_list[-1][1]-better_list[-i_bl-1][1]) < eps):
                        flag_continue = False
                        stop_crierion = f"Improvment of dest. function by less than {eps}"
                        break
        elif( (better_list[-1][1] < df_tresh) & bool(CD["Stop_threshold"])):
            flag_continue = False
            stop_crierion = f"Dest. function below treshold: {df_tresh}"

    end_ACO = time.time()
    i = i-1
    file.close()
    
    print("best\n", best_sol) 
    print("Ant: ", best_iter, "   ", best_ant.visited, "iteration: ", i) 
    print(better_list)
    # print("AM:\n", AM)  
    # print("FM:\n", FM)

    #plt.imshow(FM)
    #plt.show()
    #summary text for plot:
    text_summary = f"SUMMARY:\nBest road: {best_ant.visited}\nNumber of iterations: {i}\nDest. functio: {best_ant.dest_fun}\nStop criterion:{stop_crierion}\nTime: {end_ACO - start_ACO}\n\n"
    parameters_summary = f"PARAMETERS:\nBasket mass: {M0}\nDestination function distance constant: {C_dist}\n"+ \
                                    f"Fatigue constant: {C_fat}\n" + \
                                    f"Distance cosntant: {A_dist}\n" + \
                                    f"Feromone constant: {A_fer}\n" + \
                                    f"Feromone evaporation constant: {Evap}\n" + \
                                    f"Amount of feromones: {Fero_amount}\n" + \
                                    f"Feromone evaporation constant: {A_fer}\n" + \
                                    f"Disatnce to shop: {L0}\n" + \
                                    f"Fatigue of getting to shop: {F0}\n" + \
                                    f"Max. number of iterations: {Iter}\n" + \
                                    f"Epsilon: {A_fer}, Threshold: {threshold}"
    return best_ant.visited, best_ant_arr, FM, i, text_summary+parameters_summary


