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

    def list_tables(self):
        try:
            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()
            print("Successfully Connected to: " + self.db_name)
            c.execute("SELECT name FROM sqlite_master WHERE type='table';")
            conn.commit()
            print(c.fetchall())
            c.close()
        except sqlite3.Error as error:
            print("Error while listing tables", error)
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



# menu, note no clear screen since is is, afaik, not platform independent
def menu():
    while True:
        print('Welkom maak je keuze\n1:  Database\n2:  Onderhoud producten\n3:  Boodschappenlijst\n9: verlaten ')
        keuze = input()
        if keuze == '1':
            print('een gekozen')
        elif keuze == '2':
            print('2 gekozen')
        elif keuze == '3':
            print('3 gekozen')
        elif keuze == '9':
            sys.exit()
        else:
            print('!!!ongeldige keuze!!!\n')


operations = DatabaseOperations()
# menu()
operations.list_tables()
# operations.create_table()
operations.list_tables()
# operations.drop_table()
operations.list_tables()
