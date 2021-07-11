import sqlite3


class MenuExec:
    """
    MenuExec contains static method to execute a simple cli menu.
    The parameter data is a dictionary containing the data required to build yhe menu.
    A typical example of a dictionary:
            {   'title': 'Database Operations\n', 'options': [
                    {'title': 'Exit', 'function': self.stop},
                    {'title': 'List Tables,', 'function': self.list_tables},
                    {'title': 'Renew Tables', 'function': self.reset_database}
                ]}
    The title contains the menu title, printed on tot of the menu. The options contain the menu items.
    Each option consists of a title and a function. To exit the menu, without an error the static method
    stop() (without content) should be called.
    """
    @ staticmethod
    def menu(data):
        number = len(data['options'])
        print(data['title'])
        count = 0
        for x in data['options']:
            print(count, '  ', x['title'])
            count += 1

        y = None
        while y != 0:
            try:
                y = int(input('Choose an option\n'))
            except ValueError:
                print('Input Error, integer required')
            else:
                if y < number:
                    data['options'][y]['function']()
                else:
                    print('Input Error, out of scope')
                print(data['title'])
                count = 0
                for x in data['options']:
                    print(count, '  ', x['title'])
                    count += 1

    @staticmethod
    def stop():
        pass


class ShoppingList:
    """
    ShoppingList is the main class basically it holds the main menu of the application and the name of the
    database
    Within ShoppingList subclasses DataBaseOperations, ProductMaintenance and ShoppingList exist. Each of them
    holds its own submenu and the operations belonging to the group of operations.
    For documentation regarding the cli menu see MenuExec
    """

    class DataBaseOperations:
        """
        The class DataBaseOperations holds functions to list th tables in the database and to renew
        the database tables, erasing all data.
        """
        def __init__(self, dbname):
            self.db_name = dbname
            self.menu_func = MenuExec
            self.menu_data = {
                'title': 'Database Operations\n', 'options': [
                    {'title': 'Exit', 'function': self.menu_func.stop},
                    {'title': 'List Tables,', 'function': self.list_tables},
                    {'title': 'Renew Tables', 'function': self.reset_database}
                ]
            }

        def menu_db_opr(self):
            self.menu_func.menu(self.menu_data)

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
            print('ATTENTION:\n After resetting the database all data will be lost \n'
                  'Do you want to continue? (yes/No\n')
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
        """

        """
        def __init__(self, dbname):
            self.db_name = dbname
            pass

        def test(self):
            print('in maintenance')

    class ShoppingList:
        """

        """
        def __init__(self, dbname):
            self.db_name = dbname
            pass

        def test(self):
            print('in shopping list')

    def __init__(self):
        self.db_name = 'shopping_list.db'
        self.db_operations = self.DataBaseOperations(self.db_name)
        self.prod_maintenance = self.ProductMaintenance(self.db_name)
        self.shopping_list = self.ShoppingList(self.db_name)
        self.menu_func = MenuExec()
        self.menu_data = {
            'title': 'Main Menu\n', 'options': [
                {'title': 'Exit', 'function': self.menu_func.stop},
                {'title': 'Database Operations,', 'function': self.db_operations.menu_db_opr},
                {'title': 'Product maintenance', 'function': self.prod_maintenance.test},
                {'title': 'Shopping list', 'function': self.shopping_list.test}
            ]
        }
        self.menu_func.menu(self.menu_data)


shopping_list = ShoppingList()