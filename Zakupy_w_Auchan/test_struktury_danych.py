import pytest
import coverage
import numpy as np
from baza import Database
import struktury_danych as sd

class TestAnt:
    def test_Ant_goto_next_product(self):
        product_1 = sd.Product(1, 1, (1, 1), "1")
        product_2 = sd.Product(2, 2, (2, 2), "2")
        ant = sd.Ant(product_1)
        ant.goto_next_product(product_2)
        assert ant.visited == [1, 2]

    def test_choose_next_product(self):
        shop_entry = sd.Product(sd.entry_ID, sd.M0, sd.entry_coords1, "ENTER")
        product_1 = sd.Product(1, 1, (1, 1), "1")
        product_2 = sd.Product(2, 2, (2, 2), "2")
        shop_exit = sd.Product(sd.exit_ID, 0, sd.exit_coords1, "EXIT")
        LZ = [shop_entry, product_1, product_2, shop_exit]
        AM = sd.calculate_adjacency_matrix(LZ)
        FM = sd.create_feromone_matrix(LZ)
        ant = sd.Ant(product_1)
        id = ant.choose_next_product(AM, FM, 0.5)
        assert id == 2

    def test_Ant_arrange_visited_1(self):
        shop_entry = sd.Product(sd.entry_ID, sd.M0, sd.entry_coords1, "ENTER")
        product_1 = sd.Product(1, 1, (1, 1), "1")
        product_2 = sd.Product(2, 2, (2, 2), "2")
        product_3 = sd.Product(3, 3, (3, 3), "3")
        ant = sd.Ant(product_1)
        ant.goto_next_product(product_3)
        ant.goto_next_product(product_2)
        ant.goto_next_product(shop_entry)
        ant.arrange_visited()
        assert ant.visited == [0, 1, 3, 2]

    def test_Ant_arrange_visited_2(self):
        shop_entry = sd.Product(sd.entry_ID, sd.M0, sd.entry_coords1, "ENTER")
        product_1 = sd.Product(1, 1, (1, 1), "1")
        product_2 = sd.Product(2, 2, (2, 2), "2")
        product_3 = sd.Product(3, 3, (3, 3), "3")
        ant = sd.Ant(product_3)
        ant.goto_next_product(product_1)
        ant.goto_next_product(product_2)
        ant.goto_next_product(shop_entry)
        ant.arrange_visited()
        assert ant.visited == [0, 3, 1, 2]

    def test_Ant_arrange_visited_3(self):
        shop_entry = sd.Product(sd.entry_ID, 1, sd.entry_coords1, "ENTER")
        product_1 = sd.Product(1, 2, (10, 10), "1")
        product_2 = sd.Product(2, 2, (20, 20), "2")
        product_3 = sd.Product(3, 3, (30, 30), "3")
        shop_exit = sd.Product(sd.exit_ID, 0, sd.exit_coords1, "EXIT")
        LZ = [shop_entry, product_1, product_2, product_3, shop_exit]
        AM = sd.calculate_adjacency_matrix(LZ)
        ant = sd.Ant(product_1)
        ant.goto_next_product(product_2)
        ant.goto_next_product(shop_exit)
        ant.goto_next_product(product_3)
        ant.arrange_visited()
        assert ant.visited == [0, 3, 1, 2, -1]

    def test_calculate_destination_function_1(self):
        shop_entry = sd.Product(sd.entry_ID, 1, (0, 0), "ENTER")
        product_1 = sd.Product(1, 1, (1, 1), "1")
        product_2 = sd.Product(2, 0, (2, 2), "2")
        LZ = [shop_entry, product_1, product_2]
        AM = sd.calculate_adjacency_matrix(LZ)
        ant = sd.Ant(product_1)
        ant.goto_next_product(product_2)
        ant.goto_next_product(shop_entry)
        ant.calculate_destination_function(LZ, AM)
        assert ant.dest_fun == 10

    def test_calculate_destination_function_2(self):
        shop_entry = sd.Product(sd.entry_ID, 1, sd.entry_coords1, "ENTER")
        product_1 = sd.Product(1, 2, (10, 10), "1")
        product_2 = sd.Product(2, 2, (20, 20), "2")
        product_3 = sd.Product(3, 3, (30, 30), "3")
        shop_exit = sd.Product(sd.exit_ID, 0, sd.exit_coords1, "EXIT")
        LZ = [shop_entry, product_1, product_2, product_3, shop_exit]
        AM = sd.calculate_adjacency_matrix(LZ)
        ant = sd.Ant(product_1)
        ant.goto_next_product(product_2)
        ant.goto_next_product(shop_exit)
        ant.goto_next_product(product_3)
        ant.calculate_destination_function(LZ, AM)
        assert ant.dest_fun == 2288
    
def test_create_feromone_matrix():
    db = Database()

    shop_entry = sd.Product(0, sd.M0, sd.entry_coords1, "ENTER")

    LZ = [shop_entry]
    for i in range(10):
        LZ.append(db.get_productinfo(i+1))

    FM = sd.create_feromone_matrix(LZ)

    assert FM.size == np.ndarray([11, 11]).size
    assert FM.shape[0] == np.ndarray([11, 11]).shape[0]
    assert FM.shape[1] == np.ndarray([11, 11]).shape[1]

def test_calculate_adjacency_matrix():
    db = Database()

    shop_entry = sd.Product(0, sd.M0, sd.entry_coords1, "ENTER")

    LZ = [shop_entry]
    for i in range(10):
        LZ.append(db.get_productinfo(i+1))

    AM = sd.calculate_adjacency_matrix(LZ)

    assert AM.size == np.ndarray([11, 11]).size
    assert AM.shape[0] == np.ndarray([11, 11]).shape[0]
    assert AM.shape[1] == np.ndarray([11, 11]).shape[1]

