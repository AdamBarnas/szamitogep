import sqlite3
from sqlite3 import Error
import struktury_danych as sd
import os

class Database:
    def __init__(self):
        base_path = os.path.abspath(os.path.dirname(__file__))
        self.database = os.path.join(base_path, "database", "data.db")
        self.conn = self.create_connection(self.database)


    def create_connection(self, db_file):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

        return conn


    def create_product(self, product: sd.Product) -> None:
        userfull = [product.ID, product.name, product.mass, product.coords[0], product.coords[1]]
        sql = ''' INSERT INTO products(id,name,mass,x_coord,y_coord)
                  VALUES(?,?,?,?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, userfull)
        self.conn.commit()
        return None

    def update_productinfo(self, product: sd.Product) -> None:
        changes = (product.mass, product.coords[0], product.coords[1], product.ID, product.name)
        sql = ''' UPDATE products
                          SET mass = ?,
                              x_coord = ?
                              y_coord = ?
                          WHERE id = ? AND name = ? '''
        cur = self.conn.cursor()
        cur.execute(sql, changes)
        self.conn.commit()
        return None

    def get_productinfo(self, id: int) -> sd.Product:
        sql = '''SELECT * FROM products WHERE id = ?'''
        cur = self.conn.cursor()
        cur.execute(sql, [id])
        dane = cur.fetchall()
        dane = dane[0]
        product = sd.Product(ID=dane[0], name=dane[1], mass=dane[3], coords=(dane[3], dane[4]))
        return product


    def delete_product(self, id: int) -> None:
        sql = '''DELETE FROM products WHERE id = ?'''
        cur = self.conn.cursor()
        cur.execute(sql, [id])
        self.conn.commit()
        return None

    def delete_all(self) -> None:
        sql = '''DELETE FROM products'''
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()
        return None
    