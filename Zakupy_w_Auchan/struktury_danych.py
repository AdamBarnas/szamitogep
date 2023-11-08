import typing

#constans
m0 = 0.5  #masa pustego koszyka
c_l = 1   #destination function distance constant
c_f = 1   #destination function fatigue constant
L0 = 500  #distance to the shop
F0 = 100  #fatigue of getting to the shop

#types
coords_t = tuple[float, float]

#shopping list
LZ = []
#state list
LS = []
#decision list
DL = []
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

class Decision:
    def __init__(self, item: Product) -> None:
        self.ID = item.ID #selected product ID
        self.mass = item.mass #selected product mass
        self.coords = item.coords #selected product coordinates

def calculate_distance(coords1: coords_t, coords2: coords_t) -> float:
    distance = 0
    for i in range(len(coords1)):
        distance += abs(coords1[i] - coords2[i])
    return distance

def calculate_fatigue(distance, mass) -> float:
    return distance * mass

def transfer_function(S: State, D: Decision):
    B = S.B
    if D.ID not in B:
        B.append(D.ID)
    else:
        print("Item already in a basket")
        return None
    mass = S.mass + D.mass
    coords = D.coords
    distance = calculate_distance(S.coords, D.coords)
    L = S.L + distance
    F = S.F + calculate_fatigue(distance, S.mass)
    newstate = State(B, mass, coords, L, F)
    return newstate
