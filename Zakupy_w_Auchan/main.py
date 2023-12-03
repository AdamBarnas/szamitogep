from baza import Database
import struktury_danych as sd

def ant_algorithm(LZ: list[sd.Product], AM: list[float], FM: list[float]) -> list[sd.Product]:
    DL = []


    return DL

def main() -> None:
    db = Database()
    LZ = []
    for i in range(10):
        LZ.append(db.get_productinfo(i+1))
    # for product in LZ:
    #     print(product)

    AM = sd.calculate_adjacency_matrix(LZ)
    sd.print_matrix(AM)

    sd.show_points(LZ)
    return None

main()