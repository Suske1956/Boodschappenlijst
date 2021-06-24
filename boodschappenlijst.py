import sqlite3
import sys


class DatabaseOperations:
    def __init__(self):
        self.db_name = None

    def menu(self, database):
        self.db_name = database
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
            print('Press ENTER to continue')
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
        if answer.upper() == 'YES':
            conn = None
            try:
                conn = sqlite3.connect(self.db_name)
                c = conn.cursor()
                c.execute("DROP TABLE products")
                c.execute("DROP TABLE shops")
                c.execute("DROP TABLE prod_shop")
                conn.commit()
                print('Tables successfully removed')
            except sqlite3.Error as error:
                print('Error while removing a table', error)
            finally:
                if conn:
                    conn.close()
            try:
                conn = sqlite3.connect(self.db_name)
                c = conn.cursor()
                c.execute('''CREATE TABLE products (
                                               prod_name TEXT NOT NULL,
                                               prod_unit text NOT NULL,
                                               prod_required REAL,
                                               shop_id INTEGER);''')
                c.execute('''CREATE TABLE shops (
                                               shop_name TEXT);''')
                c.execute('''CREATE TABLE prod_shop (
                                               prod_id INTEGER,
                                               shop_id INTEGER,
                                               prod_price REAL);''')
                conn.commit()
                print('Tables successfully created')
                c.close()
            except sqlite3.Error as error:
                print("Error while creating a sqlite table", error)
            finally:
                if conn:
                    conn.close()

        else:
            print('\nABORTED!!\n')


class ProductMaintenance:
    def __init__(self):
        self.db_name = None

    def menu(self, database):
        self.db_name = database
        while True:
            print('\n    Producten menu, maak je keuze \n1:  Lijst producten \n2:  Producten toevoegen \n9:  Terug')
            keuze = input()
            if keuze == '1':
                print('1 gekozen')
            elif keuze == '2':
                # the while loop can be in a method returning True or False
                while True:
                    print('New product will be added continue? [Y/n]')
                    answer = input()
                    if answer.upper() == 'Y' or answer == '':
                        print('continue')
                        self.add_product()
                        break
                    elif answer.upper() == 'N':
                        print('back')
                        break

            elif keuze == '9':
                break
            else:
                print('Ongeldige keuze')

    def list_products(self):
        pass

    def add_product(self):
        print('add product')



    def remove_product(self):
        pass


# menu, note no "clear screen" since, afaik, this is not platform independent
class MainMenu:
    def __init__(self):
        self.db_name = 'boodschappenlijst.db'

    def menu(self):
        menu_text = '\n    Hoofdmenu maak je keuze\n1:  Tabellen\n2:  Onderhoud producten\n3: ' \
                    'Boodschappenlijst\n9: verlaten \n'
        keuze = input(menu_text)
        while keuze != '9':
            # print('\n    Hoofdmenu maak je keuze\n1:  Tabellen\n2:  Onderhoud producten\n3:  '
            #      'Boodschappenlijst\n9: verlaten ')
            if keuze == '1':
                print('1 gekozen')
                # operations.menu(self.db_name)
            elif keuze == '2':
                print('2 gekozen')
                # maintenance.menu(self.db_name)
            elif keuze == '3':
                print('3 gekozen')
            else:
                print('!!!ongeldige keuze!!!\n')
            keuze = input(menu_text)
        print('einde')
        sys.exit()


main_menu = MainMenu()
operations = DatabaseOperations()
maintenance = ProductMaintenance()
main_menu.menu()
