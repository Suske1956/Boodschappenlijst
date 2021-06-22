import sqlite3
import sys


class DatabaseOperations:
    def __init__(self):
        self.db_name = 'boodschappenlijst.db'
        # currently queries without parameters (this class is probably used once).
        # parameters to be added later on
        self.q_create_table_products = '''CREATE TABLE products (
                                prod_name TEXT NOT NULL,
                                prod_unit text NOT NULL,
                                prod_required REAL,
                                shop_id INTEGER);'''
        self.q_create_table_shops = '''CREATE TABLE shops (
                                shop_name TEXT);'''
        self.q_create_table_prod_shop = '''CREATE TABLE prod_shop (
                                prod_id INTEGER,
                                shop_id INTEGER,
                                prod_price REAL);'''
        self.q_drop_table_products = "DROP TABLE products"
        self.q_drop_table_shops = "DROP TABLE shops"
        self.q_drop_table_prod_shop = "DROP TABLE prod_shop"

    def menu(self):
        while True:
            print('\n    Tabellen menu, maak je keuze \n1:  Lijst tabellen \n2:  Tabellen verversen \n9:  Terug')
            keuze = input()
            if keuze == '1':
                print('1 gekozen')
                self.list_tables()
            elif keuze == '2':
                self.reset_database()
            elif keuze == '9':
                break
            else:
                print('Ongeldige keuze')

    def list_tables(self):
        conn = None
        try:
            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()
            c.execute("SELECT name FROM sqlite_master WHERE type='table';")
            conn.commit()
            tables = (c.fetchall())
            print('\nList of tables:')
            for item in tables:
                print(item[0])
            print('Druk op ENTER om door te gaan')
            input()
            c.close()
        except sqlite3.Error as error:
            print("Error while listing tables", error)
        finally:
            if conn:
                conn.close()

    def reset_database(self):
        print('ATTENTION:\n After resetting the database all data will be lost \nDo you want to continue? (yes/No\n')
        answer = input()
        print(answer.upper())
        if answer.upper() == 'YES':
            print('reset')
        else:
            print('aborted')

    # create table, arguments: table name (string) and column list (tuple of strings)
    def create_table(self):
        conn = None
        try:
            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()
            print("Successfully Connected to SQLite")
            c.execute(self.q_create_table_prod_shop)
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
        conn = None
        try:
            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()
            c.execute(self.q_drop_table_prod_shop)
            conn.commit()
            print('table successfully removed')
            c.close()
        except sqlite3.Error as error:
            print('Error while removing a table', error)
        finally:
            if conn:
                conn.close()
                print('sqlite connection is closed')


# menu, note no clear screen since is is, afaik, not platform independent
def menu():
    while True:
        print('\n    Hoofdmenu maak je keuze\n1:  Tabellen\n2:  Onderhoud producten\n3:  '
              'Boodschappenlijst\n9: verlaten ')
        keuze = input()
        if keuze == '1':
            operations.menu()
        elif keuze == '2':
            print('2 gekozen')
        elif keuze == '3':
            print('3 gekozen')
        elif keuze == '9':
            sys.exit()
        else:
            print('!!!ongeldige keuze!!!\n')


operations = DatabaseOperations()
menu()
# operations.list_tables()
# operations.create_table()
# operations.list_tables()
# operations.drop_table()
# operations.list_tables()
