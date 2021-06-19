import sqlite3
import sys

class DatabaseOperations:
    def __init__(self):
        self.db_name = 'boodschappenlijst.db'
        self.q_create_table = '''CREATE TABLE SqliteDb_developers (
                                        id INTEGER PRIMARY KEY,
                                        name TEXT NOT NULL,
                                        email text NOT NULL UNIQUE,
                                        joining_date datetime,
                                        salary REAL NOT NULL);'''
        self.q_sqlite_version = "select sqlite_version();"

    def connect_2_database(self):
        try:
            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()
            print("Successfully Connected to: " + self.db_name)

            # c.execute(self.q_sqlite_version)
            c.execute("SELECT name FROM sqlite_master WHERE type='table';")
            conn.commit()
            print(c.fetchall())

            c.close()

        except sqlite3.Error as error:
            print("Error while creating a sqlite table", error)
        finally:
            if conn:
                conn.close()
                print("sqlite connection is closed")

    # create table, arguments: table name (string) and column list (tuple of strings)
    def create_table(self):
        try:
            conn = sqlite3.connect(self.db_name)
            sqlite_create_table_query = '''CREATE TABLE SqliteDb_developers (
                                        id INTEGER PRIMARY KEY,
                                        name TEXT NOT NULL,
                                        email text NOT NULL UNIQUE,
                                        joining_date datetime,
                                        salary REAL NOT NULL);'''

            c = conn.cursor()
            print("Successfully Connected to SQLite")
            c.execute(sqlite_create_table_query)
            conn.commit()
            print("SQLite table created")

            c.close()

        except sqlite3.Error as error:
            print("Error while creating a sqlite table", error)
        finally:
            if conn:
                conn.close()
                print("sqlite connection is closed")

    # delete table, arguments: table name (string)
    def drop_table(self):
        try:
            conn = sqlite3.connect(self.db_name)
            sqlite_drop_table_query = "DROP TABLE SqliteDb_developers"
            c = conn.cursor()
            c.execute(sqlite_drop_table_query)
            conn.commit()
            print('table successfully removed0')
            c.close()
        except sqlite3.Error as error:
            print("Error while creating a sqlite table", error)
        finally:
            if conn:
                conn.close()
                print("sqlite connection is closed")




class Database:
    def __init__(self):
        self.dbname = 'boodschappenlijst.db'

    # create table: columns is tuple example ('colname1 datatype', 'colname2 datatype')
    def create_table(self, tablename, columns):
        try:
            conn = sqlite3.connect(self.dbname)
            c = conn.cursor()
            c.execute("CREATE TABLE {} {}".format(tablename, columns))
            conn.close()
        except sqlite3.OperationalError:
            print('sqlite3 error')

    def drop_table(self, tablename):
        conn = sqlite3.connect(self.dbname)
        c = conn.cursor()
        c.execute("DROP TABLE {}".format(tablename))
        conn.close()

    def add_record(self, tablename, data):
        conn = sqlite3.connect(self.dbname)
        c = conn.cursor()
        c.execute("INSERT INTO {} VALUES {}".format(tablename, data))
        conn.commit()
        c.execute("SELECT * FROM test")
        print(c.fetchall())
        conn.close()

# menu, note no clear screen since is is, afaik, not platform independent
def menu():
    while True:
        print('Welkom maak je keuze \n1:  een \n2:  twee \n9: verlaten ')
        keuze = input()
        if keuze == '1':
            print('een gekozen')
        elif keuze == '2':
            print('2 gekozen')
        elif keuze == '9':
            print('verlaten')
            sys.exit()
        else:
            print('ongeldige keuze')


operations = DatabaseOperations()
menu()
# operations.connect_2_database()
# operations.create_table()
# operations.connect_2_database()
# operations.drop_table()
# operations.connect_2_database()

# db = Database()
# db.create_table('test', ('een text', 'twee text'))
# db.add_record('test', ('afja', 'jhsdakfha'))
# db.drop_table('test')
