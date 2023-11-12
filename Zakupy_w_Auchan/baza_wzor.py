import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self):
        self.database = "database/data.db"
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


    def create_user(self, user, avatar=None):
        """
        Create a new project into the projects table
        :param conn:
        :param project:
        :return: project id
        """
        userfull = [user[0], user[1], 0, 0, avatar]
        sql = ''' INSERT INTO tabela(login,password,total_distance,XP,avatar)
                  VALUES(?,?,?,?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, userfull)
        self.conn.commit()
        return None

    def update_userinfo(self, user, distance, XP):
        """
        Create a new project into the projects table
        :param conn:
        :param project:
        :return: project id
        """
        changes = (distance, XP, user[0], user[1])
        sql = ''' UPDATE tabela
                          SET total_distance = ?,
                              XP = ?
                          WHERE login = ? AND password = ? '''
        cur = self.conn.cursor()
        cur.execute(sql, changes)
        self.conn.commit()
        return None

    def check_userinfo(self, user):
        sql = '''SELECT * FROM tabela WHERE login = ? and password = ?'''
        cur = self.conn.cursor()
        cur.execute(sql, user)
        nodes = cur.fetchall()
        if len(nodes) > 0:
            pass
        else:
            self.create_user(user)

    def get_userdata(self, user):
        sql = '''SELECT * FROM tabela WHERE login = ? AND password = ?'''
        cur = self.conn.cursor()
        cur.execute(sql, user)
        dane = cur.fetchall()
        return dane


    def delete_user(self, user):
        """
        Delete a task by task id
        :param conn:  Connection to the SQLite database
        :param id: id of the task
        :return:
        """
        sql = 'DELETE FROM tabela WHERE login = ? AND password = ?'
        cur = self.conn.cursor()
        cur.execute(sql, user)
        self.conn.commit()

    def delete_all(self):
        """
        Delete a task by task id
        :param conn:  Connection to the SQLite database
        :param id: id of the task
        :return:
        """
        sql = 'DELETE FROM tabela'
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()



class Trasa:
    def __init__(self):
        self.database = "database/trasa.db"
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

    def create_node(self, coords):
        node = [coords[0], coords[1], 0]
        sql = ''' INSERT INTO tabela(lon, lat, visit)
                  VALUES(?,?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, node)
        self.conn.commit()

    def update_node(self, coords):
        min_lat, min_lon, max_lat, max_lon = coords
        sql = ''' UPDATE tabela
                          SET visit = 1
                          WHERE visit = 0 AND lon > %s AND lon < %s AND lat > %s AND lat < %s '''%(min_lon, max_lon, min_lat, max_lat)

    def get_nodes(self, coords):
        min_lat, min_lon, max_lat, max_lon = coords
        sql = '''SELECT * FROM tabela WHERE lon > %s AND lon < %s AND lat > %s AND lat < %s '''%(min_lon, max_lon, min_lat, max_lat)
        cur = self.conn.cursor()
        cur.execute(sql)
        nodes = cur.fetchall()
        nodesy = []
        for node in nodes:
            node = (node[0], node[1])
            nodesy.append(node)
        return nodesy

    def get_visted(self, coords):
        min_lat, min_lon, max_lat, max_lon = coords
        sql = '''SELECT * FROM tabela WHERE visit = 1 AND lon > %s AND lon < %s AND lat > %s AND lat < %s '''%(min_lon, max_lon, min_lat, max_lat)
        cur = self.conn.cursor()
        cur.execute(sql)
        nodes = cur.fetchall()
        nodesy = []
        for node in nodes:
            node = (node[0], node[1])
            nodesy.append(node)
        return nodesy

    def get_not_visted(self, coords):
        min_lat, min_lon, max_lat, max_lon = coords
        sql = '''SELECT * FROM tabela WHERE visit = 0 AND lon > %s AND lon < %s AND lat > %s AND lat < %s '''%(min_lon, max_lon, min_lat, max_lat)
        cur = self.conn.cursor()
        cur.execute(sql)
        nodes = cur.fetchall()
        nodesy = []
        for node in nodes:
            node = (node[0], node[1])
            nodesy.append(node)
        return nodesy

    def delete_trip(self):
        """
        Delete a task by task id
        :param conn:  Connection to the SQLite database
        :param id: id of the task
        :return:
        """
        sql = 'DELETE FROM tabela'
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()

class Miejsca:
    def __init__(self):
        self.database = "database/miejsca.db"
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

    def convertToBinaryData(self, filename):
        # Convert digital data to binary format
        with open(filename, 'rb') as file:
            blobData = file.read()
        return blobData

    def create_place(self, place, obrazek):
        # place = [nazwa, lon, lat, opis]
        binob = self.convertToBinaryData(obrazek)
        calosc = [place[1], place[2], place[0], place[3], binob]
        sql = ''' INSERT INTO tabela(lon, lat, nazwa, opis, obrazek)
                  VALUES(?,?,?,?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, calosc)
        self.conn.commit()

    def get_places(self, coords, style):
        min_lon, min_lat, max_lon, max_lat = coords
        sql = '''SELECT * FROM tabela WHERE lon > ? AND lon < ? AND lat > ? AND lat < ? '''
        cur = self.conn.cursor()
        cur.execute(sql, (min_lon, max_lon, min_lat, max_lat))
        places = cur.fetchall()
        miejsca = []
        for place in places:
            place = (place[0], (place[1], place[2]))
            miejsca.append(place)
        return miejsca



def main():
    baza = Database()
    baza.delete_all()
    user = ('nick', "haslo")
    # baza.create_user(user)
    baza.check_userinfo(user)
    print(baza.get_userdata(user))
    # baza.delete_user(user)

    # trasa = Trasa()
    # trasa.create_node((23, 23))
    # trasa.create_node((25, 25))
    # print(trasa.get_not_visted((10, 12, 40, 40)))
    # trasa.delete_trip()

if __name__ == '__main__':
    main()