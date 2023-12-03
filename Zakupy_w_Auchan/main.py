from baza import Database
import struktury_danych as sd

def ant_algorithm(LZ: list[sd.Product]) -> list[sd.Product]:
    AM = sd.calculate_adjacency_matrix(LZ)
    FM = sd.create_feromone_matrix(LZ)
    
    return DL

def main() -> None:
    db = Database()

    # entry = sd.Product(0, sd.m0)

    LZ = []
    for i in range(10):
        LZ.append(db.get_productinfo(i+1))
    # for product in LZ:
    #     print(product)

    # AM = sd.calculate_adjacency_matrix(LZ)
    # print(AM)

    # FM = sd.create_feromone_matrix(LZ)
    # print(FM)

    sd.show_points(LZ)
    return None

main()